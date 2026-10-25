#!/usr/bin/env python3
"""Turn LXR-02 kits (.SND files) into Deluge LXR preset kits on the drum synth's LXR voices.

usage: lxr_to_deluge.py SND_DIR OUTDIR [first last]
Writes OUTDIR/<name>.XML, one seven-row kit per .SND, rows as SHIFT + KIT > LXR lays them out (bottom first):
KICK (drum 1), SNARE, CH (hat, closed decay), OH (hat, open decay), LTOM (drum 2), HTOM (drum 3), CYM.

A .SND file is the kit name (8 bytes) then one byte per LXR-02 sound parameter, in the order of the firmware's
ParamEnums (lxr02_params.json). The drum synth's LXR voices are a port of the LXR-02's, so most settings go across
as they are. The rest are conversions, as close as the Deluge allows:
- Pitch: the LXR-02's coarse is an absolute MIDI note and kit rows play at middle C, so transpose = coarse - 60, fine
  in cents. Its mod oscillators' frequencies are absolute notes too; ours are semitones above the main osc.
- Amp envelope: the LXR-02's linear decay through its slope curve becomes the voice's own decay (COMMON_DECAY),
  matched where it is 20 dB down. The Deluge envelope is open (sustain full) with a release long enough to let it
  ring out, as on every drum row.
- Voice filters (drums, hats, cymbal) become the Deluge's low or high pass; the snare's filter is its own noise filter.
- Drive and distortion go to the voice's drive, scaled down (ours is a different curve). Volume and pan go across.
- Not carried over: LFOs, velocity modulation, decimation, the LXR's FX.
"""
import json, math, sys
from pathlib import Path

P = json.load(open(Path(__file__).with_name('lxr02_params.json')))
NAMES = ['modulator1Amount', 'modulator2Amount', 'modulator1Feedback', 'modulator2Feedback', 'carrier1Feedback',
         'carrier2Feedback', 'mod1PitchAdjust', 'mod2PitchAdjust', 'oscAPulseWidth', 'oscAWavetablePosition',
         'oscBWavetablePosition']
kRowVolume = 40       # the Deluge's default sound volume, user value, at LXR volume 127
kDriveScale = 0.6     # LXR drive / distortion to the drum synth's drive
kMaxResonance = 20    # Deluge filter resonance (0-50) at LXR resonance 127

RELEASE_TABLE = [1959518848, 240577040, 126456408, 84972672, 63518640, 50408868, 41567836, 35202512, 30400724,
                 26649400, 23637820, 21166812, 19102814, 17352918, 15850494, 14546511, 13404089, 12394955, 11497068,
                 10692993, 9968758, 9313033, 8716538, 8171592, 7671792, 7211749, 6786901, 6393359, 6027784, 5687299,
                 5369406, 5071928, 4792960, 4530827, 4284050, 4051316, 3831462, 3623446, 3426337, 3239300, 3061582,
                 2892503, 2731448, 2577859, 2431229, 2291096, 2157036, 2028664, 1905625, 1787593, 1674270, 1565377,
                 1460662, 1359888, 1262836, 1169305, 1079105, 992062, 908014, 826807, 748301, 672363, 598870, 527703,
                 458757]


def q31(v): return f'0x{int(v) & 0xFFFFFFFF:08X}'
def user(u): return int(u) * 85899345 - 2147483648
def cable(u): return int(u) * 21474836
def clamp(v, lo, hi): return max(lo, min(hi, int(round(v))))


def knob(v):
    """DrumControls::fromValue"""
    d = (int(v) << 8) - 0x4000
    den = 0x4000 if d < 0 else 0x3F00
    raw = abs(d << 31) // den * (1 if d >= 0 else -1)
    return max(-2**31, min(2**31 - 1, raw))


