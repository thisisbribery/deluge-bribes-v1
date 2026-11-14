#!/usr/bin/env python3
"""Sort the synth presets on a Deluge SD card into the folders SHIFT + SYNTH browses.

usage: sort_synth_presets.py CARD [--dry-run]

CARD is the SD card (or a copy of it). Every synth preset in SYNTHS and its folders (except the type folders
SUBT, FM, WAVE, RING, BRINGS, DX7 and BROPHET) is COPIED to SYNTHS/<TYPE>/<CATEGORY>/:

  TYPE      SUBT (subtractive), WAVE (subtractive with a wavetable oscillator), FM, RING (ring mod)
  CATEGORY  BASS, LEAD, PAD or MISC

The category comes from the preset's name first (bass, pad, lead, pluck, bell...), then from its sound: low
transpose, slow attack, long release, mono or portamento, arpeggiator, samples. Nothing is moved or deleted, and a
preset already in its target folder is skipped, so it's safe to run again. Move any preset that lands in the wrong
category by hand. DX7 and drum synth presets are left where they are.
"""
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET

TYPE_FOLDERS = {"SUBT", "FM", "WAVE", "RING", "BRINGS", "DX7", "BROPHET"}


def value(el, name):
    if el is None:
        return None
    if name in el.attrib:
        return el.attrib[name]
    child = el.find(name)
    return child.text.strip() if child is not None and child.text else None


def knob(hex_value):
    """A stored param (hex) as the Deluge's 0 to 50 knob"""
    if hex_value is None:
        return 0
    v = int(hex_value, 16)
    if v >= 2**31:
        v -= 2**32
    return round((v + 2**31) / 2**32 * 50)


def read_sound(path):
    text = open(path, errors="replace").read()
    text = re.sub(r"<\?xml[^>]*\?>", "", text)
    root = ET.fromstring("<w>" + text + "</w>")
    return root.find("sound")


def classify(path):
    """(TYPE, CATEGORY), or None to leave the preset alone"""
    sound = read_sound(path)
    if sound is None:
        return None
    osc1, osc2 = sound.find("osc1"), sound.find("osc2")
    types = (value(osc1, "type"), value(osc2, "type"))
    if "dx7" in types or "drumSynth" in types:
        return None
    mode = value(sound, "mode") or "subtractive"
    kind = {"fm": "FM", "ringmod": "RING"}.get(mode, "WAVE" if "wavetable" in types else "SUBT")

    name = os.path.basename(path).lower()
    for word, category in (("bass", "BASS"), ("pad", "PAD"), ("lead", "LEAD"), ("pluck", "MISC"),
                           ("bell", "MISC"), ("flute", "LEAD"), ("recorder", "LEAD")):
        if word in name:
            return kind, category

    params = sound.find("defaultParams")
    env1 = params.find("envelope1") if params is not None else None
    attack, sustain, release = (knob(value(env1, k)) for k in ("attack", "sustain", "release"))
    transpose = int(value(sound, "transpose") or 0) + int(value(osc1, "transpose") or 0)
    mono = str(value(sound, "polyphonic")) in ("0", "mono", "legato")
    portamento = knob(value(params, "portamento"))
    arp = sound.find("arpeggiator")
    arp_mode = value(arp, "mode") if arp is not None else None

    if arp_mode not in (None, "off"):
        return kind, "MISC"
    if "sample" in types:
        return kind, "MISC"
    if transpose <= -12 and attack < 25:
        return kind, "BASS"
    if attack >= 25 and sustain >= 25:
        return kind, "PAD"
    if attack >= 10 and release >= 35 and sustain >= 30:
        return kind, "PAD"
    if (mono or portamento > 0) and attack < 25:
        return kind, "LEAD"
    if sustain >= 35 and attack < 25:
        return kind, "LEAD"
    return kind, "MISC"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry_run = "--dry-run" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    synths = os.path.join(args[0], "SYNTHS")
    if not os.path.isdir(synths):
        sys.exit(f"No SYNTHS folder in {args[0]}")

    copied = skipped = left = 0
    for folder, subfolders, files in os.walk(synths):
        if folder == synths:
            subfolders[:] = [d for d in subfolders if d.upper() not in TYPE_FOLDERS]
        subfolders[:] = [d for d in subfolders if not d.startswith(".")]
        for file in sorted(files):
            if file.startswith(".") or not file.upper().endswith(".XML"):
                continue
            path = os.path.join(folder, file)
            try:
                found = classify(path)
            except ET.ParseError as error:
                print(f"Can't read {path}: {error}", file=sys.stderr)
                found = None
            if found is None:
                left += 1
                continue
            target_folder = os.path.join(synths, *found)
            target = os.path.join(target_folder, file)
            if os.path.exists(target):
                skipped += 1
                continue
            print(f"{os.path.relpath(path, synths)} -> {found[0]}/{found[1]}")
            if not dry_run:
                os.makedirs(target_folder, exist_ok=True)
                shutil.copy2(path, target)
            copied += 1

    action = "Would copy" if dry_run else "Copied"
    print(f"{action} {copied}, already there {skipped}, left alone {left} (DX7, drum synth or unreadable)")


if __name__ == "__main__":
    main()
