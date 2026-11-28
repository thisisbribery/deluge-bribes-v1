#!/usr/bin/env python3
"""Bribeluge CPU bench: reads the 0x59 CPU stream over USB MIDI and drives the Deluge.

Needs Bribeluge v1.49 or later on the Deluge, plugged in over USB, and Python 3 with mido and python-rtmidi:
    pip install mido python-rtmidi
    python3 deluge_bench.py ports
    python3 deluge_bench.py watch
    python3 deluge_bench.py run --seconds 30 --play --label 303-baseline
    python3 deluge_bench.py sweep --channel 1 --max 16
    python3 deluge_bench.py compare results/a.json results/b.json
    python3 deluge_bench.py snap --label empty        (empty song: the RAM baseline)
    python3 deluge_bench.py snap --label tribe-808    (after loading a kit)
    python3 deluge_bench.py ledger                    (every kit: RAM taken, CPU playing)

    python3 deluge_bench.py rammap --label empty      (every allocation by size: on-chip, small, SDRAM)
    python3 deluge_bench.py ramdiff empty tribe-808   (what a kit added, named by object)

Protocol (all 7-bit, numbers MSB first). Nothing is sent and nothing is timed unless asked for:
  out: F0 00 21 7B 01 02 03 12 <period x 10 ms, 0 = stop> F7   (repeat about once a second; stops 3 s after the last)
       F0 00 21 7B 01 02 03 13 <region> F7                     (one RAM map: 1 on-chip, 2 SDRAM, 3 SDRAM small,
                                                                4 on-chip small)
       F0 00 21 7B 01 02 03 08 00 F7                            (press PLAY)
  in:  F0 00 21 7B 01 02 59 <version 2> <seq> <flags: 1 = playing>
       audio ticks/samples, voices ticks/samples, drum osc ticks/samples   (28-bit each, running totals)
       peak ticks (28) peak samples (14) longest render (14)               (since the last message)
       voices (14) audio clip voices (14) direness (7) culls (28, running)
       internal RAM free (28) largest (28) internal small free (28) largest (28)
       SDRAM free (28) largest (28) SDRAM small free (28) largest (28)
       <n> then n x: <kind> ticks (28) samples (28)                       (whole voice time per kind, running)
       <n> then n x: <kind> ticks (28) samples (28)                       (whole Sound::render per kind, running)
       <n> then n x: ticks (28) samples (28)                              (render sections, cpu_meter::Section order)
       kinds: drum_synth::Engine numbers, 40 sample, 41 subtractive, 42 FM, 43 ringmod, 44 303
       F0 00 21 7B 01 02 70 <version 1> <region> <stopped early> size, allocated, allocations, empty, stealable,
       other bytes, other count (28 each), <n> then n x: slot size (28) count (28)   (biggest total first)
  ticks are 33.33 MHz, samples 44.1 kHz.
"""

import argparse
import csv
import json
import os
import statistics
import sys
import threading
import time

TICKS_PER_SECOND = 33_330_000
SAMPLE_RATE = 44_100
WRAP28 = 1 << 28
HDR = [0x00, 0x21, 0x7B, 0x01, 0x02]  # mido drops F0 / F7

# drum_synth::Engine order (append-only in the firmware), then the cpu_meter kinds from 40
KIND_NAMES = {
    0: "LXR kick/tom", 1: "LXR snare", 2: "LXR cymbal", 3: "DXIA", 4: "DIIA",
    5: "Cyc kick", 6: "Cyc snare", 7: "Cyc metal", 8: "Cyc perc", 9: "Cyc tone", 10: "Cyc chord",
    11: "Vtg snare", 12: "Clap", 13: "GIN", 14: "ULTRAKIK", 15: "BRINGS", 16: "BROPHET", 17: "BRUNO106",
    18: "TRIBE kick", 19: "TRIBE snare", 20: "TRIBE clap", 21: "TRIBE tom", 22: "TRIBE rim", 23: "TRIBE hat",
    24: "TRIBE cymbal", 25: "TRIBE cowbell",
    40: "Sample", 41: "Subtractive", 42: "FM", 43: "Ringmod", 44: "303",
}