def release_seconds(u):
    """As drum_synth.cpp releaseSeconds()"""
    p = (u * 85899345 - 2**31) >> 2
    i = (p >> 24) + 32
    fr = ((p << 7) & 0x7FFFFFFF) / 2**31
    r = RELEASE_TABLE[0] if i < 0 else RELEASE_TABLE[64] if i >= 64 else RELEASE_TABLE[i] * (1 - fr) + RELEASE_TABLE[i + 1] * fr
    return 2**23 / max((140 << 9) * r / 2**32, 1) / 44100


def release_for(t60):
    """As drum_synth.cpp envelopeReleaseFor()"""
    if t60 >= 1000: return 40
    for r in range(40, 50):
        if release_seconds(r) >= 5 * t60: return r
    return 50


def lxr_t60(knob_value):
    return 1000.0 if knob_value >= 127 else 0.03 * 400 ** (knob_value / 126)


def decay_knob(decay, slope):
    """LXR-02 amp decay (0-127) and slope to the drum synth's own decay knob, matched at -20 dB"""
    K = 2 * 0.999 / (1 - 0.999)
    v = decay / 127
    step = min(1.0, (1 - (1 + K) * v / (1 + K * v)) * 2)  # slopeEg2_calcTime(), per 64-sample block
    if step <= 0: return 127
    t_end = 64 / (44100 * step)
    a = (slope / 127 - 0.5) * 1.999
    s = 2 * a / (1 - a)
    x20 = 0.1 / (1 + s - s * 0.1)  # where slopeEg2_calcSlopeValue() is 0.1
    t20 = t_end * (1 - x20)
    t60 = 3 * t20  # an exponential is 20 dB down a third of the way to 60
    return clamp(126 * math.log(max(t60, 0.03) / 0.03) / math.log(400), 0, 126)


def cutoff_hz(value):
    """LXR-02 filter frequency: valueShaperF2F(v, FILTER_SHAPER) through SVF_directSetFilterValue()"""
    k = 2 * -0.9 / (1.0001 + 0.9)
    x = value / 127
    return (1 + k) * x / (1 + k * abs(x)) * 0.45 * 44100


def deluge_filter_user(hz):
    """Deluge LPF / HPF frequency user value (0-50) for a cutoff, about 0.224 octaves a step from 20 kHz at 50"""
    return clamp(50 + math.log2(max(hz, 20) / 20000) / 0.224, 0, 50)


def noise_cutoff(hz):
    """The drum synth's snare noise filter: 30 Hz to 16 kHz across 0-127"""
    return clamp(127 * math.log(max(hz, 30) / 30) / math.log(16000 / 30), 0, 127)


def wave(v): return min(int(v), 3) if int(v) != 4 else 4  # SINE TRI SAW REC NOISE (PWM -> square)


def rel_semis(note, base): return clamp(64 + note - base, 0, 127)


ROWS = [  # name, engine (0 drum, 1 snare, 2 metal), LXR voice (1-6), decay parameter, choke
    ('KICK', 0, 1, 'PAR_VELOD1', False), ('SNARE', 1, 4, 'PAR_VELOD4', False), ('CH', 2, 6, 'PAR_VELOD6_CLOSED', True),
    ('OH', 2, 6, 'PAR_VELOD6_OPEN', True), ('LTOM', 0, 2, 'PAR_VELOD2', False), ('HTOM', 0, 3, 'PAR_VELOD3', False),
    ('CYM', 2, 5, 'PAR_VELOD5', False)]


