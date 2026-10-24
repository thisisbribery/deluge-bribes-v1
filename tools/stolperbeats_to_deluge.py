#!/usr/bin/env python3
"""Converts Stolperbeats PatternBankNNN.txt files into kit pattern mode banks for the Deluge.

Each bank file becomes one bank folder, laid out the way kit pattern mode reads it:

    STUMBLE/<BANK>/<TRACK>/PATTERN001.XML ... PATTERN024.XML

<TRACK> is KICK, SNARE, HIHAT1, HIHAT2, PERC1 or PERC2. Copy the STUMBLE folder to PATTERNS/RHYTHMIC/ on the
Deluge's SD card. Bank folders can be renamed to anything, such as TECHNO or HOUSE.

Every note gets velocity 127 (the files hold hits only; --velocity changes it), and every pattern is repeated out to 4
bars (--bars changes it), so 1-bar hats and percs line up with the 4-bar kick and snare.

A PatternExtNNN.txt next to a bank file adds its ratchets: a step with 2, 3 or 4 hits becomes that many evenly spaced
notes inside the step. Pitch in the ext file is skipped, since a Deluge kit row has no pitch per note.

Usage:
    stolperbeats_to_deluge.py PatternBank000.txt [PatternBank001.txt ...] [-o OUT] [--name TECHNO]
                              [--velocity 127] [--bars 4]
"""

import argparse
import os
import re
import sys

TRACKS = ["KICK", "SNARE", "HIHAT1", "HIHAT2", "PERC1", "PERC2"]
NUM_SLOTS = 24
TICKS_PER_STEP = 24  # A 16th at the Deluge's default 96 ticks per quarter note
STEPS_PER_BAR = 16

LINE = re.compile(r"^\s*(KICK|SNARE|HIHAT1|HIHAT2|PERC1|PERC2)\s*>\s*PTN(\d+)\s*:\s*([01,\s]+);")
RATCHET_LINE = re.compile(r"^\s*(KICK|SNARE|HIHAT1|HIHAT2|PERC1|PERC2)\s*>\s*PTN(\d+)\s+RATCHET\s*:\s*([1-4,\s]+);")


def read_bank(path):
    """Returns {track: {slot: "0101..."}} with each pattern's bars joined."""
    bank = {track: {} for track in TRACKS}
    with open(path, encoding="ascii") as f:
        for line in f:
            match = LINE.match(line)
            if not match:
                continue
            track, slot, bars = match.group(1), int(match.group(2)), match.group(3)
            steps = "".join(bar.strip() for bar in bars.split(","))
            if slot < NUM_SLOTS and steps and len(steps) % 16 == 0:
                bank[track][slot] = steps
    return bank


def read_ratchets(path):
    """Returns {(track, slot): "1111211..."} from a PatternExtNNN.txt, or {} if there isn't one."""
    ratchets = {}
    if not path or not os.path.exists(path):
        return ratchets
    with open(path, encoding="ascii") as f:
        for line in f:
            match = RATCHET_LINE.match(line)
            if match:
                steps = "".join(bar.strip() for bar in match.group(3).split(","))
                ratchets[(match.group(1), int(match.group(2)))] = steps
    return ratchets


def ext_path_for(path):
    folder, name = os.path.split(path)
    ext_name = re.sub(r"PatternBank", "PatternExt", name, flags=re.IGNORECASE)
    if ext_name == name:
        return None
    # The module's card may use either case for the file name
    for candidate in os.listdir(folder or "."):
        if candidate.lower() == ext_name.lower():
            return os.path.join(folder, candidate)
    return None


def encode_note(pos, length, velocity):
    # Position, length, velocity, then lift 64, probability 20 (always), no iterance and no fill
    return f"{pos:08X}{length:08X}{velocity:02X}4014000000"


def repeat_to_bars(steps, bars):
    """Repeats a pattern until it's at least `bars` long, e.g. a 1-bar hat four times to match a 4-bar kick."""
    if not steps:
        return steps
    target = bars * STEPS_PER_BAR
    return (steps * -(-target // len(steps)))[: max(target, len(steps))]


def pattern_xml(steps, ratchets="", velocity=127):
    notes = []
    for i, step in enumerate(steps):
        if step != "1":
            continue
        hits = int(ratchets[i]) if i < len(ratchets) else 1
        length = TICKS_PER_STEP // hits
        notes += [encode_note(i * TICKS_PER_STEP + h * length, length, velocity) for h in range(hits)]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += "<pattern>\n  <attributes\n"
    xml += f'    patternVersion="0.0.1"\n    screenWidth="{len(steps) * TICKS_PER_STEP}"\n'
    xml += '    scaleType="1"\n    yNoteOfBottomRow="0"/>\n  <noteRows>\n'
    if notes:
        xml += f'    <noteRow\n      numNotes="{len(notes)}"\n      yNote="0"\n      yDisplay="0"\n'
        xml += f'      noteDataWithSplitProb="0x{"".join(notes)}" />\n'
    xml += "  </noteRows>\n</pattern>\n"
    return xml


def bank_name_for(path):
    # PatternBank000.txt is Bank 1 on the module
    match = re.search(r"PatternBank(\d+)", os.path.basename(path), re.IGNORECASE)
    return f"BANK{int(match.group(1)) + 1:03d}" if match else os.path.splitext(os.path.basename(path))[0].upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("banks", nargs="+", help="PatternBankNNN.txt files")
    parser.add_argument("-o", "--out", default="STUMBLE", help="output folder (default: STUMBLE)")
    parser.add_argument("--name", help="bank folder name, for a single bank file (e.g. TECHNO)")
    parser.add_argument("--velocity", type=int, default=127, help="velocity of every note, 1 to 127 (default: 127)")
    parser.add_argument("--bars", type=int, default=4, help="repeat shorter patterns out to this many bars (default: 4)")
    args = parser.parse_args()
    if not 1 <= args.velocity <= 127:
        sys.exit("--velocity must be 1 to 127")

    if args.name and len(args.banks) > 1:
        sys.exit("--name only works with one bank file")

    for path in args.banks:
        bank = read_bank(path)
        ratchets = read_ratchets(ext_path_for(path))
        name = (args.name or bank_name_for(path)).upper()
        written = 0
        for track in TRACKS:
            folder = os.path.join(args.out, name, track)
            os.makedirs(folder, exist_ok=True)
            for slot, steps in sorted(bank[track].items()):
                ratchet = ratchets.get((track, slot), "")
                if ratchet:
                    ratchet = repeat_to_bars(ratchet.ljust(len(steps), "1"), args.bars)
                with open(os.path.join(folder, f"PATTERN{slot + 1:03d}.XML"), "w", newline="\n") as f:
                    f.write(pattern_xml(repeat_to_bars(steps, args.bars), ratchet, args.velocity))
                written += 1
        extra = f", {len(ratchets)} with ratchets" if ratchets else ""
        print(f"{path} -> {os.path.join(args.out, name)} ({written} patterns{extra})")


if __name__ == "__main__":
    main()