# cpu_meter::Section order
SECTION_NAMES = ["synth tracks", "kit tracks", "audio tracks", "MIDI/CV tracks", "kit rows", "kit param ticks",
                 "reverb", "song FX", "preview", "metronome"]

# sizeof() in the v1.49 arm build, to name RAM map sizes (Sound/SoundDrum/Kit as before v1.49 shrank them, but they
# land in the same slots either way except SoundDrum and Kit, now 2040)
KNOWN_SIZES = {
    2024: "SoundDrum (kit row)", 2256: "SoundInstrument (synth track)", 1760: "Voice", 924: "drum engine voice",
    256: "NoteRow", 3136: "InstrumentClip", 1980: "Kit", 1184: "PatchedParamSet", 948: "UnpatchedParamSet",
    84: "ExpressionParamSet", 1056: "PatchCableSet", 144: "VoiceSample", 128: "MultisampleRange",
    120: "SampleHolderForVoice", 360: "Sample", 112: "Cluster",
}


def pad_size(size, min_align=64, max_align=4096):
    """MemoryRegion::padSize: add the 8 header bytes, round each 4 KB chunk's remainder up to a power of two"""
    size += 8
    if size < min_align:
        return min_align - 8
    extra = 0
    while size > max_align:
        extra += max_align
        size -= max_align
    if size & (size - 1):
        size = 1 << size.bit_length()
    return size + extra - 8


def size_name(size):
    """Objects that land in this padded slot size"""
    names = [n for sz, n in sorted(KNOWN_SIZES.items(), key=lambda kv: -kv[0]) if pad_size(sz) == size]
    return ", ".join(names)


def kind_name(k):
    return KIND_NAMES.get(k, "engine %d" % k)


# ---- Decoding ----

def decode(data):
    """mido sysex data (no F0/F7) -> dict, or None if it isn't a CPU message"""
    data = list(data)
    if data[:5] != HDR or len(data) < 7 or data[5] != 0x59:
        return None
    b = data[6:]
    if b[0] not in (1, 2):
        raise ValueError("CPU stream version %d, this script knows 1 and 2" % b[0])
    i = 3

    def u28():
        nonlocal i
        v = (b[i] << 21) | (b[i + 1] << 14) | (b[i + 2] << 7) | b[i + 3]
        i += 4
        return v

    def u14():
        nonlocal i
        v = (b[i] << 7) | b[i + 1]
        i += 2
        return v

    def u7():
        nonlocal i
        v = b[i]
        i += 1
        return v

    m = {"seq": b[1], "playing": bool(b[2] & 1), "t": time.time()}
    for name in ("audio", "voices", "drum"):
        m[name] = (u28(), u28())
    m["peak_ticks"] = u28()
    m["peak_samples"] = u14()
    m["max_render"] = u14()
    m["num_voices"] = u14()
    m["num_audio"] = u14()
    m["direness"] = u7()
    m["culls"] = u28()
    m["int_free"], m["int_largest"] = u28(), u28()
    m["small_free"], m["small_largest"] = u28(), u28()
    m["ext_free"], m["ext_largest"] = u28(), u28()
    m["ext_small_free"], m["ext_small_largest"] = u28(), u28()
    n = u7()
    m["kinds"] = {}
    for _ in range(n):
        k = u7()
        m["kinds"][k] = (u28(), u28())
    m["sound_kinds"] = {}
    m["sections"] = []
    if b[0] >= 2:
        for _ in range(u7()):
            k = u7()
            m["sound_kinds"][k] = (u28(), u28())
        m["sections"] = [(u28(), u28()) for _ in range(u7())]
    return m


def d28(a, b):
    return (b - a) % WRAP28


def load_pct(ticks, samples):
    """Render time as % of real time"""
    if samples == 0:
        return 0.0
    return ticks * SAMPLE_RATE * 100.0 / (TICKS_PER_SECOND * samples)


def ns_per(ticks, samples):
    return ticks * 1e9 / (TICKS_PER_SECOND * samples) if samples else 0.0