def row(g, name, engine, n, decay_param):
    coarse, fine = g(f'PAR_COARSE{n}'), g(f'PAR_FINE{n}')
    semis_f = coarse - 60 + (fine / 127 - 0.5) * 2
    semis = int(round(semis_f))
    cents = clamp((semis_f - semis) * 100, -50, 50)

    b = [0] * 26
    b[0] = engine
    b[2:5] = [64, 64, 64]
    b[8:10] = [64, 64]; b[12:14] = [64, 64]
    b[15], b[17] = 127, 127
    b[19], b[20], b[21] = g(f'PAR_TRANS{n}_WAVE'), g(f'PAR_TRANS{n}_VOL'), g(f'PAR_TRANS{n}_FREQ')
    if engine == 0:
        b[1] = wave(g(f'PAR_OSC_WAVE_DRUM{n}'))
        b[2], b[3], b[4] = g(f'PAR_MODAMNT{n}'), g(f'PAR_MOD_EG{n}'), g(f'PAR_PITCH_SLOPE{n}')
        b[5] = 1 if g(f'PAR_MIX_MOD_{n}') else 0
        b[6], b[7] = g(f'PAR_FMAMNT{n}'), wave(g(f'PAR_MOD_WAVE_DRUM{n}'))
        b[8] = rel_semis(g(f'PAR_FM_FREQ{n}'), coarse)
        drive = g(f'PAR_DRIVE{n}')
    elif engine == 1:
        b[1] = wave(g('PAR_OSC_WAVE_SNARE'))
        b[2], b[3], b[4] = g('PAR_MODAMNT4'), g('PAR_MOD_EG4'), g('PAR_PITCH_SLOPE4')
        b[14], b[15] = g('PAR_MIX1'), g('PAR_NOISE_FREQ1')
        ftype = g('PAR_FILTER_TYPE_4')  # 0 LP, 1 HP, 2 BP, ... (the firmware adds 1)
        b[16] = {0: 0, 1: 1, 2: 2, 3: 2, 6: 0}.get(ftype, 3)
        b[17] = noise_cutoff(cutoff_hz(g('PAR_FILTER_FREQ_4')))
        b[18] = g('PAR_RESO_4')
        drive = g('PAR_SNARE_DISTORTION')
    else:
        cym = n == 5
        sfx = '_CYM' if cym else '_HH'
        b[1], b[7], b[11] = (wave(g(f'PAR_WAVE{i}{sfx}')) for i in (1, 2, 3))
        b[6] = g('PAR_MOD_OSC_GAIN1_CYM' if cym else 'PAR_MOD_OSC_GAIN1')
        b[10] = g('PAR_MOD_OSC_GAIN2_CYM' if cym else 'PAR_MOD_OSC_GAIN2')
        b[8] = rel_semis(g('PAR_MOD_OSC_F1_CYM' if cym else 'PAR_MOD_OSC_F1'), coarse)
        b[12] = rel_semis(g('PAR_MOD_OSC_F2_CYM' if cym else 'PAR_MOD_OSC_F2'), coarse)
        drive = g('PAR_CYMBAL_DISTORTION' if cym else 'PAR_HAT_DISTORTION')
    b[19] = min(b[19], 13)
    b[25] = 1  # CONTROLS_VERSION

    dk = decay_knob(g(decay_param), g(f'PAR_VOL_SLOPE{n}'))
    drv = clamp(drive * kDriveScale, 0, 127)
    # The continuous settings live on Deluge params (lxrControlSlot()); the patch bytes keep a copy
    if engine == 2:
        slots = [b[10], b[12], b[13], b[6], b[8], b[9], b[20], b[21], 64, dk, drv]
    else:
        slots = [b[2], b[3], b[4], b[14] if engine == 1 else b[6], b[15] if engine == 1 else b[8],
                 b[17] if engine == 1 else b[9], b[20], b[21], b[18] if engine == 1 else 64, dk, drv]

    lpf, hpf, res = 50, 0, 0
    if engine != 1:
        ftype, fr = g(f'PAR_FILTER_TYPE_{n}'), cutoff_hz(g(f'PAR_FILTER_FREQ_{n}'))
        res = clamp(g(f'PAR_RESO_{n}') / 127 * kMaxResonance, 0, 50)
        if ftype in (0, 6): lpf = deluge_filter_user(fr)
        elif ftype == 1: hpf = deluge_filter_user(fr)
        elif ftype in (2, 3): lpf, hpf = deluge_filter_user(fr * 2), deluge_filter_user(fr / 2)
        else: res = 0
    rel = release_for(lxr_t60(dk))

    params = {
        'oscAVolume': 2**31 - 1, 'oscBVolume': -2**31, 'noiseVolume': -2**31,
        'volume': user(round(kRowVolume * g(f'PAR_VOL{n}') / 127)),
        'pan': max(-2**31, min(2**31 - 1, (g(f'PAR_PAN{n}') - 64) * 2**25)),
        'lpfFrequency': 2**31 - 1 if lpf >= 50 else user(lpf),
        'lpfResonance': user(res) if lpf < 50 else -2**31,
        'hpfFrequency': -2**31 if hpf <= 0 else user(hpf),
        'hpfResonance': user(res) if hpf > 0 else -2**31,
        'delayRate': 0, 'delayFeedback': -2**31, 'reverbAmount': -2**31,
    }
    params.update({k: knob(v) for k, v in zip(NAMES, slots)})
    attrs = '\n'.join(f'\t\t\t\t{k}="{q31(v)}"' for k, v in params.items())
    return attrs, ''.join(f'{x:02X}' for x in b), semis, cents, rel


