#!/usr/bin/env python3
"""Bring the Cycles and LXR preset kits up to eight preset rows, as every Bribes preset kit has from v1.40.

usage: add_perc_rows.py presets/KITS

Cycles kits (six rows) get row 7 CLAP on the clap engine and row 8 PERC2 on Cyc Perc, each a little different per kit.
LXR kits (seven rows) get row 8 PERC: the kit's own high tom voice a fifth up with a shorter decay, so it sits in the
kit it is in. A file that already has eight preset rows is left alone, so the tool can be run again.

By thisisbribery, GPL-3.0 as the firmware. The new rows are new sounds, not converted from anyone's kit.
"""
import re
import sys
from pathlib import Path

from lxr_to_deluge import cable, knob, lxr_t60, q31, release_for, user

NUM_ROWS = 8
CLAP_ENG, CYC_PERC = 12, 8  # dsp::drum_synth::Engine
kRowVolume = 40
kDrive = 100

# Per kit, by its place in the folder: clap Color, Shape, decay; perc semitones, Color, Shape, decay. Around the
# engines' own defaults (clap 24 25 46 37 decay 56, perc 15 38 100 64 decay 52; the perc
# rows are kept shorter than that, 0.3 to 1 s).
CLAP = [(12, 25, 56), (24, 35, 50), (36, 15, 62), (48, 45, 56), (30, 25, 46), (18, 40, 60), (42, 20, 52), (24, 55, 66),
        (54, 30, 56), (12, 35, 48), (36, 25, 58), (24, 45, 54), (48, 15, 64), (30, 40, 50), (18, 50, 60), (42, 30, 56)]
PERC = [(7, 15, 38, 34), (5, 25, 28, 30), (12, 7, 50, 37), (3, 35, 44, 32), (9, 20, 58, 29), (7, 45, 23, 36),
        (14, 15, 46, 31), (0, 30, 38, 40), (7, 10, 63, 34), (10, 40, 33, 26), (5, 25, 53, 35), (12, 15, 68, 39),
        (2, 50, 30, 30), (7, 20, 48, 32), (9, 35, 38, 37), (4, 5, 56, 29)]

NAMES = ['modulator1Amount', 'modulator2Amount', 'modulator1Feedback', 'modulator2Feedback', 'carrier1Feedback',
         'carrier2Feedback', 'mod1PitchAdjust', 'mod2PitchAdjust', 'oscAPulseWidth', 'oscAWavetablePosition',
         'oscBWavetablePosition']


def cyc_patch_bytes(engine):
    """As cycles_to_deluge.py: the KICK preset's LXR settings under a Cyc engine, Punch and Snappy off"""
    b = [0] * 26
    b[1:22] = [0, 45, 55, 20, 0, 30, 0, 76, 64, 0, 4, 64, 64, 0, 127, 0, 127, 0, 0, 60, 64]
    b[0] = engine
    b[25] = 1  # CONTROLS_VERSION
    return ''.join(f'{x:02X}' for x in b)


def cyc_row(name, engine, semis, macros, decay, t60):
    controls = [*macros, kDrive, 64, 64, 64, 64, decay, 0]
    params = {
        'oscAVolume': 2**31 - 1, 'oscBVolume': -2**31, 'noiseVolume': -2**31,
        'volume': user(kRowVolume), 'pan': 0,
        'lpfFrequency': 2**31 - 1, 'lpfResonance': -2**31, 'hpfFrequency': -2**31, 'hpfResonance': -2**31,
        'delayRate': 0, 'delayFeedback': -2**31, 'reverbAmount': -2**31,
    }
    params.update({n: knob(v) for n, v in zip(NAMES, controls)})
    attrs = '\n'.join(f'\t\t\t\t{k}="{q31(v)}"' for k, v in params.items())

    def env(tag, a, d, s, r):
        return (f'\t\t\t\t<{tag} attack="{q31(user(a))}" decay="{q31(user(d))}" sustain="{q31(user(s))}" '
                f'release="{q31(user(r))}" />')

    return f'''\t\t<sound
\t\t\tname="{name}"
\t\t\tpresetKit="2"
\t\t\tpolyphonic="auto"
\t\t\tvoicePriority="1">
\t\t\t<osc1 type="drumSynth" transpose="{semis}" cents="0"
\t\t\t\tdrumSynth="{cyc_patch_bytes(engine)}" />
\t\t\t<osc2 type="sine" transpose="0" cents="0" />
\t\t\t<defaultParams
{attrs}>
{env('envelope1', 0, 30, 50, release_for(t60))}
{env('envelope2', 0, 5, 0, 0)}
\t\t\t\t<patchCables>
\t\t\t\t\t<patchCable source="velocity" destination="volume" polarity="bipolar" amount="{q31(cable(50))}" />
\t\t\t\t\t<patchCable source="aftertouch" destination="volume" polarity="unipolar" amount="{q31(cable(33))}" />
\t\t\t\t\t<patchCable source="y" destination="lpfFrequency" polarity="bipolar" amount="{q31(cable(20))}" />
\t\t\t\t</patchCables>
\t\t\t</defaultParams>
\t\t</sound>
'''