def interval(prev, cur):
    """What happened between two messages"""
    if prev is None:
        return None
    dt_audio, ds_audio = d28(prev["audio"][0], cur["audio"][0]), d28(prev["audio"][1], cur["audio"][1])
    if ds_audio == 0 or ds_audio > SAMPLE_RATE * 5:
        return None  # Nothing rendered, or messages lost for so long the tick totals may have wrapped
    row = {
        "t": cur["t"],
        "playing": cur["playing"],
        "load": load_pct(dt_audio, ds_audio),
        "peak": load_pct(cur["peak_ticks"], cur["peak_samples"]),
        "max_render": cur["max_render"],
        "voices": cur["num_voices"],
        "audio_voices": cur["num_audio"],
        "direness": cur["direness"],
        "culls": d28(prev["culls"], cur["culls"]),
        "int_free": cur["int_free"],
        "int_largest": cur["int_largest"],
        "small_free": cur["small_free"],
        # The drum engines' own oscillators, inside their voices (the rest of a voice is the Deluge's filter, envelopes
        # and panning)
        "drum_osc": load_pct(d28(prev["drum"][0], cur["drum"][0]), ds_audio),
        "ext_free": cur["ext_free"],
        "ext_small_free": cur["ext_small_free"],
        "kinds": {},
    }
    for k, (tk, sk) in cur["kinds"].items():
        # The Deluge only leaves out kinds that have never played, so one missing last time started from zero
        p = prev["kinds"].get(k, (0, 0))
        dt, ds = d28(p[0], tk), d28(p[1], sk)
        if ds:
            # share = this kind's time as % of real time; ns = per voice-sample (per output sample for the 303)
            row["kinds"][k] = {"share": load_pct(dt, ds_audio), "ns": ns_per(dt, ds), "voice_samples": ds}
    # v2: whole row / synth track render per kind, and the parts of the render, as % of real time
    row["sound_kinds"] = {}
    for k, (tk, sk) in cur["sound_kinds"].items():
        p = prev["sound_kinds"].get(k, (0, 0))
        row["sound_kinds"][k] = load_pct(d28(p[0], tk), ds_audio)
    row["sections"] = {}
    if len(prev["sections"]) == len(cur["sections"]):
        for i, ((pt, _), (ct, _)) in enumerate(zip(prev["sections"], cur["sections"])):
            row["sections"][SECTION_NAMES[i] if i < len(SECTION_NAMES) else "section %d" % i] = load_pct(d28(pt, ct),
                                                                                                         ds_audio)
    return row


# ---- MIDI ----

class Deluge:
    def __init__(self, port_hint=None):
        import mido
        self.mido = mido
        ins = mido.get_input_names()
        outs = mido.get_output_names()
        pick = lambda names: next((n for n in names if (port_hint or "deluge").lower() in n.lower()), None)
        name_in, name_out = pick(ins), pick(outs)
        if not name_in or not name_out:
            sys.exit("No Deluge MIDI port. Inputs: %s" % (ins or "none"))
        self.inp = mido.open_input(name_in, callback=self._on_msg)
        self.out = mido.open_output(name_out)
        self.lock = threading.Lock()
        self.messages = []
        self.latest = None
        self.period = 10
        self._stop = threading.Event()
        self._keep = threading.Thread(target=self._keepalive, daemon=True)

    def _on_msg(self, msg):
        if msg.type != "sysex":
            return
        try:
            m = decode(msg.data)
        except (IndexError, ValueError) as e:
            print("bad CPU message:", e, file=sys.stderr)
            return
        if m:
            with self.lock:
                self.messages.append(m)
                self.latest = m

    def sysex(self, body):
        self.out.send(self.mido.Message("sysex", data=HDR + body))

    def _keepalive(self):
        while not self._stop.is_set():
            self.sysex([0x03, 0x12, self.period])
            self._stop.wait(1.0)

    def start(self, period_ms=100):
        self.period = max(2, min(100, period_ms // 10))
        self._keep.start()

    def wait_first(self, timeout=4.0):
        end = time.time() + timeout
        while time.time() < end:
            if self.latest:
                return self.latest
            time.sleep(0.05)
        sys.exit("No CPU stream from the Deluge. Is Bribeluge v1.49 (or later) on it?")

    def press_play(self):
        self.sysex([0x03, 0x08, 0x00])

    def set_playing(self, want):
        m = self.wait_first()
        if m["playing"] != want:
            self.press_play()
            time.sleep(0.4)

    def note(self, channel, note, velocity):
        t = "note_on" if velocity else "note_off"
        self.out.send(self.mido.Message(t, channel=channel - 1, note=note, velocity=velocity))

    def close(self):
        self._stop.set()
        try:
            self.sysex([0x03, 0x12, 0x00])
        finally:
            self.inp.close()
            self.out.close()

    def take(self):
        with self.lock:
            msgs, self.messages = self.messages, []
        return msgs


def rows_from(msgs, prev=None):
    rows = []
    for m in msgs:
        r = interval(prev, m)
        if r:
            rows.append(r)
        prev = m
    return rows, prev


# ---- Reports ----

def pct(xs, q):
    if not xs:
        return 0.0
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(q * (len(xs) - 1))))]