def kit_xml(path):
    raw = Path(path).read_bytes()
    kitname = raw[:8].decode('latin1').strip() or Path(path).stem
    v = raw[8:]
    g = lambda k: v[P[k]] if P[k] < len(v) else 0
    sounds = []
    for name, engine, n, dp, choke in ROWS:
        attrs, hexb, semis, cents, rel = row(g, name, engine, n, dp)
        sounds.append(f'''\t\t<sound
\t\t\tname="{name}"
\t\t\tpresetKit="1"
\t\t\tpolyphonic="{'choke' if choke else 'auto'}"
\t\t\tvoicePriority="1">
\t\t\t<osc1 type="drumSynth" transpose="{semis}" cents="{cents}"
\t\t\t\tdrumSynth="{hexb}" />
\t\t\t<osc2 type="sine" transpose="0" cents="0" />
\t\t\t<defaultParams
{attrs}>
\t\t\t\t<envelope1 attack="{q31(user(0))}" decay="{q31(user(30))}" sustain="{q31(user(50))}" release="{q31(user(rel))}" />
\t\t\t\t<envelope2 attack="{q31(user(0))}" decay="{q31(user(5))}" sustain="{q31(user(0))}" release="{q31(user(0))}" />
\t\t\t\t<patchCables>
\t\t\t\t\t<patchCable source="velocity" destination="volume" polarity="bipolar" amount="{q31(cable(50))}" />
\t\t\t\t\t<patchCable source="aftertouch" destination="volume" polarity="unipolar" amount="{q31(cable(33))}" />
\t\t\t\t\t<patchCable source="y" destination="lpfFrequency" polarity="bipolar" amount="{q31(cable(20))}" />
\t\t\t\t</patchCables>
\t\t\t</defaultParams>
\t\t</sound>''')
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<kit
\tfirmwareVersion="c1.3.0"
\tearliestCompatibleFirmware="4.1.0-alpha">
\t<defaultParams
\t\treverbAmount="0x80000000"
\t\tvolume="0x00000000"
\t\tpan="0x00000000"
\t\tmodFXDepth="0x00000000"
\t\tmodFXRate="0xE0000000">
\t\t<delay rate="0x00000000" feedback="0x80000000" />
\t\t<lpf frequency="0x7FFFFFFF" resonance="0x80000000" />
\t\t<hpf frequency="0x80000000" resonance="0x80000000" />
\t</defaultParams>
\t<soundSources>
''' + '\n'.join(sounds) + '''
\t</soundSources>
</kit>
'''
    return kitname, xml


if __name__ == '__main__':
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    first, last = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (0, 999)
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted(src.glob('*.SND')):
        num = int(f.name.split('-')[0])
        if not first <= num <= last: continue
        kitname, xml = kit_xml(f)
        dest = out / f'{num:02d} {kitname.upper()}.XML'
        dest.write_text(xml)
        print(dest.name)