SOUND = re.compile(r'\t\t<sound\n.*?\t\t</sound>\n', re.S)


def preset_rows(xml):
    return [m for m in SOUND.finditer(xml) if 'presetKit="' in m.group(0)]


def unique(name, xml):
    base, n = name, 2
    while f'name="{name}"' in xml:
        name, n = f'{base}{n}', n + 1
    return name


def insert_after(xml, match, rows):
    return xml[:match.end()] + rows + xml[match.end():]


def cycles(path, index, t60):
    xml = path.read_text()
    rows = preset_rows(xml)
    if len(rows) != 6:
        return False
    color, shape, decay = CLAP[index % len(CLAP)]
    clap = cyc_row(unique('CLAP', xml), CLAP_ENG, 0, (color, shape, 46, 37), decay, t60(7, (color, shape, 46, 37), decay, 0))
    semis, color, shape, decay = PERC[index % len(PERC)]
    perc = cyc_row(unique('PERC2', xml), CYC_PERC, semis, (color, shape, 100, 64), decay,
                   t60(3, (color, shape, 100, 64), decay, semis))
    path.write_text(insert_after(xml, rows[-1], clap + perc))
    return True


def knob_value(raw):
    """DrumControls::value: the 0-127 knob a stored param reads as"""
    return min(range(128), key=lambda v: abs(knob(v) - raw))


def signed(hexstr):
    v = int(hexstr, 16)
    return v - 2**32 if v >= 2**31 else v


def lxr(path):
    xml = path.read_text()
    rows = preset_rows(xml)
    if len(rows) != 7:
        return False
    tom = rows[5].group(0)  # KICK SNARE CH OH LTOM HTOM CYM
    assert 'name="HTOM' in tom, path

    perc = re.sub(r'name="[^"]*"', f'name="{unique("PERC", xml)}"', tom, count=1)
    semis = int(re.search(r'<osc1 type="drumSynth" transpose="(-?\d+)"', tom).group(1))
    perc = perc.replace(f'<osc1 type="drumSynth" transpose="{semis}"', f'<osc1 type="drumSynth" transpose="{semis + 7}"', 1)
    # The LXR voices' own decay (DrumControls::COMMON_DECAY): shorter, a tap not a tom
    old = re.search(r'oscAWavetablePosition="(0x[0-9A-F]{8})"', tom).group(1)
    decay = max(40, round(knob_value(signed(old)) * 0.8))
    perc = perc.replace(f'oscAWavetablePosition="{old}"', f'oscAWavetablePosition="{q31(knob(decay))}"', 1)
    perc = re.sub(r'(<envelope1 [^>]*release=")0x[0-9A-F]{8}"',
                  lambda m: f'{m.group(1)}{q31(user(release_for(lxr_t60(decay))))}"', perc, count=1)
    path.write_text(insert_after(xml, rows[-1], perc))
    return True


def cyc_t60(render):
    """The time a Cyc row takes to fall 60 dB, from the host renderer (cyc-engines host/cyc_render), or a safe guess"""
    import array, subprocess

    def t60(kind, macros, decay, semis):
        if render is None or not Path(render).exists():
            return 0.4
        raw = subprocess.run([render, str(kind), *map(str, macros), str(decay), '0', f'{60 + semis:.4f}', '44100', '3'],
                             env={'DRIVE': str(kDrive)}, capture_output=True, check=True).stdout
        x = array.array('i', raw)
        peak = max(abs(v) for v in x) or 1
        above = [i for i, v in enumerate(x) if abs(v) > peak * 0.001]
        return above[-1] / 44100
    return t60


def main():
    root = Path(sys.argv[1])
    render = sys.argv[2] if len(sys.argv) > 2 else None
    t60 = cyc_t60(render)
    done = 0
    for i, path in enumerate(sorted((root / 'CYCLES').glob('*.XML'))):
        done += cycles(path, i, t60)
    for path in sorted((root / 'LXR').glob('*.XML')):
        done += lxr(path)
    print('kits changed:', done)


if __name__ == '__main__':
    main()