def summarise(rows, label):
    loads = [r["load"] for r in rows]
    peaks = [r["peak"] for r in rows]
    kinds = {}
    sec_tot, sound_tot = {}, {}
    for r in rows:
        for name, v in r.get("sections", {}).items():
            sec_tot[name] = sec_tot.get(name, 0.0) + v
        for k, v in r.get("sound_kinds", {}).items():
            sound_tot[k] = sound_tot.get(k, 0.0) + v
    for r in rows:
        for k, v in r["kinds"].items():
            e = kinds.setdefault(k, {"share": [], "ns_t": 0.0, "vs": 0})
            e["share"].append(v["share"])
            e["ns_t"] += v["ns"] * v["voice_samples"]
            e["vs"] += v["voice_samples"]
    n = len(rows) or 1
    return {
        "label": label,
        "seconds": round(rows[-1]["t"] - rows[0]["t"], 1) if rows else 0,
        "messages": len(rows),
        "load_avg": round(statistics.mean(loads), 2) if loads else 0,
        "load_p95": round(pct(loads, 0.95), 2),
        "load_max": round(max(loads), 2) if loads else 0,
        "peak_max": round(max(peaks), 2) if peaks else 0,
        "voices_avg": round(statistics.mean(r["voices"] for r in rows), 1) if rows else 0,
        "drum_osc_avg": round(statistics.mean(r.get("drum_osc", 0) for r in rows), 2) if rows else 0,
        "voices_max": max((r["voices"] for r in rows), default=0),
        "culls": sum(r["culls"] for r in rows),
        "direness_max": max((r["direness"] for r in rows), default=0),
        "longest_render": max((r["max_render"] for r in rows), default=0),
        "int_free_min": min((r["int_free"] for r in rows), default=0),
        "int_largest_min": min((r["int_largest"] for r in rows), default=0),
        "small_free_min": min((r["small_free"] for r in rows), default=0),
        "ext_free_min": min((r["ext_free"] for r in rows), default=0),
        "ext_small_free_min": min((r["ext_small_free"] for r in rows), default=0),
        "kinds": {
            kind_name(k): {
                "share_avg": round(sum(e["share"]) / n, 2),
                "ns_per_voice_sample": round(e["ns_t"] / e["vs"]) if e["vs"] else 0,
                # The row's own processing around its voices (v2)
                "outside_voices": round((sound_tot.get(k, 0.0) - sum(e["share"])) / n, 2) if k in sound_tot else None,
            }
            for k, e in sorted(kinds.items(), key=lambda kv: -sum(kv[1]["share"]))
        },
        "rows_total": {kind_name(k): round(v / n, 2) for k, v in sorted(sound_tot.items(), key=lambda kv: -kv[1])},
        "sections": {name: round(v / n, 2) for name, v in sec_tot.items()},
    }


def print_summary(s):
    print("\n== %s: %.1f s, %d readings" % (s["label"], s["seconds"], s["messages"]))
    print("load avg %.1f%%  p95 %.1f%%  max %.1f%%  worst single render %.1f%%" % (
        s["load_avg"], s["load_p95"], s["load_max"], s["peak_max"]))
    print("voices avg %.1f max %d  culls %d  direness max %d  longest render %d samples" % (
        s["voices_avg"], s["voices_max"], s["culls"], s["direness_max"], s["longest_render"]))
    print("on-chip RAM free min %.1f KB (largest block %.1f KB), small objects %.1f KB; SDRAM free %.1f MB" % (
        s["int_free_min"] / 1024, s["int_largest_min"] / 1024, s["small_free_min"] / 1024,
        s["ext_free_min"] / 1048576))
    if s["kinds"]:
        print("%-16s %8s %14s %10s" % ("kind", "voices %", "ns/voice-smp", "row own %"))
        for name, v in s["kinds"].items():
            own = v.get("outside_voices")
            print("%-16s %8.2f %14d %10s" % (name, v["share_avg"], v["ns_per_voice_sample"],
                                             "%.2f" % own if own is not None else "-"))
    sec = s.get("sections") or {}
    if sec:
        kit, rows, ticks = sec.get("kit tracks", 0), sec.get("kit rows", 0), sec.get("kit param ticks", 0)
        tracks = sum(sec.get(k, 0) for k in ("synth tracks", "kit tracks", "audio tracks", "MIDI/CV tracks"))
        glob = sum(sec.get(k, 0) for k in ("reverb", "song FX", "preview", "metronome"))
        voices = sum(v["share_avg"] for v in s["kinds"].values())
        rows_total = sum(s.get("rows_total", {}).values())
        print("where the %.1f%% goes:" % s["load_avg"])
        print("  voices                    %6.1f%%" % voices)
        engine_voices = sum(v["share_avg"] for k, v in s["kinds"].items() if not k.startswith(
            ("Sample", "Subtractive", "FM", "Ringmod", "303")))
        if engine_voices:
            osc = s.get("drum_osc_avg", 0)
            print("    drum engines themselves  %6.1f%%" % osc)
            print("    their Deluge voice chain %6.1f%%  (filters, envelopes, pan, mixing into the row)" % (
                engine_voices - osc))
        print("  rows' own processing      %6.1f%%  (each row's Sound around its voices)" % (rows_total - voices))
        print("  kit FX                    %6.1f%%  (kit track - rows - param ticks)" % (kit - rows - ticks))
        print("  kit param ticks           %6.1f%%" % ticks)
        print("  synth/audio/MIDI tracks   %6.1f%%  (synth includes its voices above)" % (tracks - kit))
        for k in ("reverb", "song FX", "preview", "metronome"):
            print("  %-25s %6.1f%%" % (k, sec.get(k, 0)))
        print("  rest of the engine        %6.1f%%  (buffers, mixing, sidechain, monitoring)" % (
            s["load_avg"] - tracks - glob))


def write_results(rows, summary, label):
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"), exist_ok=True)
    stem = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results",
                        time.strftime("%Y%m%d-%H%M%S") + "-" + label)
    kind_ids = sorted({k for r in rows for k in r["kinds"]})
    with open(stem + ".csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t", "playing", "load", "peak", "voices", "audio_voices", "direness", "culls", "max_render",
                    "int_free", "int_largest"] + ["%s load" % kind_name(k) for k in kind_ids])
        t0 = rows[0]["t"] if rows else 0
        for r in rows:
            w.writerow([round(r["t"] - t0, 2), int(r["playing"]), round(r["load"], 2), round(r["peak"], 2),
                        r["voices"], r["audio_voices"], r["direness"], r["culls"], r["max_render"], r["int_free"],
                        r["int_largest"]] + [round(r["kinds"].get(k, {}).get("share", 0), 2) for k in kind_ids])
    with open(stem + ".json", "w") as f:
        json.dump(summary, f, indent=1)
    print("saved %s.csv and .json" % stem)


# ---- Commands ----

def cmd_ports(_):
    import mido
    print("in: ", mido.get_input_names())
    print("out:", mido.get_output_names())


def cmd_watch(a):
    d = Deluge(a.port)
    d.start(a.period)
    d.wait_first()
    prev = None
    try:
        while True:
            time.sleep(0.5)
            rows, prev = rows_from(d.take(), prev)
            if not rows:
                continue
            r = rows[-1]
            top = sorted(r["kinds"].items(), key=lambda kv: -kv[1]["share"])[:4]
            tops = "  ".join("%s %.1f%%" % (kind_name(k), v["share"]) for k, v in top if v["share"] >= 0.1)
            print("%s load %5.1f%% peak %5.1f%%  voices %3d  culls %2d  dire %2d  RAM %6.1f KB  %s" % (
                ">" if r["playing"] else " ", max(x["load"] for x in rows), max(x["peak"] for x in rows),
                r["voices"], sum(x["culls"] for x in rows), r["direness"], r["int_free"] / 1024, tops))
    except KeyboardInterrupt:
        pass
    finally:
        d.close()


def cmd_run(a):
    d = Deluge(a.port)
    d.start(a.period)
    d.wait_first()
    if a.play:
        d.set_playing(True)
    time.sleep(a.settle)
    d.take()
    print("measuring %s for %d s..." % (a.label, a.seconds))
    time.sleep(a.seconds)
    rows, _ = rows_from(d.take())
    if a.play and not a.keep_playing:
        d.set_playing(False)
    d.close()
    s = summarise(rows, a.label)
    print_summary(s)
    write_results(rows, s, a.label)


def cmd_sweep(a):
    """Hold more and more notes on one channel and log the load at each voice count"""
    d = Deluge(a.port)
    d.start(a.period)
    d.wait_first()
    notes = [a.note + (i * 7) % 36 + (i // 5) for i in range(a.max)]
    held = []
    results = []
    try:
        for n in notes:
            d.note(a.channel, n, 100)
            held.append(n)
            time.sleep(1.0)
            d.take()
            time.sleep(a.step_seconds)
            rows, _ = rows_from(d.take())
            s = summarise(rows, "%d notes" % len(held))
            results.append(s)
            print("%2d notes  voices %3d  load avg %5.1f%%  max %5.1f%%  culls %d" % (
                len(held), s["voices_max"], s["load_avg"], s["load_max"], s["culls"]))
            if s["culls"]:
                print("culling started")
                break
    finally:
        for n in held:
            d.note(a.channel, n, 0)
        d.close()
    if len(results) >= 2:
        per = (results[-1]["load_avg"] - results[0]["load_avg"]) / max(1, results[-1]["voices_max"] - results[0]["voices_max"])
        print("about %.2f%% load per extra voice" % per)
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"), exist_ok=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results",
                       time.strftime("%Y%m%d-%H%M%S") + "-sweep-" + a.label + ".json")
    with open(out, "w") as f:
        json.dump(results, f, indent=1)
    print("saved", out)


RESULTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")


def cmd_snap(a):
    """Memory (and idle load) right now, averaged over a few seconds: take one on an empty song as the baseline,
    then one after loading each kit. RAM cost of a kit = baseline free - free now."""
    d = Deluge(a.port)
    d.start(a.period)
    d.wait_first()
    time.sleep(0.5)
    d.take()
    time.sleep(a.seconds)
    msgs = d.take()
    d.close()
    rows, _ = rows_from(msgs)
    snap = {
        "label": a.label, "time": time.strftime("%Y-%m-%d %H:%M:%S"), "kind": "snap",
        "int_free": min(m["int_free"] for m in msgs), "int_largest": min(m["int_largest"] for m in msgs),
        "small_free": min(m["small_free"] for m in msgs), "ext_free": min(m["ext_free"] for m in msgs),
        "ext_small_free": min(m["ext_small_free"] for m in msgs),
        "idle_load": round(statistics.mean(r["load"] for r in rows), 2) if rows else 0,
        "voices": msgs[-1]["num_voices"],
    }
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "snap-%s.json" % a.label), "w") as f:
        json.dump(snap, f, indent=1)
    base = _load_snap(a.baseline) if a.baseline and a.baseline != a.label else None
    print("%s: on-chip free %.1f KB (largest %.1f KB), small %.1f KB, SDRAM free %.2f MB, idle load %.1f%%" % (
        a.label, snap["int_free"] / 1024, snap["int_largest"] / 1024, snap["small_free"] / 1024,
        snap["ext_free"] / 1048576, snap["idle_load"]))
    if base:
        print("vs %s: on-chip %+.1f KB, small %+.1f KB, SDRAM %+.1f KB, idle load %+.1f%%" % (
            base["label"], (snap["int_free"] - base["int_free"]) / -1024,
            (snap["small_free"] - base["small_free"]) / -1024, (snap["ext_free"] - base["ext_free"]) / -1024,
            snap["idle_load"] - base["idle_load"]))


def _load_snap(label):
    p = os.path.join(RESULTS, "snap-%s.json" % label)
    return json.load(open(p)) if os.path.exists(p) else None


def cmd_ledger(a):
    """One table of every kit measured: RAM taken (from its snap vs the baseline) and CPU while playing (newest run
    with the same label)"""
    base = _load_snap(a.baseline)
    runs = {}
    for name in sorted(os.listdir(RESULTS)):
        if name.endswith(".json") and not name.startswith(("snap-", "sweep")) and "-sweep-" not in name:
            s = json.load(open(os.path.join(RESULTS, name)))
            if isinstance(s, dict) and "load_avg" in s:
                runs[s["label"]] = s  # Sorted by time, so the newest wins
    labels = sorted(set(runs) | {n[5:-5] for n in os.listdir(RESULTS) if n.startswith("snap-")} - {a.baseline})
    print("%-18s %9s %9s %9s %8s %8s %8s %6s  %s" % ("kit", "chip KB", "small KB", "SDRAM KB", "load avg", "load p95",
                                                    "peak", "culls", "heaviest engine"))
    for label in labels:
        snap, run = _load_snap(label), runs.get(label)
        ram = ("%9.1f %9.1f %9.1f" % ((base["int_free"] - snap["int_free"]) / 1024,
                                      (base["small_free"] - snap["small_free"]) / 1024,
                                      (base["ext_free"] - snap["ext_free"]) / 1024)) if snap and base else "%29s" % "-"
        if run:
            heavy = next(iter(run["kinds"].items()), None)
            cpu = "%8.1f %8.1f %8.1f %6d  %s" % (run["load_avg"], run["load_p95"], run["peak_max"], run["culls"],
                                                 "%s %.1f%%" % (heavy[0], heavy[1]["share_avg"]) if heavy else "")
        else:
            cpu = "%8s %8s %8s %6s" % ("-", "-", "-", "-")
        print("%-18s %s %s" % (label[:18], ram, cpu))
    if not base:
        print("(no baseline snap '%s' yet: RAM columns need one)" % a.baseline)


def decode_rammap(data):
    data = list(data)
    if data[:5] != HDR or len(data) < 7 or data[5] != 0x70:
        return None
    b, i = data[6:], 3

    def u28():
        nonlocal i
        v = (b[i] << 21) | (b[i + 1] << 14) | (b[i + 2] << 7) | b[i + 3]
        i += 4
        return v

    m = {"region": b[1], "corrupt": bool(b[2])}
    for key in ("size", "allocated", "allocations", "empty", "stealable", "other_bytes", "other_count"):
        m[key] = u28()
    n = b[i]
    i += 1
    m["sizes"] = [(u28(), u28()) for _ in range(n)]
    return m


REGION_NAMES = {1: "on-chip", 2: "SDRAM", 3: "SDRAM small", 4: "on-chip small"}


def cmd_rammap(a):
    """Every live allocation in a region, grouped by size: take one per state (empty song, kit loaded) and diff"""
    import mido
    d = Deluge(a.port)
    maps = {}

    def on(msg):
        if msg.type == "sysex":
            m = decode_rammap(msg.data)
            if m:
                maps[m["region"]] = m
            else:
                Deluge._on_msg(d, msg)
    d.inp.callback = on
    for region in a.regions:
        d.sysex([0x03, 0x13, region])
        end = time.time() + 3
        while region not in maps and time.time() < end:
            time.sleep(0.05)
    d.close()
    out = {"label": a.label, "time": time.strftime("%Y-%m-%d %H:%M:%S"), "regions": {}}
    for region, m in sorted(maps.items()):
        out["regions"][REGION_NAMES[region]] = m
        print("== %s: %s, %.1f KB used in %d allocations, %.1f KB free%s" % (
            a.label, REGION_NAMES[region], m["allocated"] / 1024, m["allocations"], m["empty"] / 1024,
            " (WALK STOPPED: bad header)" if m["corrupt"] else ""))
        for size, count in m["sizes"][:a.top]:
            print("   %7d B x %4d = %8.1f KB  %s" % (size, count, size * count / 1024, size_name(size)))
    missing = [REGION_NAMES[r] for r in a.regions if r not in maps]
    if missing:
        print("no RAM map from:", ", ".join(missing))
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "rammap-%s.json" % a.label), "w") as f:
        json.dump(out, f, indent=1)


def cmd_ramdiff(a):
    """What one RAM map has that another doesn't, by allocation size"""
    m1, m2 = (json.load(open(os.path.join(RESULTS, "rammap-%s.json" % l))) for l in (a.a, a.b))
    for region in m2["regions"]:
        if region not in m1["regions"]:
            continue
        r1, r2 = m1["regions"][region], m2["regions"][region]
        c1, c2 = dict(map(tuple, r1["sizes"])), dict(map(tuple, r2["sizes"]))
        diffs = sorted(((s, c2.get(s, 0) - c1.get(s, 0)) for s in set(c1) | set(c2)), key=lambda x: -abs(x[0] * x[1]))
        print("== %s: %s -> %s: %+.1f KB in %+d allocations" % (region, a.a, a.b,
              (r2["allocated"] - r1["allocated"]) / 1024, r2["allocations"] - r1["allocations"]))
        for size, dc in diffs[:a.top]:
            if dc:
                print("   %7d B x %+4d = %+8.1f KB  %s" % (size, dc, size * dc / 1024, size_name(size)))
        print("   (sizes outside the top lists: %+.1f KB)" % ((r2["other_bytes"] - r1["other_bytes"]) / 1024))


def cmd_compare(a):
    s1, s2 = (json.load(open(p)) for p in (a.a, a.b))
    print("%-22s %14s %14s %9s" % ("", s1["label"][:14], s2["label"][:14], "change"))
    for key in ("load_avg", "load_p95", "load_max", "peak_max", "voices_max", "culls", "int_free_min"):
        x, y = s1[key], s2[key]
        ch = "%+.1f%%" % ((y - x) * 100.0 / x) if x else ""
        print("%-22s %14s %14s %9s" % (key, x, y, ch))
    for name in sorted(set(s1["kinds"]) | set(s2["kinds"])):
        x = s1["kinds"].get(name, {}).get("ns_per_voice_sample", 0)
        y = s2["kinds"].get(name, {}).get("ns_per_voice_sample", 0)
        ch = "%+.1f%%" % ((y - x) * 100.0 / x) if x and y else ""
        print("%-22s %14s %14s %9s" % (name + " ns", x, y, ch))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--port", help="part of the MIDI port name (default: deluge)")
    p.add_argument("--period", type=int, default=100, help="ms between readings (20-1000)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ports").set_defaults(fn=cmd_ports)
    sub.add_parser("watch").set_defaults(fn=cmd_watch)
    r = sub.add_parser("run")
    r.add_argument("--seconds", type=int, default=30)
    r.add_argument("--settle", type=float, default=2.0, help="seconds to wait before measuring")
    r.add_argument("--play", action="store_true", help="start the song first, stop it after")
    r.add_argument("--keep-playing", action="store_true")
    r.add_argument("--label", default="run")
    r.set_defaults(fn=cmd_run)
    s = sub.add_parser("sweep")
    s.add_argument("--channel", type=int, default=1, help="MIDI channel the sound follows (MIDI Follow or learned)")
    s.add_argument("--note", type=int, default=48)
    s.add_argument("--max", type=int, default=16)
    s.add_argument("--step-seconds", type=float, default=3.0)
    s.add_argument("--label", default="synth")
    s.set_defaults(fn=cmd_sweep)
    sn = sub.add_parser("snap")
    sn.add_argument("--label", required=True)
    sn.add_argument("--baseline", default="empty")
    sn.add_argument("--seconds", type=float, default=3.0)
    sn.set_defaults(fn=cmd_snap)
    lg = sub.add_parser("ledger")
    lg.add_argument("--baseline", default="empty")
    lg.set_defaults(fn=cmd_ledger)
    rm = sub.add_parser("rammap")
    rm.add_argument("--label", required=True)
    rm.add_argument("--regions", type=int, nargs="+", default=[1, 4, 2])
    rm.add_argument("--top", type=int, default=20)
    rm.set_defaults(fn=cmd_rammap)
    rd = sub.add_parser("ramdiff")
    rd.add_argument("a")
    rd.add_argument("b")
    rd.add_argument("--top", type=int, default=20)
    rd.set_defaults(fn=cmd_ramdiff)
    c = sub.add_parser("compare")
    c.add_argument("a")
    c.add_argument("b")
    c.set_defaults(fn=cmd_compare)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
