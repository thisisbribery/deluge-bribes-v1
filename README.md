<a id="readme-top"></a>

# BRIBELUGE: Deluge Bribes FW v1.49

> **Contributing and beta testing:** anyone is welcome to contribute and beta test. Please send bug reports and feature requests through the [Issues](https://github.com/thisisbribery/deluge-bribes-v1/issues) tab, and code changes through [Pull requests](https://github.com/thisisbribery/deluge-bribes-v1/pulls). Fair warning: I'm not overly responsive, and this won't turn into a wild free-for-all feature set. It's designed to be a contained set of instruments. Open to input though! This repo is for Bribeluge only: to contribute to the Deluge firmware itself, go to the [community firmware](https://github.com/SynthstromAudible/DelugeFirmware) ([delugecommunity.com](https://delugecommunity.com/)).

Bribeluge is an unofficial modified firmware for the Synthstrom Deluge, rebased on the latest official community firmware release (CFW v1.3.0, Derbyshire) from [delugecommunity.com](https://delugecommunity.com/), with thanks to [everyone who has contributed to it](https://github.com/SynthstromAudible/DelugeFirmware/graphs/contributors).

I build Bribeluge for those who want more wonk, more destruction options, more speed, and a "studio in a box" mentality. I could not have done any of this without the incredible work of the original Deluge creators, Rohan Hill and [Synthstrom Audible](https://synthstrom.com/), and the tireless work of the community firmware team ever since the Deluge was open sourced.

**Built on the community firmware:** Bribeluge is a set of additions. The firmware underneath is the work of Rohan Hill and Synthstrom Audible, who made the Deluge and open sourced its firmware, and of the volunteers who have built the [Deluge Community Firmware](https://delugecommunity.com/) since. Anything Bribeluge does that isn't in the numbered list below is theirs, not mine: see the community firmware's own [feature list](https://github.com/SynthstromAudible/DelugeFirmware/blob/v1.3.0/docs/community_features.md). More in [Design and credit](#design-and-credit).

**Source code (GPL-3.0):** the complete source, with the community firmware's full history and contributors, is at [thisisbribery/DelugeFirmware](https://github.com/thisisbribery/DelugeFirmware), a fork of the community firmware. This release is tag [`bribes-v1.49`](https://github.com/thisisbribery/DelugeFirmware/tree/bribes-v1.49), the exact commit the bin was built from, and a full source download on the [v1.49 release](https://github.com/thisisbribery/deluge-bribes-v1/releases/tag/v1.49). See [Source code](#source-code).

What Bribeluge adds:

1. **[Stumble swing](#1-stumble-swing):** Four extra swing styles (HOPP, DEEP, SQEZ, FOLD), seven levels each, on SHIFT + TEMPO. New songs start on Stumble SQEZ.
2. **[Kit pattern mode](#2-kit-pattern-mode):** 24 saved patterns for each of a kit's bottom six rows. Step a row through them or load a whole bank.
3. **[Autofill](#3-autofill):** TAP plays a fill to the end of the bar: Ghost, Drive, Build, Climb or Stutter.
4. **[Mono sequencer](#4-mono-sequencer):** A bassline step sequencer for synth, MIDI and CV tracks: octave per note, slide steps, gate control and a voltage per row on CV.
5. **[Endless Record](#5-endless-record):** RECORD while playing keeps recording past the end of the loop. RECORD again stops at the next bar.
6. **[Drum synth](#6-drum-synth):** Synthesised drums on any kit row: LXR voices, DXIA, DIIA, eight Cyc engines, GIN, the ULTRAKIK kick and TRIBE. One pad layout, Cycles-style gold knobs, eight-row preset kits on SHIFT + KIT that swap for each other in place and keep any rows you add above or below, and ULTRAKIK or XIA onto a single row from the same menu.
7. **[Saturation](#7-saturation):** A one-knob drive that gets louder and denser all the way to a hard clip, with five curves. Learnable to a gold knob.
8. **[Sample start offset](#8-sample-start-offset):** Move where a sample starts, per step: draw it, lock it, modulate it.
9. **[303 synth](#9-303-synth):** A TB-303 voice from Open303 with accent and slide from the mono sequencer, three filters (303, LP18, DIRT) and an overdrive after them.
10. **[Delay feedback and tone](#10-delay-feedback-and-tone):** Delay amount and feedback on separate controls, plus a DJ filter in the loop, one SHIFT layer down.
11. **[Affect all](#11-affect-all):** SHIFT + AFFECT ENTIRE snapshots any kit: every knob moves all its sound rows (drum synths, samples and synths), and it snaps back on the next bar.
12. **[Pad Guides](#12-pad-guides):** SHIFT makes a drum synth's setting pads pulse pink (purple on BRINGS, BROPHET and BRUNO106), with the Shortcut Overlay on or off, gold knob buttons flash theirs, shortcut pads blink their gold knob's button, and a held shortcut pad scrolls its name on the 7-segment display.
13. **[Synth browser](#13-synth-browser):** SHIFT + SYNTH: pick a type (SUBT, FM, WAVE, RING, BRINGS, DX7, BROPHET, BRUNO106, 303, INIT), then a category, then play through the presets. The audition pads play each type's init synth (or your own patch) the whole way. 99 wavetable, 288 DX7, 37 BRINGS, 536 BROPHET and 212 BRUNO106 presets included.
14. **[Instrument Picker](#14-instrument-picker):** The kit and synth type every new track starts as, on its top preset.
15. **[Gate out](#15-gate-out):** A kit's bottom four rows fire the four gate outputs. GATE and MIDI out sit at the top of each row's menu.
16. **[MIDI kits](#16-midi-kits):** SHIFT + MIDI makes an MKIT: sixteen MIDI rows that kit patterns and Autofill can play.
17. **[CV2 lock](#17-cv2-lock):** CV 2 follows the gold knobs in semitones, lockable per step.
18. **[Elektron P-locks](#18-elektron-p-locks):** Optional: a parameter lock stays on its own step and goes with its note.
19. **[Track types in song view](#19-track-types-in-song-view):** Section pads move by track type: kits flash, synths breathe, MIDI pings, CV stays solid.
20. **[MIDI loop tracks](#20-midi-loop-tracks):** LOOP tracks and ECHO turn the Deluge into a MIDI looper for synths with their local control on.
21. **[BRIBERING MODE](#21-bribering-mode):** A resonator synth engine after Mutable Instruments Rings: five models, and Bow to keep it sounding. On synths and kit rows.
22. **[Feedback](#22-feedback):** Feeds each synth voice's filter output back into its input: thicker, driven low end, and self-oscillation from patch cables.
23. **[Crush types](#23-crush-types):** Bitcrush and Decimation that sound like real low bit depths and sample rates: Hard, Vintage, u-Law and Jitter, and Decay (a dying BBD chip), plus the original.
24. **[BROPHET](#24-brophet):** A two-oscillator poly synth engine from Pro-54, the open source port of NI's Pro-53: sync, poly mod, analog drift, its filter in every LPF list, and all 512 Pro-53 programs.
25. **[Pan spread](#25-pan-spread):** Each note of a poly synth gets its own place in the stereo field, like a poly synth's voice pan spread, no unison needed.
26. **[BRUNO106](#26-bruno106):** A Juno-style poly synth engine from Ultramaster KR-106: one DCO with saw, pulse, sub and noise, its IR3109 filter in every LPF list, the four position HPF with bass boost, and BRUNO CHORUS as a Mod FX type on any track.
27. **[BRIBELUGE COMPANION](#27-bribeluge-companion):** A phone or tablet screen for the Deluge over USB: the display spelled out in full, engine drawings, every knob it shows turnable from the screen and following the Deluge (main settings, engine controls, switches and gold knobs), waveforms with draggable markers, picture pickers, a song view you can tap, the Deluge's menus whole page by touch, and a hardware-style panel for every engine: BRUNO106 (Juno-style sliders), BROPHET (Prophet-style knobs), wavetable synths (a 3D view of the table with every note moving through it), every other synth and drum engine, and the Deluge's own SUBTRACTIVE, FM and RINGMOD, all working both ways.
28. **[Master clip](#28-master-clip):** A clipper or limiter at the very end of the song: five curves and a lookahead limiter, with drive and a ceiling, so the output never hits the Deluge's harsh digital clip.
29. **[SHIFT](#29-shift):** A three-band frequency shifter as a Mod FX type on any track: each band moves by its own number of hertz, so harmonics stop lining up. Feedback shifts it again on every pass.
30. **[TRIBE](#30-tribe):** An 808 / 909 drum machine: eight voices, each with an 808 > 909 knob that blends smoothly from one machine to the other, every knob centred on the real machine, extras after Hexinverter's Mutant drums, and eleven kits. Never more CPU than the Cyc engines.
31. **[Scrolling 7SEG text](#31-scrolling-7seg-text):** An option for 7-segment Deluges: every menu name and option flashes its four letter name, then scrolls its full name when there's more to say.
32. **[Kit mixer](#32-kit-mixer):** A level fader for every kit row: hold **LEVEL/PAN** and press **KEYBOARD**, and each row's pads show and set its level. The same again brings the steps back, untouched.
33. **[Engine panels](#33-engine-panels):** The companion gets a hardware-style panel for every Bribeluge engine and the Deluge's own synth modes. Drum machines: TRIBE as an 808 on the left and a 909 on the right with MORPH on the seam, CYC in bone and grey, LXR in black with pink LED rings, GIN in machined gunmetal with a scope of its sound. Drum voices: ULTRAKIK as a kick drum shell, XIA as silver modules. Synths: BRIBERING with its resonator, the 303, DX7 with its screen and six operators, and SUBTRACTIVE, FM and RINGMOD, next to BRUNO106, BROPHET and WAVE. Both ways, with a key per kit row to pick the voice and hear it. Touch any panel control and the Deluge lights the gold knobs that turn it, or opens its setting with **SHORTCUT**.

**On the web:** [feature overview](https://www.thisisbribery.com/bribeluge/) and this [manual](https://www.thisisbribery.com/bribeluge/manual/) at thisisbribery.com.

**Support:** find it useful? [Buy me a coffee on Ko-fi](https://ko-fi.com/thisisbribery).

**Start here:** [Download](#download) · [Install](#install) · **Reference:** [Quick reference](#quick-reference) · [About](#about) · [Changelog](#changelog) · [Design and credit](#design-and-credit) · [Source code](#source-code)

Names in **bold capitals** in brackets are what the 7-segment display shows.

## Download

**Everything in one zip:** the firmware, every preset below and the steps for putting them on the SD card download together from [thisisbribery.com/bribeluge](https://www.thisisbribery.com/bribeluge/#download). The files here are the same ones, piece by piece.

[`firmware/deluge-bribes-v1.49.bin`](firmware/deluge-bribes-v1.49.bin)

SHA-256: `d806690d75549de751fc9e32e123b8ae105d52532382c0bdd08da240329e6ab1`

Presets (optional), copied to the same place on the SD card:

- [`presets/KITS/CYCLES`](presets/KITS/CYCLES) and [`presets/KITS/LXR`](presets/KITS/LXR) to `KITS/CYCLES` and `KITS/LXR` (42 LXR kits). The GIN and TRIBE kits are built into the firmware.
- [`presets/SYNTHS/WAVE`](presets/SYNTHS/WAVE) to `SYNTHS/WAVE`. These play the free **BVKER Custom Wavetables** pack, which isn't included here: download it from [bvker.com/free-serum-wavetables](https://bvker.com/free-serum-wavetables/) and unzip it into `SAMPLES/WAVETABLES`, so the card has `SAMPLES/WAVETABLES/BVKER - Custom Wavetables/Analog` and the other folders. From v1.33 the WAVE presets are a new set with new names: delete the old ones from `SYNTHS/WAVE` first. From v1.36 their **CUSTOM 3** sets LFO 1's sweep of the wavetable position (it was Feedback): copy them over the old ones.
- [`presets/SYNTHS/DX7`](presets/SYNTHS/DX7) to `SYNTHS/DX7`: 288 DX7 voices in `LEAD`, `BASS`, `PAD`, `KEYS`, `BELL` and `MISC`. From v1.36, 9 of them that played off C are retuned: copy them over the old ones.
- [`presets/SYNTHS/BRINGS`](presets/SYNTHS/BRINGS) to `SYNTHS/BRINGS`. If your card has `SYNTHS/BRIB` from v1.26, rename it to `BRINGS`.
- [`presets/SYNTHS/BROPHET`](presets/SYNTHS/BROPHET) to `SYNTHS/BROPHET`: Pro-53's 512 programs in `BNK1` to `BNK8`, and 24 Bribes presets in `BRIB`. From v1.36, 128 programs that played off C are retuned: copy them over the old ones.
- [`presets/SYNTHS/BRUNO106`](presets/SYNTHS/BRUNO106) to `SYNTHS/BRUNO106`: 212 presets in `LEAD`, `BASS`, `PAD` and `MISC`.
- Your own synth presets: [`tools/sort_synth_presets.py`](tools/sort_synth_presets.py) copies them into the synth browser's folders (see [Synth browser](#13-synth-browser)).

[Back to top](#readme-top)

## Install

1. Copy `deluge-bribes-v1.49.bin` to the top level of the Deluge's SD card. Remove any other `.bin` files from the top level.
2. Turn the Deluge off.
3. Hold **SHIFT** and switch the Deluge on. Let go once it starts loading the new firmware.

To go back, install an official firmware file the same way.

**Status: experimental.** Made on a 7-segment Deluge; the OLED screens haven't been checked on hardware. Back up your SD card before installing.

With the new settings left at their defaults, the Deluge behaves like the community firmware, except that new songs start on Stumble swing (straight until you turn the swing up), the delay's feedback has its own setting (the tone starts flat), and song view's section pads move by track type. Songs saved before keep their own swing and sound the same through the delay.

[Back to top](#readme-top)

## 1. Stumble swing

The Deluge's own swing pushes every second 16th later by one amount. Stumble swing replaces it with four styles that move the notes in different shapes, each with seven levels.

### Turning it on

New songs start with Stumble on, style SQEZ, level 0 (straight): turn the swing up with **SHIFT + turn TEMPO** to hear it. Songs saved before v1.8 keep the swing they were saved with. To change it:

1. Press **SONG**, then press the **SELECT** knob to open the Song menu.
2. Turn to **Stumble** (**STUM**) and press **SELECT** to switch it on or off.
3. Turn to **Stumble Style** (**STYL**), press **SELECT** and choose a style. It changes in real time, so you can hear the difference while playing.
4. Set the level with **SHIFT + turn TEMPO**, from 0 (straight) to 6 (strongest).

Switch **Stumble** off to go back to the Deluge's own swing. Each mode keeps its own setting, so switching back and forth doesn't change your Classic amount or your Stumble style and level. Both are saved with the song.

### The four styles

Every style repeats each beat (HOPP every pair of 16ths), and none of them moves the downbeat.

| Style | What it does |
|---|---|
| **HOPP** | MPC and Linn style 16th swing in whole ticks. The second 16th of each pair lands at 54.2, 56.3, 58.3, 62.5, 66.7 or 70.8%. |
| **DEEP** | Swing at two levels: each beat's 8ths swing (52 to 66.7%), then each 8th's two 16ths swing again inside it (52 to 60%). |
| **SQEZ** | The "e" leans late, then the "&" and "a" squeeze up against the next downbeat. |
| **FOLD** | The "e" moves late and the "a" moves early, folding in toward the "&". The 8th pulse holds while the 16ths pinch together. |

### Shortcuts on the TEMPO knob

- **SHIFT + turn TEMPO** sets the swing amount (Classic) or level (Stumble).
- **SHIFT + push and turn TEMPO** steps through HOPP, DEEP, SQEZ and FOLD while Stumble is on. The first click shows the current style. With Stumble off, it shows **CLAS** and changes nothing; Stumble is switched on and off in the Song menu.
- **The display stays up while you hold SHIFT,** so you can turn, listen and turn again. It goes when you let go of SHIFT.
- **SHIFT + click TEMPO** (without turning) still clears tempo automation. It now happens when you let go of the knob, so changing styles never clears it by accident.
- **Swing Interval** (hold **TAP** and turn **TEMPO**, or the Song menu) still works. At 16ths the styles play as described. At 8ths every pattern stretches to twice the length.

[Back to top](#readme-top)

## 2. Kit pattern mode

A pattern store for kits, after the Stolperbeats module's pattern banks. Each of a kit's bottom six rows can step through 24 saved patterns, and you can load whole banks of them at once.

### Setting it up

1. **SHIFT + press SELECT** to open Settings, then go to **Community Features** (**FEAT**).
2. Set **Sync Scaling Action** (**SCAL**) to **Kit pattern mode** (**PATT**). This takes over the SYNC SCALING button.
3. Put your banks on the SD card:

```
PATTERNS/RHYTHMIC/STUMBLE/<BANK>/<ROW>/PATTERN001.XML ... PATTERN024.XML
```

A bank is any folder you name, such as `TECHNO` or `HOUSE`. `<ROW>` is `KICK`, `SNARE`, `HIHAT1`, `HIHAT2`, `PERC1` or `PERC2`. These are standard Deluge pattern files, so they can be copied, renamed and shared.

### Using it

In a kit clip:

1. Press **SYNC SCALING**. Its LED flashes while kit pattern mode is on.
2. Turn **SELECT** to pick a bank, then press **SELECT** to load it into all six rows. Each row keeps its pattern number when you change bank.
3. Hold a row's audition pad and turn **SELECT** to step that row through patterns 1 to 24. The display shows e.g. **BD05** (Kick, pattern 5). An empty slot gives an empty row.
4. Edit notes freely, as normal.
5. Hold a row's audition pad and press **SAVE**. The normal save screen opens on that row's slot. Press **SAVE** to confirm and overwrite.
6. Press **SYNC SCALING** again to return to normal.

- **Rows:** the six rows are the bottom six, from the bottom up: Kick, Snare, Hihat 1, Hihat 2, Perc 1, Perc 2.
- **Lengths:** loading a pattern longer than the clip lengthens the clip the way clip multiply does, repeating every row's notes to fill it. Every row ends up the same length as the clip.
- **Undo:** each pattern change can be undone, and a bank load undoes in one step.
- **Clipboard:** loading a pattern replaces the copy/paste clipboard, as the Deluge's own Load Pattern does.

### Converting Stolperbeats pattern banks

[`tools/stolperbeats_to_deluge.py`](tools/stolperbeats_to_deluge.py) turns your own Stolperbeats `PatternBankNNN.txt` files into kit pattern mode banks:

```bash
python3 stolperbeats_to_deluge.py PatternBank000.txt --name TECHNO
```

- Each bank file becomes one bank folder. Copy the `STUMBLE` folder into `PATTERNS/RHYTHMIC/` on the Deluge's card.
- Every note gets velocity 127 (`--velocity` changes it), and every pattern is repeated out to 4 bars (`--bars` changes it), so 1-bar hats and percs line up with 4-bar kicks and snares.
- A `PatternExtNNN.txt` next to a bank adds its ratchets as quick repeated notes. Its pitch values are skipped.

No patterns are included in this repo.

[Back to top](#readme-top)

## 3. Autofill

TAP plays a drum fill over your beat, from the next 16th to the end of the bar. There are five fill types.

### Setting it up

1. **SHIFT + press SELECT** to open Settings, then go to **Community Features** (**FEAT**).
2. Set **Tap Tempo Action** (**TAPA**) to **Autofill** (**FILL**). This takes over the TAP button. Set it back to **Tap tempo** (**TAP**) for normal tap tempo.

### Playing fills

- **Press TAP** while playing. The fill starts on the next 16th and runs to the end of the bar. The TAP LED is lit while it plays.
- **Hold TAP** to carry the fill on into the following bars. It finishes the bar it's in when you let go.
- **Hold TAP and turn TEMPO** to pick the fill. The display shows its name. Turning cancels the fill your press started, so picking a fill never plays one.
- **SHIFT + TAP** still turns the metronome on and off.
- With TAP set to Autofill, the swing interval is only in the Song menu, because TAP + TEMPO picks fills instead.

### The five fills

Fills play on the bottom three rows of every playing kit: Kick, Snare and Hihat 1. They follow your swing, including the Stumble styles, and muted rows stay silent. Your patterns are never changed; the fill only changes what plays.

| # | Fill | What it does |
|---|---|---|
| 1 | **Ghost** (GHST) | Quiet snare and hat notes on the off-16ths |
| 2 | **Drive** (DRIV) | Straight 16th hats, snare pickups and a kick at the end of the bar |
| 3 | **Build** (BILD) | Random hits that get more likely through the bar, with some snare and hat ratchets |
| 4 | **Climb** (CLMB) | Like Build but steeper, with velocity rising, more ratchets late in the bar, and the snare stepping up 3, 5 and then 7 semitones each beat |
| 5 | **Stutter** (STUT) | Repeats your live pattern in shrinking loops of 4, 2 and then 1 step, with random drops, ratchets and octave jumps |

- **Ghost to Climb** only add hits where your pattern is silent.
- **Stutter** takes over each step completely.
- **Ratchets** split the step evenly at three quarters of the velocity, so they follow the swing too.
- **Pitch** (Climb and Stutter) shifts just that one note. Your pitch knob, any pitch automation and other sounding notes are untouched. It works on normal sound drums; MIDI and gate drum rows play fills unpitched.
- **Persistence:** the chosen fill is not remembered after power-off and starts on Build.

[Back to top](#readme-top)

## 4. Mono sequencer

Turns a synth, MIDI or CV track's grid into a mono step sequencer, built for basslines. The notes are ordinary Deluge notes, so clip length, nudging, ratchets (note repeat), copy and paste, undo and saving all work as normal.

### Turning it on

1. Open the clip's menu (press **SELECT** in the clip).
2. Turn **Mono Seq** (**MSEQ**) on. On synths it sits near the end of the menu, after Sequence Direction.

Mono is a setting on the clip, so it carries over if you switch the track between Synth, MIDI and CV.

### How it works

- **8 fixed rows:** the scale's first 8 steps from the song's root, root at the bottom. With a 7-note scale that's one octave plus the root an octave up. The grid doesn't scroll up or down; it follows your notes instead (see below).
- **One note per column:** placing a note clears that column on the other rows.
- **Octaves:** hold a note and turn the up/down knob (without pressing it) to shift it up to 4 octaves either way. The display shows the note it now plays, e.g. **D#5**, and you hear it.
- **Transposing the whole clip:** press and turn the up/down knob (with no note held) to move every note up or down an octave, as on any synth clip. The 8 rows follow the notes to their new octave, so they stay on the grid (fixed in v1.7.1).
- **The grid stays put while you edit:** adding and removing notes never moves the 8 rows, so a note placed on the bottom row stays on the bottom row and plays in that octave (fixed in v1.15.1: a lone note on the root row used to jump the grid down an octave).
- **Ratchets:** hold a note, then press and turn the up/down knob. This is the Deluge's normal note repeat.
- **Holding a note** shows and sounds the note it actually plays, octave included.
- **Always in scale (new in v1.16.1):** a mono clip's 8 rows are scale steps, so the clip always plays in scale mode. Turning Mono Seq on, or making the synth a 303, switches SCALE on (the song's scale is kept, or fitted to your notes), and songs saved with scale off come back in scale. Pressing SCALE on a mono clip shows **MSEQ** and leaves it on. Scales without seven notes and MIDI transpose clips are left as they are. Mono Seq belongs to the clip, so a new synth put on a mono clip stays mono: turn Mono Seq off in the clip menu to free it.
- **Fixed in v1.16.2:** a new synth clip, or SHIFT + SYNTH's first preset, could come up as an old unsaved 303 left in memory, bringing the mono sequencer and scale lock with it. New synths now skip unsaved 303s, and SHIFT + SYNTH always loads a saved preset.
- **Fixed in v1.23:** loading a song with a mono clip lost the rest of that clip (notes included) and every clip after it, and a kit or synth left with no clip was thrown away (**E044** on test builds). Mono clips now load whole. The files were never damaged.
- **Gate %** (**GATE**), in the same menu, shortens every note's gate, from 1 to 100% of its drawn length. Notes still keep their own lengths.

### Slide

- **Hold a note and click the up/down knob** (press and let go without turning) to switch slide on or off for that step. The display shows **SLID** or **OFF**. Holding several notes sets them all.
- A slide step plays its whole length, whatever Gate % is set to, and keeps sounding until the next step's note has started, so the two overlap.
- **On the 303** the pitch glides into the next note without retriggering, as on a real TB-303.
- **Over MIDI** the overlapping notes make 303 clones and other mono synths slide.
- **On CV** the gate stays open while the pitch moves.
- **On other Deluge synths** set Polyphony to Legato and turn up Portamento to hear a glide.
- Sliding into the same note ties it: the note carries on without retriggering. Sliding into a rest plays a normal note, as on a 303.
- Octaves and slides are kept together, so you can shift a slide step's octave and it stays a slide.

### Colours

| Pad | Means |
|---|---|
| White | A note in its own octave |
| Red, deeper per octave | Shifted up 1 to 4 octaves |
| Blue, deeper per octave | Shifted down 1 to 4 octaves |
| Orange tint | Edited: nudged, ratcheted, or given a probability, iterance or fill |
| Green tint | A slide step |
| Dim | The note's tail |

### CUSTOM voltages (CV only)

Set **Mono Scale** (**MSCL**) to **CUSTOM** and each of the 8 rows sends its own voltage instead of a scale note:

- Hold a row's audition pad and turn the **lower gold knob** to set its voltage, from 0 to 10 V in 10 mV steps (1 mV with SHIFT held). The output follows as you turn, so you can tune by ear.
- The rows start as a major scale between 0 and 1 V.
- Octave shifts add or remove 1 V on top of the row's voltage.

### How it plays

- **Synth and MIDI:** a note's octave moves the note it plays. Each row remembers which octave its note started in, so note-offs always match.
- **CV:** the octave, or the CUSTOM voltage, goes straight into the pitch voltage.
- **Limits:** recording live into a mono clip resets recorded notes to their own octave. One note per column is enforced when you place notes by hand, so pasting or nudging can still stack two in a column. On CV, the arpeggiator and pitch-bend changes can override the octave and CUSTOM voltages.

[Back to top](#readme-top)

## 5. Endless Record

On the stock Deluge, hitting RECORD while a new clip is already playing records in a loop, so you're stuck inside the clip's length. To record for as long as you like, you have to stop, arm RECORD and press PLAY. Endless Record gives you that second way of recording without stopping playback.

### Turning it on

1. **SHIFT + press SELECT** to open Settings, then go to **Community Features** (**FEAT**).
2. Turn **Endless Record** (**ENDL**) on. It's off by default.

### Using it

- **Hit RECORD while playing.** Every empty clip that's playing starts recording straight away. Each time it reaches its end it grows by its own length, so a 1-bar clip grows a bar at a time. The clip stays lined up with the bars, so if you start halfway through a bar, the first half stays empty.
- **Hit RECORD again to stop.** RECORD blinks, and your notes keep recording until the next bar line. Then recording switches off and the clip's length is set there.
- **Hit RECORD while it's blinking** to cancel the stop and keep recording.
- **Press STOP while it's blinking** and recording switches off with playback.

### Good to know

- It works on synth, kit, MIDI and CV clips that are playing and have no notes yet. Clips that already have notes overdub in a loop, as normal. Audio clips work as normal.
- Song view only, not the arranger.
- With it on, the blink-and-stop-at-the-bar also applies when you record the stock way (stop, arm RECORD, press PLAY).
- If you stop just after a bar line, the clip has already grown, so you'll get one extra empty bar.
- From v1.24 it's what closes the loop on a [MIDI loop track](#20-midi-loop-tracks).

[Back to top](#readme-top)

## 6. Drum synth

Synthesised drums as a Deluge oscillator. A drum synth row is still a normal Deluge sound: its envelopes, filters, FX, mod matrix, automation and parameter locks all work on top.

The engines:

- **Kick / tom** (**DRUM**), **Snare** (**SNAR**) and **Cymbal / hat** (**METL**): ported from the drum voices of the open source LXR-02 firmware by Erica Synths.
- **DXIA** (**DX-L**, **DX-B**, **DX-C**), called Drom1 before v1.11: three sine operators and a carrier, phase modulating each other in three routings.
- **DIIA** (**DI-G**, **DI-I**, **DI-H**), called Drom2 before v1.11: inharmonic, metallic partials with a noise strike, in three variants.
- **Cyc engines (new in v1.8):** **Cyc Kik** (**KIK**), **Cyc Snr** (**SNR**), **Cyc Metal** (**CMTL**), **Cyc Perc** (**PERC**), **Cyc Tone** (**TONE**), **Cyc Chord** (**CHRD**), **Vtg Snr** (**VSNR**) and **clap eng** (**CLAP**). Modelled on the Model:Cycles' six machines and the Syntakt's SD VINTAGE and CP VINTAGE, with the same knobs and starting values.
- **GIN** (**GIN**, new in v1.13): the drum voice from SquareWave Studio's GIN for the OP-1, built on Eric Lewis's libpo32, a PO-32 style drum synth. A tone with a pitch sweep, LFO or noise modulator, and a filtered noise layer with its own envelope, mixed, driven and EQ'd. See [GIN](#gin).
- **ULTRAKIK** (**ULTRAKIK**, new in v1.21): a kick engine. One swept oscillator into a wavefolder, four kinds of drive, grit, a click and a clean sub, with sixteen presets. See [ULTRAKIK](#ultrakik).
- **TRIBE** (**TRIBE KICK** to **TRIBE COWBELL**): an 808 / 909 drum machine, eight voices with an 808 > 909 knob each. See [TRIBE](#30-tribe).

### Making a drum synth kit

1. In clip view on an empty clip, press **SHIFT + KIT**.
2. The **New kit** (**NEW**) menu opens. Turn **SELECT** to a kit type and press **SELECT**:
   - **Kit** (**KIT**): a normal, sample based kit.
   - **Cycles** (**CYCL**): eight Cyc engine rows, from the bottom: the Model:Cycles' usual six tracks, **KIK**, **SNR**, **METAL**, **TONE**, **PERC** and **CHORD**, then **CLAP** (clap eng) and **PERC2** (Cyc Perc a fifth up), both new in v1.40. They play at the note as the Cycles does at its default tune.
   - **LXR** (**LXR**): eight LXR voice rows, from the bottom: **KICK**, **SNARE**, **CH** (closed hat), **OH** (open hat), **LTOM**, **HTOM**, **CYM** and **PERC** (new in v1.40: a short, woody perc on the drum voice). The two hat rows choke each other.
   - **GIN** (**GIN**): eight GIN rows, from the bottom: **KICK**, **SNR**, **HAT1**, **HAT2**, **PERC1**, **PERC2**, **CLAP** and **OTHER**, on the 808 kit. The two hats choke each other, and each row is tuned to its sound.
   - **TRIBE** (**TRIBE**): eight TRIBE rows, from the bottom: **KICK**, **SNARE**, **CH**, **OH**, **RIM**, **TOM**, **CLAP** and **CYM**, on the TRIBE kit. The two hats choke each other. See [TRIBE](#30-tribe).
   - **ULTRAKIK (single row only)** (**UKIK**) and **XIA (single row only)** (**XIA**): put that engine on the kit's selected row only, and open **SYNTH MODE** on it so you can pick another engine from there. On a track that isn't a kit yet, a sample kit is made first.

Vtg Snr, clap eng, DXIA and DIIA are picked per row in SYNTH MODE.

The rows an LXR, Cycles, GIN or TRIBE kit makes are its **preset rows** (new in v1.12). Their audition pads are softly coloured by the engine each plays: blue for the Cyc engines, orange for the LXR voices, green for DXIA and DIIA, pink for GIN and ULTRAKIK, red for TRIBE (brighter on the selected row).

Every Bribeluge kit has eight preset rows (new in v1.40), which is what lets them swap in and out of each other so easily, and lets you build around them.

- **Swapping kits (new in v1.40):** pick another kit in the SHIFT + KIT menu and the kit changes in place, row for row: row 1 becomes the new kit's row 1, and so on up to row 8, in every clip of the kit. The notes stay on their rows, so a pattern written on a Cycles kit plays straight away on TRIBE, LXR or GIN.
- **Adding rows:** tap an empty audition pad under the kick or over the top row and a new row appears there with **SYNTH MODE** open, to make it any engine, **Sample** or FM. Holding the empty pad and pressing **LOAD**, **SYNTH**, **MIDI** or **CV** works as on any kit. Added rows aren't coloured.
- **Added rows are kept (new in v1.40):** rows you add above or below the kit stay exactly where they are, with their sounds and notes, when you swap the kit for another or change its preset. Only the kit's own eight rows change.
- **The kit's own rows keep their order:** they can't be deleted (hold a note pad on the row and press **SAVE/DELETE**: the screen shows **CANT**), so every kit lines up with every other. Rows you added delete as on any kit.
- **Kits from before v1.40:** a Cycles kit saved with six rows or an LXR kit saved with seven gets its missing rows the first time you open its presets, turn **SELECT** on it or swap it. They go in straight over its top preset row, under anything you added above.
- **To a sample kit:** a preset kit with added rows can't be swapped for a plain **Kit**, as the added rows would lose their sounds: the screen shows **CANT**.

### Kit presets

On an LXR, Cycles, GIN or TRIBE kit, **SHIFT + KIT** opens **Kit presets** (**PRST**): the kit files in `KITS/LXR`, `KITS/CYCLES`, `KITS/GIN` or `KITS/TRIBE` on the card.

1. Turn **SELECT**. Each preset plays on the preset rows straight away, pattern running. Notes, added rows and the other rows stay as they are, and the audition pads still play the rows.
2. **SELECT** (or **KIT**) keeps the one showing. **BACK** puts the kit back as it was and goes up to the Kit / LXR / Cycles / GIN menu: its own type goes back into the presets, another swaps the kit in place, row for row.

The list is **Default** (the rows as SHIFT + KIT makes them) and then the presets in name order. On a GIN kit, Default is replaced by GIN's sixteen built in kits (on a TRIBE kit, TRIBE's eleven), so there's nothing to copy to the card. It opens on the preset the kit is on (kept with the kit when you save), or **Current** if it's on none of them.

- **Cycles presets:** sixteen kits of my own, bank E of my Model:Cycles kits, converted for the Cyc engines: copy [`presets/KITS/CYCLES`](presets/KITS/CYCLES) to `KITS/CYCLES` on the card. From v1.40 each has eight rows: the six from the Cycles, then a **CLAP** and a **PERC2** of its own.
- **LXR presets:** sixteen kits by **Hrtl** from the free [LXR-02 pack Erica Synths released in 2022](https://www.ericasynths.lv/news/fresh-kits-and-patterns-lxr-02-hrtl/), converted for the drum synth: copy [`presets/KITS/LXR`](presets/KITS/LXR) to `KITS/LXR` on the card. Close to the originals rather than identical (see the folder's README). From v1.40 each has an eighth row, **PERC**: the kit's own high tom voice a fifth up and shorter.
- **Presets with fewer rows:** a preset saved before v1.40 with six or seven rows still loads. The kit's rows above those keep the sounds they had.
- **Making presets:** a preset is an ordinary kit file. Set the kit up, press **SAVE**, go into `KITS/LXR`, `KITS/CYCLES`, `KITS/GIN` or `KITS/TRIBE` (made the first time you open the list) and save, over an existing preset or under a new name. Only the preset rows are read back. [`tools/lxr_to_deluge.py`](tools/lxr_to_deluge.py) converts LXR-02 .SND kits.
- **The kit takes the preset's name** (from v1.45.1): keeping a preset renames the kit after it, so the name stays on the display (and in the companion) after the next audition instead of going back to **KIT 0xx**. **Default** on an LXR or Cycles kit keeps the kit's own name. The renamed kit is the song's own until you save it as a kit.
- **Turning SELECT in the clip** (new in v1.19) steps to the next or previous preset in the same list and keeps it, without opening the list. It goes round at the ends.
- **Picking LXR, Cycles or GIN** in the New kit menu (new in v1.19) opens that kit's presets on the top one: the first preset in its folder, or Default if there's none (GIN: its first built in kit).
- Swapping sounds clears the undo history.

### Choosing an engine

Every engine and variant is in one list, **SYNTH MODE**. Hold a row's audition pad and press the **SYNTH MODE** pad (or the **OSC1 TYPE** pad on a drum synth row, which opens the same list):

| Group | Choices |
|---|---|
| The Deluge's own | **Sample** on a kit row (**Subtractive** on a synth), FM, Ringmod, 303 (synths only) |
| LXR voices | Kick / tom, Snare, Cymbal / hat |
| DXIA | DXIA L, DXIA B, DXIA C |
| DIIA | DIIA G, DIIA I, DIIA H |
| Cyc engines | Cyc Kik, Cyc Snr, Cyc Metal, Cyc Perc, Cyc Tone, Cyc Chord, Vtg Snr, clap eng |
| GIN | GIN (starts on the 808 kick) |
| ULTRAKIK | ULTRAKIK (starts on its ULTRA preset, at C2 on a kit row) |
| [TRIBE](#30-tribe) | TRIBE kick, snare, hat, rim, tom, clap, cymbal, cowbell (each starts as it sits in the TRIBE kit) |
| [BRIBERING MODE](#21-bribering-mode) | Bribering modal, sympathetic, string, FM, chord (new in v1.25; listed after 303) |

- Each engine you pick starts from its defaults, set up as its kit row is (new in v1.12): transpose, envelopes, filters open (the high pass on for the cymbal), osc 2 and noise off, tune centred, whatever the row was before. So what SYNTH MODE previews is what the kit plays. FX are left alone.
- **Envelopes (new in v1.12):** every drum engine shapes its hits with its own decay (the LXR voices' Decay, DXIA and DIIA's engine decay, the Cyc engines' amp decay). The Deluge envelope around it is open (attack 0, sustain full) with a release long enough for that decay to ring out after the note ends, so one tap plays the whole hit and gated sounds follow the note.
- A row that wasn't a drum synth also gets envelope 2 as a short blip (attack 0, decay 5, sustain 0, release 0) to patch to pitch for a snap.
- **DXIA and DIIA presets (new in v1.12):** each variant starts on a preset, level with the other engines (both are 6 dB louder than before): DXIA L a tight kick, B a knocky kick, C a long deep kick (envelope 2 on pitch drops them from about 200 Hz), DIIA G a snare-ish noise perc, I a zap, H metallic noise.

### Shortcut pads

Changed in v1.16: every drum engine has the same settings on the same pads, in the **MOD1** and **MOD2** columns. Hold **SHIFT** and press a pad to open its setting. Decay is on the decay pad on every engine, drive on the drive pad, and so on. An engine without a setting leaves its pad empty.

- **MOD1, from the bottom up:** Decay, Drive, Pitch, Pitch envelope amount, Pitch envelope speed, Character A, Character B, Extra 1.
- **MOD2, from the bottom up:** Extras 2 to 9, each engine's own settings.
- **OSC1 TYPE** opens SYNTH MODE. On BRINGS, BROPHET and BRUNO106, which lay out as synths (see [BRIBERING MODE](#21-bribering-mode), [BROPHET](#24-brophet) and [BRUNO106](#26-bruno106)), OSC1 TYPE is their model or wave: use the SYNTH MODE pad instead.
- **Every other pad is the Deluge's own again:** OSC1 level and transpose, OSC2 (a real second oscillator on a drum row), envelopes, filters, FX and the mod FX pads. The few whose Deluge setting a drum engine borrows for its controls (osc 1 pulse width, both oscillators' feedback and wave index) do nothing on a drum row, except on ULTRAKIK, which puts its extra settings there (new in v1.21).
- **Gold knob pairs** sit in one column: Drive / Decay, Pitch envelope speed / amount, Character A / B.

| Pad | Kick / tom | Snare | Cymbal / hat | DXIA | DIIA | Cyc engines | GIN | ULTRAKIK |
|---|---|---|---|---|---|---|---|---|
| MOD1 row 1 (bottom) | Decay | Decay | Decay | Engine decay | Engine decay | Amp decay | Decay (both) | Decay |
| MOD1 row 2 | Drive | Drive | Drive | Drive | Drive | Drive | Drive | Drive |
| MOD1 row 3 | Pitch | Pitch | Pitch | Pitch | Pitch | Pitch | Pitch | Pitch |
| MOD1 row 4 | Pitch amount | Pitch amount | | | | Sweep | Mod amount | Sweep |
| MOD1 row 5 | Pitch decay | Pitch decay | | | | Contour | Mod rate | Sweep time |
| MOD1 row 6 | FM amount | Noise mix | FM amount | Blendex 1 | Weight | Color | Mix | Fold |
| MOD1 row 7 | Mod pitch | Noise cutoff | FM 2 amount | Freq 1 | Alloy | Shape | Noise freq | Grit |
| MOD1 row 8 (top) | Pitch curve | Pitch curve | Mod 2 pitch | Punch | Punch | Punch | Mod mode | Punch |
| MOD2 row 1 (bottom) | Osc wave | Osc wave | Osc wave | Blendex 2 | Shape | | Tone wave | Sub |
| MOD2 row 2 | Osc mode (FM / mix) | Noise rate | Mod wave | Freq 2 | Strike | | Tone attack | Hold |
| MOD2 row 3 | Mod wave | Noise filter | Mod pitch | Blendex 3 | | | Tone decay | Click |
| MOD2 row 4 | Mod fine | Noise resonance | Mod fine | Freq 3 | | | Noise filter | Click type |
| MOD2 row 5 | Transient | Transient | Transient | | | | Noise reso | Click tone |
| MOD2 row 6 | Transient level | Transient level | Transient level | | | | Noise env | Bend |
| MOD2 row 7 | Transient speed | Transient speed | Transient speed | | | | Noise attack | Bend time |
| MOD2 row 8 (top) | | | Mod 2 wave | | | | Noise decay | Crush |

- **Cyc names:** Sweep / Contour are Pitch sweep / Mod envelope on Vtg Snr and Spacing crunch / Body envelope on clap eng; Color / Shape are Inharm / Freq complex and Body char / Balance. On Cyc Tone, Cyc Chord and clap eng, Sweep and Contour shape something other than pitch (see [Cyc engines](#cyc-engines)).
- **Drive** on the Cyc engines is the engine's drive (0 clean, 100 to start, 127 full saturation). **Punch** is its own pad, at the top of MOD1.
- **ULTRAKIK on OSC1 (new in v1.21):** PULSE WIDTH is its body wave, RETRIGGER its snap, FEEDBACK its drive type and WAVE INDEX its presets. OSC1 LEVEL, TRANSPOSE, TYPE and NOISE keep their jobs.
- **No pad:** Mod 2 fine on the Cymbal / hat, and GIN's EQ freq, EQ gain and level. They're in the sound menu under **Drum synth**.

### Gold knobs

Every drum synth row and the 303 share one layout, after the Cycles' knobs. It's set whenever the sound loads, however it was saved. Changed in v1.16 (with **Pad Guides** on, the default): the drum knobs follow the shortcut pads' shared settings.

| Knob | Every drum engine |
|---|---|
| Attack / Release | **Drive / Decay** (the envelope's attack and release are still in its menu) |
| Mod rate / Mod depth | **Pitch envelope speed / amount** |
| CUSTOM 1 | Tune |
| CUSTOM 2 / CUSTOM 3 | **Character A / B** (never decimation / bitcrush on a drum synth row) |

| Engine | Mod rate / Mod depth | CUSTOM 2 / CUSTOM 3 |
|---|---|---|
| Kick / tom | Pitch decay / Pitch amount | FM amount / Mod pitch |
| Snare | Pitch decay / Pitch amount | Noise mix / Noise cutoff |
| Cymbal / hat | LFO rate / Vibrato (no pitch envelope) | FM amount / FM 2 amount |
| DXIA | LFO rate / Vibrato (no pitch envelope) | Blendex 1 / Freq 1 |
| DIIA | LFO rate / Vibrato (no pitch envelope) | Weight / Alloy |
| Cyc engines | Contour / Sweep (Mod envelope / Pitch sweep on Vtg Snr, Body envelope / Spacing crunch on clap eng) | Color / Shape (Inharm / Freq complex on Vtg Snr, Body char / Balance on clap eng) |
| GIN | Mod rate / Mod amount | Mix / Noise freq |
| ULTRAKIK | Sweep time / Sweep | Fold / Grit |

- On the Cyc engines, mod depth is now Sweep and mod rate Contour (the other way round before v1.16).
- With Pad Guides off, the drum knobs keep the v1.11 layout. The knobs are set when a sound loads, so reload the song after switching it.

Every continuous drum synth setting is a Deluge parameter, so it can be parameter locked (hold a step and turn) and automated.

### Modulation and automation

- **Mod matrix:** every continuous setting on every engine can be modulated. Open the setting (its pad or the Drum synth menu) and press a mod source pad, as for any Deluge parameter: LFOs, envelopes, velocity, note, random, aftertouch and MPE all work. Each voice gets its own modulation, so velocity on Decay or random on Color changes every hit.
- **Depth:** the same on every setting. A cable at 50 with its source at full moves the setting 64 steps, from the middle to either end.
- **Automation view:** on a drum synth row the MOD1 and MOD2 columns follow the drum synth's shortcut pads, so each setting is on the pad you already use for it (changed in v1.16). Pads holding a choice (waves, modes, filter type, Punch) or the pitch are blank.
- **GIN EQ freq** is now a parameter too, so it can be locked, automated and modulated. GIN rows saved with v1.13 keep their EQ setting. EQ gain and GIN level stay row settings.

### Cyc engines

| Engine | Color | Shape | Sweep | Contour |
|---|---|---|---|---|
| Cyc Kik | Odd harmonic drive | Rounder, then spiky and buzzy, then noisy around 96 | Pitch drop depth and speed | Length of the pitch drop, short blip to long boom, plus the knock at the start |
| Cyc Snr | Rattle tuning | Rattle from tonal to noise | Body pitch drop | Noise dies early, leaving a tone |
| Cyc Metal | Spread of the partials | Density | Pitch drop | How fast the top end dies |
| Cyc Perc | Bright overtone | Modulation, hollow to gnarly | Pitch drop | Overtone decay and the length of the pitch drop |
| Cyc Tone | FM ratio, knob / 12 (24 = 2) | FM index | Index burst at the start | Index decay |
| Cyc Chord | Voicing | The chord, 38 of them in the Cycles' order | Wave, sine to buzzy | How fast the wave mellows |
| Vtg Snr | Inharm: body ratio | Freq complex: snares | Pitch sweep | Mod envelope |
| clap eng | Body char | Balance: tail against claps | Spacing crunch: gap between claps | Body envelope |

- **Drive** starts at 100: a soft clipper after the amp decay that gets louder as you turn it up and hard clips at 127, cleaning up as each hit dies away.
- **Amp decay** starts longer than the original machines' (for example 50 on Cyc Kik, 60 on Cyc Snr, 80 on Cyc Chord).
- **Punch** (the top MOD1 pad from v1.16) squares up and lifts the attack.
- They sound close to the originals, not identical: the same knobs and starting values, with the sound behind each knob measured from the originals and rebuilt. Cyc Kik's Contour, which barely did anything on the Cycles, sets the length of the pitch drop and the knock here. From v1.15 Contour stretches the pitch drop on Cyc Kik and Cyc Perc, and each engine's starting Contour sounds as before.

### GIN

GIN is the drum voice from [SquareWave Studio's GIN](https://github.com/squarewave-studio/op1-mods) for the original OP-1, which builds on Eric Lewis's [libpo32](https://github.com/ericlewis/libpo32), a PO-32 style drum synth. Each sound is two layers:

- **Tone:** a sine, triangle or saw with its own attack and decay, bent by a **Mod mode**: a decaying **sweep**, a **sine** LFO (at audio rates it frequency modulates the tone, for bells, cowbells and metal), or filtered **noise**.
- **Noise:** white noise through a low, high or band pass filter (or none), with its own attack and decay and an envelope that is exponential, linear or **modulated**, a decaying train of bursts for claps.
- **Mix** pans between them (0 tone, 64 both, 127 noise), then drive, a peak EQ and the GIN level, before a clipper.

Sixteen kits are built in, eight sounds each on the rows KICK, SNR, HAT1, HAT2, PERC1, PERC2, CLAP and OTHER. They're my own sounds, made for the Deluge (GIN's factory kits aren't included). Cycle through them with **SHIFT + KIT** on a GIN kit, or load any single sound onto a row with **GIN sound** (**GSND**) in the Drum synth menu.

| Kit | Style | Other |
|---|---|---|
| 808 | Classic analogue | Cowbell |
| 909 | Punchy, driven kick | Rim shot |
| ELEC | Electro: zaps, FM hats | Laser |
| MINI | Minimal, short and clicky | Bleep |
| INDU | Industrial, everything driven | Noise-bent saw |
| DUST | Lo-fi, tops rolled off | Rim tick |
| RUMB | Techno rumble, FM ride | Sub boom |
| ZAP | Fast deep sweeps, pews | Wobble blip |
| BOOM | Trap: long tuned 808, crisp tops | 808 tom |
| TITE | Tight and woody | Side stick |
| METL | Metallic: FM bells and gongs | Cowbell |
| DUB | Deep and round, syndrums | Falling syndrum |
| BLIP | Glitch: bleeps and broken noise | Noise-bent triangle |
| BRKS | Breakbeat crunch | Crash |
| PERC | Hand percussion: frame drum, shakers, congas | Clave |
| CHIP | 8-bit: triangle kick, raw noise | Coin |

- **Knobs:** Drive / Decay on attack / release, **Mod rate / Mod amount** on mod rate / depth (64 is none: above, the sweep starts high and falls; below, it starts low and rises), tune on CUSTOM 1, **Mix / Noise freq** on CUSTOM 2 / 3, as on GIN's own front panel.
- **Decay** moves the tone and noise decays together: 64 leaves the sound as it is, 0 is about 60 times shorter, 127 about 60 times longer. **Tone decay** and **Noise decay** are on their own pads.
- The pitch is the note and the row's transpose, not a setting: each kit row is tuned to its sound. Velocity works through the Deluge's usual velocity setting. There's no A / B morph (parameter locks do that job), and turning a knob changes a hit that's already playing.

### ULTRAKIK

ULTRAKIK is a kick engine, synthesised rather than sampled (put a sample on OSC2 if you want one on top). It starts as a thick, low thump with drive, fold, grit and a dark click already on and a short tail, and bends into long gliding 808s, hard 909s and fully broken kicks. Pick it in SYNTH MODE: on a kit row it plays at C2, on a synth at the note.

**How it works.** One oscillator (sine, round, triangle or saw) swept down from above by **Punch**, a very fast pitch spike (the beater), and **Sweep**, a slower drop (the boom). **Bend** moves the pitch slowly over the hit for 808 slides and drops, and **Snap** sets the phase it starts on. Then the amp (**Hold**, then **Decay**), a wavefolder (**Fold**), the **Drive** (Warm, Hard, Tube or Fuzz), **Grit** riding on the driven peaks, the **Click** (Thud, Tick, Noise or Zap), the **Crush**er, and **Sub**: a clean sine of the body under it all, so the low end survives whatever happens above it. Every setting peaks just under full scale.

| Pads | From the bottom up |
|---|---|
| MOD1 | Decay, Drive, Pitch, Sweep, Sweep time, Fold, Grit, Punch |
| MOD2 | Sub, Hold, Click, Click type, Click tone, Bend, Bend time, Crush |
| OSC1 | PULSE WIDTH body wave, RETRIGGER snap, FEEDBACK drive type, WAVE INDEX presets |

Its twelve continuous settings (everything on MOD1 and MOD2 except Pitch, Click type, Bend time and Crush) are parameters: lock them, automate them, modulate them. Gold knobs: Drive / Decay on attack / release, **Sweep time / Sweep** on mod rate / depth, **Fold / Grit** on CUSTOM 2 / 3.

**Presets.** Hold SHIFT and press OSC1 WAVE INDEX on an ULTRAKIK row (or **Kick preset**, **KPRE**, in the Drum synth menu) and turn SELECT: each turn loads the next preset, so you can play the row while you go through them. Press SELECT to leave. A preset sets every ULTRAKIK setting and the envelope release; on a kit row it also sets the pitch. FX are left alone.

| # | Preset | Kit row note | Sound |
|---|---|---|---|
| 1 | DEEP 808 | C1 | Clean, long sine 808 with a soft tick |
| 2 | GRIME SLIDE | C2 to C1 | Long 808 that slides down an octave |
| 3 | BOOM ROOM | C1 | Slow, deep sweep: a big round boom |
| 4 | 909 THUMP | C2 | Round body, short tick, tight |
| 5 | ULTRA | C2 | The default: thick, low thump with drive, fold, grit and a dark thud |
| 6 | CLUB 909 | C2 | Round body into hard clip, bright tick, hard snap |
| 7 | TUBE FAT | C2 | Triangle into heavy tube drive |
| 8 | TRAP KNOCK | C1 | Long 808 pushed hard into tube drive |
| 9 | HARDSTYLE | C2 | Saw, heavy drive and fold, long tail |
| 10 | DISTORTO | C2 | Hard clipped 909 with a noise burst and grit |
| 11 | RUMBLE | C2 | Long, gritty, driven: a techno rumble |
| 12 | GABBER | C2 | Full drive into hard clip, folded, long and thick |
| 13 | BITCRUSHER | C2 | Saw into hard clip, crushed, zap click |
| 14 | FUZZ BOMB | C2 | Triangle into fuzz, heavy grit |
| 15 | FOLD STORM | C2 | Folded almost all the way, bright and metallic |
| 16 | ANNIHILATE | C2 to C1 | Everything up, crushed, dropping an octave fast |

- **808 lines:** on a synth track, set polyphony to **LEGATO**, add some portamento and set Decay to 127 (it holds while the note does), then overlap notes to slide.
- **CPU:** measured on a computer at about 1.4 times a Cyc Kik voice at the defaults and under 1.8 times with everything on. Each stage switches off once it's done.
- **Known issue:** on some rows of the Deluge's sample kits ULTRAKIK can stay silent when picked in SYNTH MODE. It plays on LXR, Cycles and GIN kit rows and on most sample kit rows.

### Snappy decay

**Snappy decay** (**SNAP**), in the sound menu of any drum synth row, makes the amp envelope's decay and release follow a steeper curve: tighter hits, and the same decay setting sounds about half as long. It starts off on new drum synth rows (from v1.12: each engine's own decay does the shaping) and is saved with the row.

### Good to know

- The full settings list and a pad-per-setting editor (GIN has its own) are in the sound menu under **Drum synth** (**DRUM**). In the pad editor, turn the horizontal encoder or press **SCALE** (left) and **CROSS SCREEN** (right) to move between settings; both buttons are lit while it's open (new in v1.39.1). **Load preset** (**PRST**) there has the seven kit sounds and each DXIA and DIIA variant.
- **SHIFT + press SELECT > CPU load** (**LOAD**) shows the audio engine's load, for checking how many drum synth voices you can run.
- **One voice per row (from v1.49):** a kit row on a drum engine plays one voice, like a drum machine. A new hit cuts the last one and starts again, whatever the row's gate length or polyphony setting, so ratchets, Autofill fills and long notes never pile voices up. Choke groups work as before.
- **Settings > Defaults > High CPU Indicator** (**CPU**) set to **ON** makes the **PLAY** button blink whenever the Deluge runs out of CPU and cuts notes to keep up (voice stealing). It's off until you turn it on.
- **From v1.17** each hit ends once it's 72 dB down (it was 100 dB, 80 on GIN). The Cyc engines fade out over the last few samples. When the CPU runs short, a hit that's 40 dB down is cut before notes you can still hear. See [New in v1.17](#readme-top) at the top.
- **From v1.18** the Cycles engines build their sines from a lookup table and cost an estimated third to a quarter of what they did, for the same sound. Metal's feedback is chaotic, so its waveform never comes out exactly the same from one build to the next, but it sounds the same.
- Fixed in v1.8: loading a song no longer resets the LXR transient level and speed, or DXIA's Freq 2 and 3.
- Fixed in v1.15: CUSTOM 1 tunes rows loaded from preset kit files too (it was on portamento).
- **Kicks send to the sidechain (from v1.22.2).** Cyc Kik, ULTRAKIK, the LXR kick and the GIN kick sounds send full to the sidechain when a preset kit loads, when one is picked on a row or a synth (SYNTH MODE, an ULTRAKIK preset, a GIN kick sound, the LXR kick preset), and when a kit or synth preset loads from the card (LXR drum and GIN sounds there only if named kick, kik or bd, as kick samples are). Picking something else lets go of the full send. Songs keep what they were saved with.
- Kits with drum synth rows won't play those rows on firmware without them.
- The full reference is in the source patch, at `website/src/content/docs/features/drum_synth.mdx`.

[Back to top](#readme-top)

## 7. Saturation

The Deluge's own saturation squashes hard even at its lowest setting and gets quieter as you turn it up. This build replaces it with a one-knob drive that works like pushing an analog input stage: more drive is always denser and louder.

### Using it

**SHIFT + SATURATION pad**, or **FX > DISTORTION**, on any synth, kit row or audio clip. For a whole kit, turn **Affect Entire** on first: the kit's own **FX > DISTORTION** menu and the SATURATION pad now have it too.

- **Saturation** (**SATURATION**): the drive, **OFF** or 1 to 50. 1 is close to clean. The knob is gentle at first and steep at the top, up to +36 dB of gain into the curve. The peak level stays put while everything under it comes up, so it gets louder and thicker as you turn it.
- **Type** (**TYPE**): the curve.

| Type | 7-seg | Sound |
|---|---|---|
| **Tape** | **TAPE** | The default. Smooth and rounded, with a little even-harmonic warmth. Turns into a hard clip over the top half of the knob. |
| **Warm** | **WARM** | The softest knee and the most even harmonics. Hardens near the top. |
| **Clip** | **CLIP** | A firmer knee, more like an overdrive. Hardens sooner. |
| **Hard** | **HARD** | A hard clipper all the way. |
| **Fold** | **FOLD** | A wavefolder: bright and metallic as the drive rises. Best on bass and pads. |
| **Classic** | **CLAS** | The original Deluge saturation, unchanged. |

Hold **Affect Entire** while turning either setting in a kit row's menu to set every row at once.

### Good to know

- Songs and presets made before v1.5 load with **Classic**, so they sound the same. A sound that had no saturation starts on **Tape** when you turn it up.
- **Gold knobs, automation and MIDI (new in v1.16.1):** the drive is now a parameter. Learn it to a gold knob on any synth or kit row (open it with **SHIFT + SATURATION pad**, then hold **LEARN** and turn the gold knob, with its button's context selected), draw it in automation view on the SATURATION pad, MIDI learn it, or hold a step and turn to parameter lock it. Kit-level and audio clip gold knobs keep their fixed layout. On drum synth rows, the attack / release, mod rate / depth, CUSTOM 1 and CUSTOM 2 / 3 knobs are set again whenever the row loads, so learn saturation onto another knob there.
- Songs and presets saved before v1.16.1 keep their drive. From v1.16.1 files store the drive as a parameter only, so other firmware loads them without saturation.
- Saturation sits after the filters and the amp envelope, as before, so the sound's volume and velocity change how hard it drives.
- The curves are antialiased, so high notes alias less than with the original, except Fold, which aliases when pushed hard on bright sounds, as digital folders do.

[Back to top](#readme-top)

## 8. Sample start offset

Moves where a sample starts playing. It's a normal Deluge parameter, so every step can start from a different point.

### Using it

On any synth or kit row whose oscillator plays a sample:

- **SHIFT + the PULSE WIDTH pad** in the OSC1 or OSC2 column opens **Start offset** (**OFST**) for that oscillator. Pulse width does nothing on a sample, so the pad is reused. On synth waveforms it's still pulse width.
- The offset runs from **-512** to **+512**. **+256** starts halfway through the sample, and **+512** goes all the way round, back to the start. Negative values start earlier.
- **Offset wrap** (**WRAP**), just after it in the oscillator menu, is on by default. Off, the start stops at the sample's edges, and a negative offset that would start before the sample plays silence first.

### Per-step offsets

- **Automation view:** press the oscillator's **PULSE WIDTH** pad, then tap pads in each step's column to draw the offset across the pattern.
- **Gold knob:** in the Start offset menu, hold **LEARN** and turn a gold knob to put the offset on it. Then hold a step and turn that knob to lock the step.
- **Mod matrix:** patch velocity, an LFO or an envelope to it like any other parameter. Velocity to offset makes harder hits start later in the sample, for example.

### With loops

- The whole playback window moves, loop markers included. If that pushes the loop past the end of the sample, it plays from the loop start to the sample end, then from the sample start to the loop end, and repeats.
- In **LOOP** and **STRETCH** modes, changing the offset while a note is held moves playback straight away. A small click on the jump is normal.
- It works with reverse and time stretch too.

### Good to know

- The offset and its automation save with the song and the preset. Other firmware ignores them and plays from the normal start.
- Pitched notes with an offset skip the Deluge's sample cache, so they cost a little more CPU than the same note without one.

[Back to top](#readme-top)

## 9. 303 synth

A TB-303 style bass voice, ported from the open source [Open303](https://github.com/RobinSchmidt/Open303) by Robin Schmidt: its saw and square oscillator, its model of the 303's ladder filter, its envelopes, accent and slide. The Deluge's saturation, mod FX, EQ, delay, reverb, sidechain and volume all work after it.

### Turning it on

1. On a synth track, press the **SYNTH MODE** shortcut pad (or find **Synth mode** in the sound menu).
2. Choose **303**. The sound starts on an acid setting: cutoff 500 Hz, resonance and env mod well up, decay 400 ms.

A 303 track always plays from the mono sequencer, so its grid becomes the 8 fixed rows with octaves and slides, and the **Mono Seq** setting is hidden. Choose another synth mode to go back; the clip goes back to how it was.

### Controls

| Control | Where | What it does |
|---|---|---|
| **Cutoff** (**CUT**) | Gold knob Cutoff/Res (top), SHIFT + LPF FREQUENCY pad | Filter cutoff, 314 to 2394 Hz as on the 303 |
| **Resonance** (**RES**) | Gold knob Cutoff/Res (bottom), SHIFT + LPF RESONANCE pad | Filter resonance |
| **Env mod** (**ENV**) | Gold knob Mod rate/depth (bottom), SHIFT + MOD1 LEVEL or MOD FX DEPTH pad | How far the envelope opens the filter |
| **Decay** (**DCAY**) | Gold knob Mod rate/depth (top), SHIFT + MOD2 LEVEL, MOD FX RATE or ENV2 DECAY pad | The filter envelope's decay. Changed in v1.22.1: the knob sets how much of the envelope is left at the end of a 16th at 130 bpm, about 30 ms at the bottom to 2.8 s at the top, so it changes a pattern evenly across its travel, and it acts as you turn it. It shapes the filter only, so turn up Env mod to hear it. Songs saved before keep their knob position, which now gives a different time |
| **Drive** (**DRIV**, new in v1.11) | Gold knob Attack/Release (top), SHIFT + OSC1 FEEDBACK or LPF MORPH pad | Changed in v1.22.1: an overdrive after the filter, on all three filters. It runs oversampled, so it doesn't alias, thins the lows going into the clip and puts them back after so the bass stays full, adds a little lopsided warmth, and darkens from 12 kHz to 4 kHz as it goes up to keep the fizz down. Accents bite first, the resonance keeps its squelch, and it ends about 3 dB louder than clean. 0 is clean |
| **Amp decay** (**ADEC**, new in v1.11) | Gold knob Attack/Release (bottom), SHIFT + OSC1 WAVE INDEX or ENV1 DECAY pad | How long each note's level dies away while held: 60 ms, Open303's own 1230 ms at the centre (where older 303s sit), holding at the top |
| **Accent** (**ACC**) | Gold knob CUSTOM 2, SHIFT + OSC1 RETRIGGER pad | How hard accented notes hit |
| **Saw-square** (**WAVE**) | Gold knob CUSTOM 3, SHIFT + OSC1 PULSE WIDTH or OSC2 FEEDBACK pad | Fades from saw (0) to square (50) |
| **Slide time** (**SLID**) | Gold knob Portamento (bottom), SHIFT + MOD1 FEEDBACK pad | How long a slide takes to arrive |
| **Filter** (**FILT**) | SHIFT + LPF MODE or MOD2 FEEDBACK pad, the LPF MODE menu | **DIRT** (new in v1.22), the TB-303 filter with saturation where the note meets the resonance; **303**, Open303's clean model of the TB-303's filter; or **LP18**, Open303's plainer 18 dB lowpass. A new 303 starts on DIRT, and from v1.22.1 so do 303s saved before v1.22 |

They're all in the sound menu under **303** too. Every one except Filter is a Deluge parameter, so it can be parameter locked (hold a step and turn) and automated.

### Accent and slide

- **Accent:** any note with velocity 100 or more is accented. It opens the filter further, with half the Decay knob's time (200 ms at the default, as on a 303; changed in v1.22.1), and hits harder. Set a note's velocity as normal on the Deluge.
- **Slide:** hold a step and click the up/down knob (see the mono sequencer). Played live, notes slide when they overlap, as on Open303.

### Good to know

- The 303's own oscillator, filter and envelopes replace the Deluge's: the oscillator, envelope and unison settings do nothing in 303 mode, nor do the HPF settings. From v1.22 the LPF MODE menu and pad pick the 303's own filter instead of the Deluge's. **Saturation** (SHIFT + SATURATION pad) works as on any synth, and drives the 303 the way it drives a voice.
- Patch cables (LFOs and envelopes) don't reach the 303's controls yet. Gold knobs, menus, parameter locks and automation do.
- Transpose, Fine tune and the arpeggiator all work. It's mono, so it plays one note at a time.
- Songs and presets save the 303 setting. Firmware without it loads the sound as a normal subtractive synth.
- In automation view the 303's controls sit on the FM pads they're saved on, so OSC1 FEEDBACK there is Accent and MOD2 FEEDBACK is Drive, unlike the shortcut pads.
- **Fixed in v1.16.3:** with a 303 sounding, a busy song that ran out of CPU could scramble memory and freeze (any error code, often after notes moved around on their own). The Deluge now cuts only real voices when it's overloaded. The 303 itself is never cut, so it still uses CPU that the other voices compete for.
- **From v1.17** the 303 works out its filter every 4 samples instead of every sample, gliding in between, and skips work it doesn't need, so it uses less CPU for the same sound.

[Back to top](#readme-top)

## 10. Delay feedback and tone

On the stock Deluge, the delay's Amount sets both how loud the echoes are and how much of each echo is fed back, so turning it up always brings more repeats too. Here they're two controls, plus a filter in the delay loop to change its voicing.

### Using it

- **Amount:** the lower gold knob with the knobs on delay, or the delay amount pad, as before. It now sets only how loud the echoes are.
- **Feedback:** hold **SHIFT** and turn the Amount knob. **0** gives a single echo, **25** repeats forever, and above 25 the repeats build up and saturate, as Amount did before. While SHIFT is held, the knob's LEDs show the feedback. On the 7-segment display the value has an F in front (**F13**).
- **Tone:** hold **SHIFT** and turn the Rate knob. Turn left for a lowpass that sweeps down from 20 kHz to 150 Hz, right for a highpass that sweeps up from 20 Hz to 5 kHz. The middle is flat, and the knob catches there. The filter sits in the loop, so every repeat goes through it again: each echo comes back darker (or thinner) than the last, like a tape echo. On the 7-segment display it shows **L12** (lowpass), **H12** (highpass) or **FLAT**.
- **On the pads:** press the delay **AMOUNT** shortcut pad twice to get Feedback, and the delay **RATE** pad twice to get Tone. The pad blinks yellow while you're on the hidden setting, the same way the envelope pads reach envelopes 3 and 4. Press once more to go back.
- Feedback (**FDBK**) and Tone (**TONE**) are also in the delay menu, just after Amount, and in automation view, so they can be drawn step by step or automated.
- They work everywhere the delay does: synths, kit rows, whole kits, audio clips and the song's master FX.

### Good to know

- New sounds start with feedback at 13 (half), so turning Amount up still gives a short tail of repeats.
- Songs and presets from the stock firmware, or saved before v1.9, keep the stock delay: feedback follows the amount exactly, automation and modulation on the amount included, so they sound the same. Once you set the feedback, the two are separate. Until then the feedback menu shows the amount.
- The tone starts flat, so it changes nothing until you turn it. When flat, the filter is switched off entirely.
- Feedback and tone save with the song and the preset. Other firmware ignores them: it uses the amount for both level and feedback, and no filter.

[Back to top](#readme-top)

## 11. Affect all

A performance snapshot for any kit: push every row around at once, then drop back to where you started on the next bar.

### Using it

1. In the kit's clip, press **SHIFT + AFFECT ENTIRE**. The kit is snapshotted and **AFFECT ENTIRE** flashes (**ALL**). You start in **All voices**.
2. **All voices:** turn any gold knob, or press **SHIFT** + a shortcut pad and turn **SELECT**, and every sound row moves by the same amount, each from where it was. Turn Sweep and every drum's sweep goes up; turn CUSTOM 1 and the whole kit retunes, staying in tune with itself.
3. **Kit FX:** press **AFFECT ENTIRE** on its own to swap to the kit's FX (**FX**), as AFFECT ENTIRE normally does, and again to go back to **All voices**. Swap as often as you like: the snapshot holds both.
4. Press **SHIFT + AFFECT ENTIRE** again. **AFFECT ENTIRE** flashes twice as fast (**BACK**), and on the next bar every drum and the kit's FX go back to the snapshot, before that bar's first hits. When stopped, it goes back straight away (**DONE**).

### Good to know

- Every sound row moves: drum synths, samples and synths. A drum engine's own controls (a decay, a sweep) move on the other drum synth rows only, each on its own engine's control for that knob or pad; settings every sound has, like the filters and envelopes, move on every row. MIDI and gate rows are left alone.
- A drum pushed to the end of a setting keeps its place against the others when you turn back.
- Nothing you do in affect all is recorded as automation, so the snapshot always puts the kit back exactly. Holding notes and turning a knob still parameter locks that row, as normal.
- Choices (waves, modes, filter type), patch cable amounts and transpose stay on the one row.
- The snapshot is held in memory only. It isn't saved with the song, and loading another song drops it.
- On a kit with no sound rows (only MIDI or gate rows), **SHIFT + AFFECT ENTIRE** shows **CANT**.

[Back to top](#readme-top)

## 12. Pad Guides

Visual guides to what each pad and gold knob does. **Pad Guides** (**GUID**) is in **Community Features** and starts on.

### Persistent overlay

Bribeluge's own overlay for its kits and synths: the pads where a drum engine or a Bribesynth keeps its settings. It was the SHIFT glow before v1.39.2.

- In a clip on a drum synth (a synth, or the kit's selected row), hold **SHIFT**. The MOD1 and MOD2 pads that hold a setting pulse soft pink, on the slow two-beat breath a synth track's section pad has in song view: in time with the song while it plays, at its tempo when stopped.
- It stays whatever **Community Features > Shortcut Overlay** is set to (new in v1.39.2; the overlay used to hide it):
  - **Overlay up** (SHIFT in a sound menu, or SHIFT in the clip with **On - Menu + Clip**): the pads pulse at full brightness over the overlay's dimmed colours. The pulse is how to tell them from the stock shortcuts, some of which are purple too.
  - **Overlay off, or not shown in the clip:** the pads fade in and out of whatever is on them, so notes still show.
- Press one and the pads stay lit while you edit that setting, with SHIFT still held or let go. Empty pads in those columns grey out with the rest of the grid.
- Let go of SHIFT on the clip and the pads go straight back. Select another row with SHIFT held and the pulse follows it.
- On the synth engines, [BRINGS](#21-bribering-mode), [BROPHET](#24-brophet) and [BRUNO106](#26-bruno106), the pulse is **purple**, and it lights their pads on the OSC1, OSC2, FM MOD 1 and FM MOD 2 columns.
- No pulse with **AFFECT ENTIRE** on in a kit, where SHIFT + pad edits the kit's FX.

### Gold knob pads

- Hold any gold knob button. Its two settings' names show as before, and their shortcut pads flash: **red** for the top knob, **yellow** for the bottom.
- Works on every sound (synths, FM, the 303, drum synth rows, sample rows) and on kit, audio clip and song FX.
- A setting with no pad (a learned MIDI CC, most patch cables) just shows its name. The flashing stops when you let go.

### Knob buttons

New in v1.29: the same thing the other way round.

- Press a shortcut pad (SHIFT or an audition pad + the pad). If that setting is on a gold knob, the knob's button LED blinks four times. **LPF FREQ** or **LPF RES** blinks **CUTOFF / RES**.
- It reads the sound's own knobs, so knobs you've learned count, and so do the 303's and the drum and synth engines' layouts.
- Kit FX (AFFECT ENTIRE) and audio clips use their own knob layout. The delay feedback and delay tone pads blink **DELAY**, since SHIFT + the delay knobs edit them.
- One LED covers both knobs, so it shows the pair, not top or bottom.

### Pad names

New in v1.20, on a 7-segment Deluge.

- Hold **SHIFT** (or an audition pad) and hold a shortcut pad. The display scrolls the full name of the setting it opens, the one the OLED shows as its title, instead of the four-letter name. On the drum synth pads that's the engine's own name for it, like Amp decay, Color or Shape.
- Let go of the pad and the display shows the value. Turning SELECT while you hold shows the value straight away.
- Press a pad twice for its second layer and that layer's name scrolls.
- Works on every shortcut pad, on every sound, and on kit, audio clip and song FX. It doesn't depend on the Pad Guides setting.

### Drum synth knobs

Drum synth rows' gold knobs follow the shared pad layout (see [Gold knobs](#gold-knobs)). With Pad Guides off they keep the v1.11 layout.

[Back to top](#readme-top)

## 13. Synth browser

**SHIFT + SYNTH** opens the synth browser, the way SHIFT + KIT picks a kit type: choose a type, then a category, then play through its presets with your pattern running.

| Type | Screen | Folder | What it holds |
|---|---|---|---|
| **Subtractive** | **SUBT** | `SYNTHS/SUBT` | Subtractive synths |
| **FM** | **FM** | `SYNTHS/FM` | FM synths |
| **Wavetable** | **WAVE** | `SYNTHS/WAVE` | Wavetable synths: 99 presets on the free BVKER wavetables |
| **Ring mod** | **RING** | `SYNTHS/RING` | Ring mod synths |
| **Brings** | **BRINGS** | `SYNTHS/BRINGS` | [BRIBERING MODE](#21-bribering-mode) sounds: 37 presets |
| **DX7** | **DX7** | `SYNTHS/DX7` | DX7 voices: 288 presets (the DX7 engine is always on) |
| **Brophet** | **BROPHET** | `SYNTHS/BROPHET` | [BROPHET](#24-brophet) sounds: Pro-53's 512 programs and 24 more |
| **Bruno106** | **BRUNO106** | `SYNTHS/BRUNO106` | [BRUNO106](#26-bruno106) sounds: 212 presets |
| **303** | **303** | `SYNTHS/303` | [303 synth](#9-303-synth) sounds you save; with none yet, a blank 303 |
| **Init** | **INIT** | | The stock blank synth |

Every type's folder holds four categories, in this order: **LEAD**, **BASS**, **PAD** and **MISC**. DX7 has six: **LEAD**, **BASS**, **PAD**, **KEYS**, **BELL** and **MISC**. BROPHET's follow Pro-53 instead: **BNK1** to **BNK8**, then **BRIB**.

### Using it

1. Press **SHIFT + SYNTH**. The **Instrument** (**INST**) list opens on the type the track plays. On a track with no synth yet (MIDI, CV or an empty kit), it opens on your default synth type (see [Instrument Picker](#14-instrument-picker)), or SUBT.
2. **SHIFT + SYNTH** again, or turn **SELECT**, to move on. **SELECT** or **SYNTH** opens it.
3. The **Category** (**CATE**) list shows the categories that hold presets. **SELECT** or **SYNTH** opens one.
4. Turn **SELECT** to play through the presets, each loading as you land on it, and press **SELECT** to keep one. **BACK** returns to the categories; **BACK** again returns to the types, and **BACK** from the types puts the track back exactly as it was.

**The audition pads play the whole way.** On each type the pads play that type's init synth, through its categories and into its folder, until you land on a preset:

- **A track with no synth** starts with the init of the type the list opens on, so there's always something to play.
- **A synth track** plays its own patch on its own type, and through that type's categories and folder (opening on your preset if it lives there). Move to another type and you hear that type's init; move back and your patch comes back.
- **Your own init:** save a synth as `SYNTHS/INIT/<TYPE>.XML` (like `SYNTHS/INIT/WAVE.XML` or `SYNTHS/INIT/BRUNO106.XML`, and `INIT.XML` for INIT) and the picker plays that instead of the built in one.
- **DX7's init** is a simple two-operator FM voice rather than the DX7's own bare sine.

Also:

- It works on synth, MIDI and CV tracks, and on a kit track with no notes or sounds yet.
- A type's folders are made the first time you pick it, ready to save into. A type with no presets yet keeps its init synth, which saves into its folder.
- Presets kept loose in a type's folder, outside the categories, open as one flat list when none of its categories hold presets.
- On the 7-segment display, a type, category or option longer than four letters (like **BRINGS**) blinks twice, then scrolls back and forth so you can read it. This works in every context menu.

### The presets

- **WAVE:** 99 presets, one for each wavetable in the free [BVKER Custom Wavetables](https://bvker.com/free-serum-wavetables/) pack, which you download yourself (see [Download](#download)). Each starts where its wavetable has some body and moves through the part that changes, with an envelope, an LFO or velocity. They're named by recipe, wavetable family and number: basses are **Punch**, **Reese** or **Wobble**, leads **Mono**, **Poly** or **Sweep**, pads **Wide**, **Bloom**, **Air** or **Drift**, and MISC holds **Pluck**, **Bell** and **Keys**. Tables that are close to a sine get the wavefolder and a second oscillator. On every WAVE preset **CUSTOM 2** moves the wavetable position and **CUSTOM 3** sets how far LFO 1 sweeps it.
- **DX7:** 288 voices, sorted by name into LEAD, BASS, PAD, KEYS (pianos, organs, clavs), BELL (bells, mallets, chimes) and MISC, 48 in each. Yamaha's original ROM cartridges come first, then the rest of the collection with duplicates taken out. [`presets/SYNTHS/DX7/SOURCES.txt`](presets/SYNTHS/DX7/SOURCES.txt) lists the cartridge and slot each came from. The DX7 menu's cartridge browser still loads `.syx` files as before.
- **BRINGS:** 37 BRIBERING MODE presets across all five models: basses, plucked and struck leads, bowed and chordal pads, bells and drones.
- **BROPHET:** all 512 of Pro-53's programs, and 24 Bribes presets (see [BROPHET](#24-brophet)).
- **BRUNO106:** 212 presets: 13 made for this build, and 199 converted from the preset data that ships with KR-106 (see [BRUNO106](#26-bruno106)).
- **Your own presets:** [`tools/sort_synth_presets.py`](tools/sort_synth_presets.py) copies every synth preset in `SYNTHS` (and its other folders, like `DLFM`) into the right type and category, by name first (bass, pad, lead, pluck, bell), then by how it sounds (low transpose, slow attack, long release, mono, arpeggiator). The originals stay where they are, and a preset that lands in the wrong category can be moved by hand.

```bash
python3 tools/sort_synth_presets.py /Volumes/DELUGE --dry-run
python3 tools/sort_synth_presets.py /Volumes/DELUGE
```

[Back to top](#readme-top)

## 14. Instrument Picker

Pick the instrument every new kit track and every new synth track starts as. Press **SHIFT + SELECT** to open Settings, then go to **DEFAULTS > UI > CLIP TYPE**:

| Setting | Screen | Options |
|---|---|---|
| **Kit Instrument** | **KIT** | **OFF** (stock), **LXR**, **Cycles**, **GIN** |
| **Synth Instrument** | **SYNT** | **OFF** (stock), **SUBT**, **FM**, **WAVE**, **RING**, **BRINGS**, **DX7**, **BROPHET**, **BRUNO106**, **303** |

With one set, a new track of that type starts on the instrument's top preset that isn't already on another track: the first in `KITS/LXR`, `KITS/CYCLES` or the synth type's folder, LEAD first (see [Synth browser](#13-synth-browser)). If there's none, you get a blank one: the kit as SHIFT + KIT makes it, or a blank synth of that kind. A GIN track starts on GIN's first built in kit.

- **Counts as a new track:** a new clip in song view, a new arranger track, the **KIT** or **SYNTH** button on a clip that has never been that type (one that has goes back to what it had), and the synth a new song starts with.
- **Then:** turning SELECT on a synth steps through its folder as usual, and on an LXR, Cycles, GIN or TRIBE kit through that kit's presets (see [Kit presets](#kit-presets)). SHIFT + KIT and SHIFT + SYNTH still open the full pickers.
- Both settings start on **OFF**, so new tracks are stock until you change them.

[Back to top](#readme-top)

## 15. Gate out

**Gate out** (**GATE OUT**) sends a kit's bottom four rows out of the Deluge's four gate outputs as they play: row 1 to gate 1, row 2 to gate 2, row 3 to gate 3, row 4 to gate 4. On the LXR and Cycles preset kits that's kick, snare, hat 1 and hat 2, so a modular or another drum machine can follow the kit.

| Setting | Where | What it does |
|---|---|---|
| **Gate** (**GATE**) | First in a kit row's menu: hold the row's audition pad, press SELECT, press SELECT on GATE (changed in v1.22.2) | That row's gate: **OFF** or gate **1** to **4**, showing the gate it fires. On any sound row. Picking a gate on a kit that isn't on the gates puts that row alone on them; turning the last row off takes the kit off. Saved with the song |
| **Gate out** (**GATE OUT**) | First in the kit's menu (AFFECT ENTIRE on) | On or off for the whole kit. Turning it on with no rows on a gate starts from rows 1 to 4 on gates 1 to 4. Off on new kits, saved with the song |

- **One kit at a time.** Turning Gate out on for one kit turns it off for every other kit in the song. Two rows can share a gate.
- **Gate length.** A sound with a tail (a held note, a decay that holds) holds its gate for as long as the note plays. A one-shot hit sends a 12 ms trigger. A new hit drops the gate first, so every hit retriggers, and every gate stays high at least 12 ms so a module always sees it.
- Any sound row in rows 1 to 4 fires a gate, samples included, and the arpeggiator's notes too. MIDI and gate rows don't.
- **MIDI too (from v1.23).** Right after **GATE** in a row's menu, **MIDI** sets a channel and note the row sends as it plays, alongside its sound and its gate. On a one-shot row the MIDI note is held 12 ms, like the gate.
- **The kit's gates are its own (from v1.22.2).** CV clips and a kit's GATE rows can't use a gate a Gate out row is on. A new CV clip skips CV channels whose gate is taken, and shows **no unused channels** if gates 1 and 2 both are. Move a row off gate 1 or 2 to free it.

[Back to top](#readme-top)

## 16. MIDI kits

An **MKIT** is a kit whose sixteen rows are MIDI rows. Kit pattern mode, Autofill, Affect Entire and everything else a kit does then play your other gear: a drum machine, a sampler, a rack of synths.

### Making one

1. In clip view on an empty clip, press **SHIFT + MIDI**.
2. The display shows **MIDI**. Turn **SELECT** (or press SHIFT + MIDI again) to **MKIT** and press **SELECT**. Picking **MIDI** makes an ordinary MIDI track, as the MIDI button always has.
3. Pick a layout and press **SELECT**:

| Layout | Display | Rows |
|---|---|---|
| **1 channel, GM drums** | **1CH** | All on channel 10, on General MIDI drum notes. Rows 1 to 6 are kick 36, snare 38, hat 1 42, hat 2 46, perc 1 39 and perc 2 63, the same order kit patterns, Autofill and the Stolperbeats MIDI export use. Rows 7 to 16 are rim 37, low tom 45, mid tom 47, high tom 50, crash 49, ride 51, pedal hat 44, cowbell 56, tambourine 54 and claves 75 |
| **16 channels** | **16CH** | Row 1 on channel 1, row 2 on channel 2 and so on, all on note 60 (C3). One voice per channel, as Elektron boxes and multitimbral synths expect |
| **Blank** | **BLNK** | Every row on channel 1, note 60, ready to set up yourself |

An MKIT can only be made on an empty clip (the display shows **CANT** otherwise), as notes can't move between a kit and a melodic track. It lights the KIT button, not MIDI, as it's a kit.

### Setting a row's channel and note

- **Hold the row's audition pad and press SELECT:** **CHAN** and **NOTE** are first in the menu. Turn SELECT to change them.
- **Or hold the row's audition pad and turn a gold knob,** as on any MIDI row: one knob changes the channel, the other the note.
- **Or press SELECT with the row selected** for the MIDI row's own menu, which has CHAN and NOTE first too.

### Good to know

- An MKIT is an ordinary kit once it's made: it saves with the song, saves as a kit preset, and takes sample or drum synth rows if you add them.
- Autofill's pitched hits (Climb) shift a MIDI row's note, the same way they pitch a sound row.
- Kit pattern mode covers the bottom six rows, and Autofill the bottom three, as on any kit.

[Back to top](#readme-top)

## 17. CV2 lock

A CV track on both outputs (**CV channel BOTH**) sends pitch on CV 1 and, by default, aftertouch on CV 2. **CV 2 Source** (**CV2**) has a new choice, **LOCK**, where CV 2 follows the gold knobs in semitones:

- Each step of the knob is one semitone, so **12** is one octave (1 V) and **24** two. With the knob at zero CV 2 sits at 0 V.
- **Hold a step and turn a gold knob** to lock CV 2 for that step: an octave jump, a fifth, anything. Steps without a lock play the knob's own value.
- CV 2 is set before the step's gate fires, so a module that reads its pitch on the gate gets the locked value.
- The mono sequencer's **CUSTOM** voltages still work alongside it: holding a row's audition pad and turning the lower gold knob sets that row's CV 1 voltage, as before.

To set it up: open the CV clip's menu, set the channel to **BOTH**, then set **CV 2 Source** to **LOCK**.

[Back to top](#readme-top)

## 18. Elektron P-locks

On the Deluge, holding a step and turning a knob records the new value from that step up to the next note. Notes you add later in that stretch pick it up, a lone note on a row changes the whole row, and deleting the note leaves its value behind. Turn on **Elektron P-locks** and a lock belongs to its step, as on an Elektron:

- A lock runs from its note up to the next note (on the row in a kit, across the clip otherwise), even when it's the only note on the row.
- A new note placed inside a lock plays the unlocked value, and the lock before it stops at the new note.
- Deleting a locked note deletes its lock: the note before it carries on to the next note with its own value.
- Letting go of a held step with the transport stopped puts the unlocked value back on the knobs and the sound.

To turn it on: **SHIFT + press SELECT** to open Settings, go to **Community Features** (**FEAT**) and turn **Elektron P-locks** (**ELEK**) on. It's off by default.

### Good to know

- Locks are still the Deluge's own automation, so songs open on any firmware. Each lock ends one tick before the next note, which keeps the unlocked value in the song; you won't hear the tick.
- The new rules apply to notes you place and delete on the grid. Loading kit patterns, pasting and recording notes live leave locks as the Deluge always has.
- Drawn automation (automation view) is left alone when you add notes. Deleting a note does move a drawn value that starts exactly on that note, as it can't be told apart from a lock. Patch cable amounts aren't covered.

[Back to top](#readme-top)

## 19. Track types in song view

In song view (rows layout), the section pads in the right-hand column keep their section colours and move by what kind of track each row's clip is on:

| Track | Section pad |
|---|---|
| Kit | Flashes bright on every beat |
| Synth | Breathes slowly, over two beats |
| MIDI | Pings bright on the beat and fades, like a sawtooth |
| CV and audio | Solid |

It follows the playhead while playing, and the song's tempo when stopped. It pauses while the VU meter is showing, during MIDI learn, and while a menu is open over song view. Grid view isn't changed. It costs almost nothing: the pads are refreshed about 30 times a second, only when something has changed, and never while the pads' connection is busy.

[Back to top](#readme-top)

## 20. MIDI loop tracks

Use the Deluge as a MIDI looper: play a synth or drum machine on its own keys or pads, the Deluge records it, and the loop plays back to it. The synth's local control stays on, so its panel keeps working as normal.

On the stock Deluge a MIDI track sends everything it receives straight back out on its channel. With local control on, the synth hears your playing twice while you record: once from its own keys, once from the Deluge. LOOP tracks don't send your playing back.

### Setting up

- **Cables:** the synth's MIDI out to the Deluge's MIDI in, the Deluge's MIDI out to the synth's MIDI in. A MIDI merger lets two or more synths share the Deluge's input, each on its own channel.
- **On each synth:** have its MIDI out send only what you play, not pass through what comes in. Set its knobs to send **CC**, not NRPN: the Deluge records CCs, and NRPN knob moves come back as nonsense. On a Prophet '08, that's **Param Xmit** on **CC** and **Param Rcv** on **CC** or **All**.
- **On the Deluge:** turn on [Endless Record](#5-endless-record) (**FEAT > ENDL**), so a loop closes at the next bar.

### Recording a loop

1. In clip view on a new clip, press **SHIFT + MIDI**, turn **SELECT** to **LOOP** and press **SELECT**. The display shows **LOOP**.
2. Launch the clip in song view and press **PLAY**.
3. Play a note on the synth. The track takes that note's channel, in and out, and the display shows **CH** and the channel (**CH2** for channel 2).
4. Hit **RECORD**, play, then hit **RECORD** again. RECORD blinks, the loop closes at the next bar and plays back to the synth.
5. For the next synth, make another LOOP track and play that synth. It takes that synth's channel, as the first one is taken.

### ECHO

Every MIDI track has **ECHO** in its menu, second after Actions:

| Setting | Display | What you play into the track |
|---|---|---|
| **On** | **ON** | Goes back out, as on the stock Deluge. The default for MIDI tracks |
| **Off** | **OFF** | Records, but never goes back out: notes, CCs, pitch bend and aftertouch. LOOP tracks start here |
| **Off while recording** | **REC** | Goes back out, except while recording |

Whatever the track plays back from its clip always goes out.

### Good to know

- A LOOP track only takes a channel nothing else is listening on: not another track's MIDI input, and not a MIDI Follow channel. Only a LOOP track you're looking at, or one that's launched, takes a channel. Learning its input by hand (LEARN + the clip's pad) still works and takes over.
- If another MIDI track already sends on that channel, the LOOP track shares the channel as a second track on it.
- With the arpeggiator on, a track sends its notes out whatever ECHO is set to, as they're the arpeggiator's notes, not yours.
- Clock isn't changed. If the Deluge starts following a synth's clock, turn off the synth's clock out, or the Deluge's receive clock for its MIDI port.
- ECHO and a LOOP track still waiting for its first note save with the song.

[Back to top](#readme-top)

## 21. BRIBERING MODE

A resonator synth engine. Each note strikes a resonator, and the resonator rings on in its own time, the way a bell, a bar or a string does: hit it again and it's struck again, ringing from wherever it was. Its DSP is built on Mutable Instruments Rings, one resonator per Deluge voice, so it plays polyphonically through the Deluge's own envelopes, filters, mod FX, delay, reverb and sidechain.

### Turning it on

1. On a synth track, press the **SYNTH MODE** shortcut pad (or find **Synth mode** in the sound menu). On a kit row, hold the row's audition pad and press SYNTH MODE.
2. Choose a model. They're listed after **303** (straight after Ringmod on a kit row):

| Display | OLED | Model | What it is |
|---|---|---|---|
| **BMOD** | Bribering modal | Modal | A bank of 24 tuned band passes, the partials of a struck object: from harmonic, string-like tones through bars and glass to bells and plates |
| **BSYM** | Bribering sympathetic | Sympathetic strings | A struck string, with more strings tuned around it that ring in sympathy |
| **BSTR** | Bribering string | Inharmonic string | One plucked string, with stiffness and dispersion that pull it out of tune, from clean to buzzy and metallic |
| **BFM** | Bribering FM | FM | A two-operator FM voice with its own strike envelope |
| **BCHD** | Bribering chord | Chord | Sympathetic strings tuned to a chord, which Structure picks |

A new BRIBERING sound starts at the note played (no transpose), with envelope 1 fully open while the note is held and a release long enough for it to ring out after you let go. Moving between the models keeps your knobs, as switching models on Rings does.

### Controls

| Control | Display | Pad (SHIFT + pad) | Gold knob | What it does |
|---|---|---|---|---|
| **Structure** | **STRU** | FM MOD 1 TRANSPOSE (row 2) | CUSTOM 3 | Modal: the partials' spacing, from harmonic to bell and plate. Sympathetic: the intervals the other strings are tuned to. String: dispersion, a curved bridge at the bottom, clean around a quarter, stiff and inharmonic towards the top. FM: the frequency ratio. Chord: which chord |
| **Brightness** | **BRIT** | FM MOD 1 row 3 | CUSTOM 2 | How bright the strike is and how long the high partials last. FM: the modulation depth |
| **Damping** | **DAMP** | FM MOD 1 FEEDBACK (row 6) | Attack / Release (bottom) | How long it rings: a short knock at the bottom, many seconds near the top. From about 121 it fades towards ringing forever, which it does at 127 |
| **Position** | **POSI** | FM MOD 1 RETRIG PHASE (row 5) | Mod depth | Where the resonator is struck and heard from: near the end is bright and full, the middle is hollow and comb-like. FM: feedback |
| **Bow** | **BOW** | FM MOD 2 LEVEL (row 1) | Mod rate | A continuous noise excitation, bowing or blowing the resonator for as long as the note sounds, on top of each strike. 0 is off: struck only |
| **Drive** | **DRIV** | FM MOD 1 LEVEL (row 1) | Attack / Release (top) | A soft clip on the output. 0 is clean |
| **Pitch** | | OSC1 TRANSPOSE (row 2) | CUSTOM 1 (tune) | The Deluge's own transpose and tune |
| **Model** | **MODL** | OSC1 TYPE (row 3) | | **MODA**, **SYMP**, **STRG**, **FM** or **CHRD** |
| **Poly** | **POLY** | FM MOD 2 row 3 | | Sympathetic and chord only: **4** voices or **2** (see below) |

From v1.28 the pads follow the Deluge's own labels, as on any synth: **OSC1 LEVEL** is the level and **OSC1 TRANSPOSE** the pitch, and the resonator is on FM MOD 1. Hold **SHIFT** and they pulse purple.

They're all in the sound menu under **Drum synth**, and in the drum synth pad editor (BRIBERING has its own page: the model, poly, its knobs, then transpose, release and the filters). Every one except Model and Poly is a Deluge parameter, so it can be parameter locked (hold a step and turn), automated, MIDI learned and modulated from the mod matrix: an LFO on Position, an envelope on Brightness, velocity on Structure.

### Poly: strings per voice

Rings shares eight strings between its voices, and BRIBERING MODE does the same on the two string-bank models:

| Poly | Voices | Strings a voice | Sound |
|---|---|---|---|
| **4** (default) | 4 | 2 | Each note is a struck string and one sympathetic string. On Chord, each note plays a two-note chord: an octave down, a 2nd, minor or major 3rd, 4th, 5th, 6th, minor or major 7th, an octave up, or octaves either side |
| **2** | 2 | 4 | Fuller: three sympathetic strings a note. On Chord, each note plays a four-note chord: octaves, 5th, sus4, minor, m7, m9, m11, 6/9, M9, M7 or major |

Poly sets the sound's Max voices to match (4 or 2), so a note past the limit lets the oldest go. The other models play up to the Deluge's usual 8 voices.

### How it plays

- **Strike and ring:** every note on strikes the resonator, the way Rings' internal exciter does when it's strummed. The resonator then rings with its own decay (Damping), inside the Deluge's envelope.
- **Velocity** sets the level through the Deluge's usual velocity cable. Patch it to Brightness or Structure as well for a strike that changes with how hard you play.
- **Legato and portamento:** in Legato mode a new note retunes the ringing resonator without striking it again.
- **Bow** keeps a note sounding for as long as you hold it, so the Deluge's envelope shapes it like any synth: pads, drones, bowed metal.
- **A note ends** once its resonator has died away to silence, even with the key still held (unless Bow is up), so long chords of short notes don't keep using CPU.

### Good to know

- **CPU:** Modal and String are the lightest models and FM the heaviest; all three play up to 8 voices. Sympathetic and Chord are held to 4 or 2 voices by Poly, so they can't run away with the CPU. In a busy song, watch the LOAD menu if you hold big FM chords.
- On a kit row it plays at the row's note (C3), for tuned percussion, bells and plucks in a kit.
- The lowest a string goes is about 21.5 Hz, so on notes below about F1 the octave-down string of a chord stops at that.
- Rings' stereo outputs and its reverb model aren't used: the voice is mono into the Deluge's stereo, and the Deluge's own reverb is there instead.
- Songs and presets save the model, Poly and every knob. Bribes firmware from before v1.25 loads the sound on its last drum engine (ULTRAKIK from v1.21) instead.

[Back to top](#readme-top)

## 22. Feedback

**Feedback** (**FDBK**) feeds a synth voice's filter output back into the filter's input, like patching a mono synth's output back into its own mixer. A little thickens and warms the sound; more drives the filter, fattening and saturating the low end. Every voice has its own loop, so each note of a chord feeds back on itself only.

### Where it is

- **SHIFT + the shortcut pad directly below FOLD.**
- In the sound menu under **Distortion**, after **Wavefold**.
- In automation view, as a patch cable destination (an envelope, LFO or velocity on Feedback), and on a gold knob with LEARN.

### How it plays

- **0 is off**, and costs no CPU. The knob is gentle through its lower half and strongest at the top, where it adds about 4.5 dB of saturated low end.
- **Around the filter:** the loop goes around the low pass filter. With the LPF off it goes around the high pass filter, and with both off, around the voice itself. Resonance and Feedback together growl.
- **It can't run away from the knob alone:** the fed-back signal is soft clipped, and its DC and deepest sub (below about 55 Hz) are taken out. Patch cables can push it past the knob's range, into self-oscillation: a tone that rings for as long as the note is held.
- **Each note starts clean:** a voice's loop starts silent and stops with the note.
- It works on subtractive, wavetable, FM, ring mod and BRIBERING MODE synths, and on kit rows.
- Songs and presets save it (`voiceFeedback`). Anything saved before loads with Feedback off.

[Back to top](#readme-top)

## 23. Crush types

The Deluge's own Bitcrush and Decimation sound more like filters than crushers. Decimation draws a line from each sample it keeps to the next, which smooths the top end away instead of aliasing. Bitcrush jumps through eight steps, adds a DC offset and drops the volume near the top. **Crush type** sets how both of them sound: four types that hold each sample flat and sweep smoothly, one that breaks the sound another way (a dying BBD chip), and the original kept as Classic.

### Where it is

- **FX > DISTORTION > Crush type** (**CTYP**), after **Bitcrush** (**CRUSH**) and **Decimation**, on any synth, kit row or audio clip.
- For a whole kit, turn **Affect Entire** on first: the kit's own **FX > DISTORTION** menu has it too. For the song, press **SELECT** in song view, then **FX > DISTORTION**.
- Hold **Affect Entire** while turning it in a kit row's menu to set every row at once.

The type only changes the sound once **Bitcrush** or **Decimation** is turned up.

| Type | 7-seg | Bitcrush | Decimation |
|---|---|---|---|
| **Hard** | **HARD** | The default. Clean digital steps from 12 bits down to 1; at the end quiet parts drop out. | Sample and hold: bright, metallic aliasing. Around 5 kHz at the middle of the knob, down to 172 Hz. |
| **Vintage** | **VINT** | An old 12-bit sampler: 12 bits as soon as either control is on, down to 3, with a softly rounded input. | The clock starts around 26 kHz and goes down to about 580 Hz, with the steps a little softened. |
| **u-Law** | **ULAW** | Companded: every octave of level gets the same number of steps, so quiet tails stay grainy instead of dropping out. The top of the knob gets properly broken. | As Hard. |
| **Jitter** | **JITR** | A noisy threshold: crackles and sputters. | The clock wobbles by up to half a sample period each time: noisy and broken rather than tonal. |
| **Decay** | **DECY** | A dying BBD chip: grit that rides the level, pushed around by the sound's own 1 kHz band, then irregular sputters, stutter bursts and flickering sags in the level. More of all of it, more often, as you turn up. | A BBD clock instead of a sampler: 1x down to 32x (about 1.4 kHz), smoothed after, so it goes dark and woolly with only a little aliasing. |
| **Classic** | **CLAS** | The original. | The original. |

### Good to know

- The level stays put as you turn either control up, with no DC offset. Jitter gets a little louder at the top.
- Decay keeps silence silent: nothing is left once the sound has stopped.
- Decay's sputters run on their own random timing, not synced to the tempo.
- New sounds, kits, audio clips and songs start on **Hard**. Songs and presets from the stock firmware, or saved before v1.27, load as **Classic**, so they sound the same, even where Bitcrush or Decimation only comes up later from a knob or automation.
- The **Data** type (v1.37 to v1.39.2) was removed in v1.39.3. Songs and presets saved with it load as **Hard**: Decimation sounds the same, and Bitcrush becomes Hard's bit depth.
- Bitcrush and Decimation are still parameters: gold knobs, automation, MIDI learn and parameter locks work as before, and the type changes how they sound.
- Songs and presets save it (`crushType`). Other firmware ignores it and plays the original.
- It costs a few operations per sample, only while Bitcrush or Decimation is on.

[Back to top](#readme-top)

## 24. BROPHET

A two-oscillator polyphonic synth engine: the voice of Pro-54, Cmajor's open source port of Native Instruments' Pro-53, which emulates the Sequential Prophet-5. Each Deluge voice is one of its voices, so it plays through the Deluge's own envelopes, LFOs, mod matrix, FX and unison, and its filter is in every LPF list.

### Turning it on

- **SHIFT + SYNTH**, then **BROPHET**, then a bank (**BNK1** to **BNK8**, or **BRIB**), then turn SELECT to play through the presets. See [Synth browser](#13-synth-browser).
- Or press the **SYNTH MODE** pad on any synth (or hold a kit row's audition pad and press it) and choose **BROPHET**, after the BRIBERING models. A new BROPHET sound gets the Brophet filter, envelope 2 on its cutoff, and an envelope that holds while the key is down.

### Controls

The pads follow the Deluge's own labels: osc A on OSC1, osc B on OSC2, and only what has no pad of its own on FM MOD 1 and 2. Hold **SHIFT** and they pulse purple.

| Control | Display | Pad (SHIFT + pad) | Gold knob | What it does |
|---|---|---|---|---|
| **Osc A wave** | **AWAV** | OSC1 TYPE | | **SAW**, **PULS** or **SAPU** (both) |
| **Osc A pulse width** | **APW** | OSC1 PULSE WIDTH | CUSTOM 3 | |
| **Osc A level** | **ALVL** | OSC1 LEVEL | | Osc A in the mixer |
| **Pitch** | | OSC1 TRANSPOSE | | The Deluge's own transpose: osc A, and osc B with it while it's on the keys |
| **Noise** | **NOIS** | OSC1 NOISE | | Noise in the mixer |
| **Osc B wave** | **BWAV** | OSC2 TYPE | | **SAW**, **TRIA**, **PULS**, or two or all three together: **SATR**, **SAPU**, **TRPU**, **ALL** |
| **Osc B frequency** | **BFRQ** | OSC2 TRANSPOSE | | In semitones against osc A, two octaves either way (64 is unison). Off the keys, four octaves either side of middle C |
| **Osc B pulse width** | **BPW** | OSC2 PULSE WIDTH | | |
| **Osc B level** | **BLVL** | OSC2 LEVEL | | Osc B in the mixer |
| **Sync** | **SYNC** | OSC2 SYNC | | Osc A restarts with every cycle of osc B |
| **Poly mod osc B** | **PMOB** | FM MOD 1 LEVEL | | Osc B modulating osc A at audio rate: growls, clangs and bells |
| **Osc B fine** | **BFIN** | FM MOD 1 TRANSPOSE | CUSTOM 2 | About half a semitone either way |
| **Osc B low** | **BLOW** | FM MOD 1 row 3 | | Drops osc B about 91 semitones, into LFO range, for poly mod and sync |
| **Osc B keyboard** | **BKEY** | FM MOD 1 row 4 | | **ON**: osc B follows the keys. **OFF**: it stays put, around middle C |
| **Poly mod env** | **PMEN** | FM MOD 2 LEVEL | | Envelope 2 sweeping osc A: with Sync on, the classic sync sweep |
| **Analog** | **ANLG** | FM MOD 2 TRANSPOSE | | Each note's random drift: osc A and B detune a little differently every note, and the poly mod depth with them. About a cent at the default, up to about a quarter tone at the top |
| **Poly mod dest** | **PMDS** | FM MOD 2 DESTINATION | | What poly mod moves: **FRQA** (osc A's pitch), **PWA** (its pulse width) or **BOTH** |

The Attack and Release gold knobs stay on envelope 1, and Mod rate and Mod depth are the Deluge's vibrato (LFO 1's rate, and LFO 1 to pitch), as on any synth. Every control except the waves and switches is a Deluge parameter, so it can be parameter locked, automated, MIDI learned and patched from the mod matrix. They're also in the sound menu under **Drum synth** and on BROPHET's page of the drum synth pad editor.

### The Brophet filter

**Brophet** (**BROPHET** on the 7-segment display) is an LPF type, after **Drive** in every LPF list: synths, kit rows, audio clips and the song. It's Pro-53's original filter: two state variable stages, 24 dB, with the output soft-clipped and fed back.

- **Resonance** self-oscillates near the top. As on the original, turning it up thins the bass and the level (about 10 dB down at half way) and lifts the cutoff a little.
- **LPF MORPH** is its drive: up to 30 dB into a soft clipper before the filter, which pushes the filter's own clipper too. A saw at full drive comes out about 4 dB louder than clean.
- On BROPHET, envelope 2 is both the filter envelope (through its cable to the cutoff) and the poly mod envelope, as on the original.

### The presets

- **BNK1** to **BNK8** hold all 512 of Pro-53's programs, 64 each. Each is named by its Pro-53 number: **411 Brass** is file 4, bank 1, program 1. **BNK4** to **BNK6** are the classic programs (Brass, Low Strings, Harpsichord, Sync II, Clangorous Bells and the rest); the other banks are Native Instruments' own sounds.
- **BRIB** holds 24 presets made for this build.
- The programs come from the preset bank Pro-54 ships. The oscillator, mixer and poly mod settings carry over exactly, since it's the same voice. The filter, envelopes, glide, LFO and delay were worked out again through the Deluge's own scales, so cutoffs land at the same frequency at middle C and envelopes take the same time.
- Some things can't carry over exactly:
  - **Mod wheel:** a Deluge cable can't start from nothing with the wheel down, so a program saved with the wheel up gets its LFO fixed at that depth, and the others leave the LFO off.
  - **Poly mod to the filter:** its envelope part is added to the filter envelope, but osc B can't sweep the filter at audio rate.
  - **Glide** is only set on unison programs: Pro-53 glides in unison only, so a poly program's glide was never heard.
  - **Delay** is the Deluge's own, at Pro-53's time (23 ms at the shortest), wet level as the amount and feedback as the feedback.
  - **Velocity** is off, as on a Prophet-5, unless the program turns it on.
- **v1.35:** the 85 presets with vibrato (LFO to pitch) now have it at the original's depth (before, they had almost none). Copy them over the old ones.

### Good to know

- **CPU:** about 5.8% of the Deluge a voice (around 1300 ns on LOAD's **VNS**), about twice a stock voice. An 8-note chord fits with room for the rest of a song; two busy BROPHET tracks plus a full song will start cutting voices.
- On a kit row it plays at the row's note.
- The companion shows BROPHET as a panel of knobs, both ways (see [BROPHET panel](#brophet-panel)).
- Songs and presets save every setting. Bribes firmware from before v1.28 doesn't know BROPHET.

[Back to top](#readme-top)

## 25. Pan spread

**Pan spread** spreads a poly synth's notes across the stereo field: every new note takes its own place, left or right, and keeps it until it ends. A chord fans out and an arpeggio moves across the speakers, as with the voice pan spread on a poly synth like the Prophet '08. It works on single voices, so it doesn't need unison (unison's own Spread still spreads each note's unison copies, and the two work together).

### Where it is

- **SHIFT + PAN pad, press again.** The pad blinks yellow and opens **PAN SPREAD**. Press **SELECT** to go on to **SPREAD MODE**.
- In the sound menu under **Voice**, after **Portamento**: **Pan spread** (**PAN SPREAD**, 0 to 50) and **Spread mode** (**SPREAD MODE**).
- Hold **AFFECT ENTIRE** to set every row of a kit.

### Spread modes

| Mode | Display | Where each new note goes |
|---|---|---|
| **Alternate** | **ALT** | Eight fixed places, taken in turn: the outer pair first, then the inner ones, always swapping sides. Two notes go wide, bigger chords fill in |
| **Key** | **KEY** | By pitch: low notes left, high notes right, middle C in the centre, the edges two and a half octaves out |
| **Random** | **RAND** | Anywhere, picked fresh for each note |
| **Ping pong** | **PING** | Left, right, left, right. The amount sets how far out: near the centre at low values, hard left and right at 50 |

### How it plays

- **0 is off**: the sound pans as before, with no extra CPU.
- **PAN still moves the whole spread**, left or right.
- **Turning Pan spread moves held notes too:** each note keeps its place and the amount scales how far out that is.
- **Poly sounds only:** Mono and Legato have one voice, so the setting is hidden there. The 303 is always mono.
- It works on subtractive, wavetable, FM, ring mod, BRINGS, BROPHET and BRUNO106 synths, and on kit rows.
- **CPU:** each voice pans itself instead of the whole sound being panned once, which costs a couple of multiplies per sample per voice.
- Songs and presets save it (`voiceSpread`). Anything saved before loads with it off.

[Back to top](#readme-top)

## 26. BRUNO106

A Juno-style polyphonic synth engine: the voice of Ultramaster KR-106, Karl LaRocca's open source emulation of the Roland Juno-106, calibrated from real hardware. Each Deluge voice is one DCO: saw, pulse with its width, the sub an octave down and noise, with the Juno-106's own levels and slider curves. It plays through the Deluge's envelopes, LFOs, mod matrix, FX and unison. Its IR3109 filter is in every LPF list, its four position HPF runs on the track, and its BBD chorus is a Mod FX type any track can use.

### Turning it on

- **SHIFT + SYNTH**, then **BRUNO106**, then **BASS**, **LEAD**, **PAD** or **MISC**, then turn SELECT to play through the presets. See [Synth browser](#13-synth-browser).
- Or press the **SYNTH MODE** pad on any synth (or hold a kit row's audition pad and press it) and choose **BRUNO106**, after **BROPHET**. A new BRUNO106 sound gets the Bruno106 filter, envelope 2 on its cutoff, and an envelope that holds while the key is down.

### Controls

The pads follow the Deluge's own labels: the DCO on OSC1, its pulse and sub on OSC2, and the HPF and chorus on FM MOD 1. Hold **SHIFT** and they pulse purple.

| Control | Display | Pad (SHIFT + pad) | Gold knob | What it does |
|---|---|---|---|---|
| **Saw** | **SAW** | OSC1 TYPE | | Saw on or off |
| **Pulse width** | **PW** | OSC1 or OSC2 PULSE WIDTH | CUSTOM 3 | 0 is a square, up to a narrow 95% pulse. Patch LFO 1 or an envelope to it for PWM |
| **Level** | | OSC1 LEVEL | | The Deluge's own oscillator level |
| **Pitch** | | OSC1 TRANSPOSE | | The Deluge's own transpose: 12 down for the Juno's 16', 12 up for 4' |
| **Noise** | **NOIS** | OSC1 NOISE | | Noise level, on the Juno-106's slider curve |
| **Sub level** | **SUB** | OSC2 LEVEL | CUSTOM 2 | The square sub an octave down, a little louder than the saw at the top |
| **Pulse** | **PULS** | OSC2 TYPE | | Pulse on or off |
| **HPF** | **HPF** | FM MOD 1 LEVEL | | The Juno-106's slider: **BOST** (bass boost), **FLAT**, **236** or **754** Hz |
| **Chorus** | **CHOR** | FM MOD 1 TRANSPOSE | | BRUNO CHORUS on or off. Each SHIFT + pad press flips it |
| **Chorus mode** | **CMOD** | FM MOD 1 row 3 | | **I**, **II** or **I-II**, while the chorus is on |
| **Slop** | **SLOP** | FM MOD 2 TRANSPOSE | | How much each note differs from the last, as the parts of a real voice do: tuning (about 12 cents at the top), the pulse width's range and the level |

The Attack and Release gold knobs stay on envelope 1, and Mod rate and Mod depth are the Deluge's vibrato (LFO 1's rate, and LFO 1 to pitch), as on any synth. One LFO for vibrato and PWM is how the Juno does it too. Every control except the switches is a Deluge parameter, so it can be parameter locked, automated, MIDI learned and patched from the mod matrix. They're also in the sound menu under **Drum synth** and on BRUNO106's page of the drum synth pad editor.

### The Bruno106 filter

**Bruno106** (**BRUNO106** on the 7-segment display) is an LPF type, after **Brophet** in every LPF list: synths, kit rows, audio clips and the song. It's KR-106's model of the Juno-106's IR3109: four poles with the BA662 feeding the output back, on the Juno-106's resonance curve.

- **Resonance** comes in the Juno-106 way and self-oscillates near the top, at the cutoff's pitch.
- **LPF MORPH** is its drive: up to 18 dB into the filter's OTAs, 12 dB of it taken back off after.
- The four stages run clean and the feedback stage carries the saturation, so it holds the voice's CPU at BROPHET's.

### HPF

The Juno-106's high pass slider, once per track on all its voices together, before the Mod FX, as on the hardware.

- **BOST** is the bass boost: a shelf of about +10 dB at the very bottom, easing off above 100 Hz.
- **FLAT** is off, and costs nothing.
- **236** and **754** cut below those frequencies, gently (6 dB an octave), for thinner pads and leads.
- Moving between positions fades over 1.5 ms, so it doesn't click.

### BRUNO CHORUS

The Juno's two-line BBD chorus, as a **Mod FX** type (**BRUNO CHORUS**) on any track: synths, kit rows, kits and the song. Pick it in the MOD FX menu, or with the chorus pad on BRUNO106.

- With it picked, **Chorus mode** (**CMOD**) appears in the MOD FX menu: **I**, a slow wide sweep; **II**, faster and a little shallower; **I-II**, a fast shallow vibrato. Rates and depths are KR-106's, measured on hardware.
- Changing mode fades out and back in over 5 ms. The Deluge's MOD FX rate, depth, feedback and offset aren't used: as on the Juno, the mode sets them.
- From v1.34 the [companion's BRUNO106 panel](#bruno106-panel) adds a chorus **Rate** (a quarter to four times the mode's own) and **Depth** (none to twice the mode's). The middle of each is the mode's own, so older sounds play exactly as before. Songs and presets save them (`brunoChorusRate`, `brunoChorusDepth`) only once moved.
- It keeps a stereo track stereo: each delay line takes its own side.
- It runs once per track, not per voice. Songs and presets save the mode (`brunoChorusMode`).

### The presets

212 presets in `LEAD`, `BASS`, `PAD` and `MISC`:

- **13 made for this build:** basses with the bass boost, PWM leads, chorused strings and pads, brass, organ and a couple of effects.
- **199 converted from KR-106's preset data** (GPL-3.0): the factory bank and David Churcher's patch library, which KR-106 ships. They use KR-106's own curves for cutoff, envelopes, LFO, pulse width, sub and noise. Bank numbers are dropped from the names. Each plays with BRUNO CHORUS as the original's chorus switches set it, no velocity, and six voices. LFO delay has no equivalent here, so delayed vibrato starts straight away, and the longest releases stop at about 4.9 seconds. A few effects patches play only the filter ringing at full resonance. Credits in [`presets/SYNTHS/BRUNO106/CREDITS.txt`](presets/SYNTHS/BRUNO106/CREDITS.txt).
- **v1.34:** the 34 converted presets with DCO vibrato now have it at the original's depth (before, they had almost none). Copy them over the old ones.

### Good to know

- **CPU:** about the same as BROPHET a voice: around 1300 ns on LOAD's **VNS** with an 8-note chord held. It reads higher with one or two notes and while an envelope sweeps the filter, as the Deluge's fixed costs per buffer weigh more then.
- On a kit row it plays at the row's note.
- Songs and presets save every setting. Bribes firmware from before v1.31 doesn't know BRUNO106 or BRUNO CHORUS.

[Back to top](#readme-top)

## 27. BRIBELUGE COMPANION

A second screen for the Deluge on a phone or tablet, over USB. It runs in the browser: **[thisisbribery.com/bribeluge/companion](https://www.thisisbribery.com/bribeluge/companion/)** (source: [thisisbribery/bribes-companion](https://github.com/thisisbribery/bribes-companion)).

It talks plain USB MIDI. The display mirror is the Deluge Community firmware's screen-over-SysEx feature (started by bfredl), and STOCK mode's knobs are the community firmware's MIDI Follow; Bribeluge adds its own SysEx messages under the same header. Credits and the full message list are on the [companion page](https://www.thisisbribery.com/bribeluge/companion/#credits).

### What it shows

- **Top bar:** Play, Record, the tempo, the Deluge's display mirrored (7SEG or OLED, switchable), Back, the select knob left and right, and a big SELECT button.
- **Readout:** whatever the display shows, spelled out in full English (no four letter abbreviations), with a menu item's name and value side by side.
- **Track:** a drawing of the engine, the main settings as knobs (greyed out where the Deluge would say **CANT**), and each engine's own controls and switches: a drum engine's controls, the 303's knobs and filter. They work both ways (new in v1.41): drag a knob up or down with a finger or the mouse and the Deluge follows, as if you'd turned it there; turn it on the Deluge and the knob moves. Tap a knob without dragging and it opens on the Deluge, as before. Tap a switch to step it to its next setting. Every engine gets its own panel (below, and [Engine panels](#33-engine-panels)).
- **Gold knobs:** the two knobs of each of the eight mod buttons, with the lit pair glowing. Drag one to turn it (new in v1.41): if its mod button isn't lit, the Deluge lights it first, as only the lit pair turns. It goes through the Deluge's own knob, so the value popup, affect all on a kit and holding notes for parameter locks work as with your hand on it. A knob on a patch cable covers its whole range, -50 to +50. Tap a pair to light its mod button.
- **Kits:** every row's engine, and a list of the kit's sample rows that light as they play. Tap one to open its sample's waveform.
- **Pickers and browsers:** SHIFT + SYNTH and SHIFT + KIT as picture tiles, preset folders as a scrollable list. Tap to choose, tap again to load.
- **Follows the Deluge:** the screen goes where the Deluge goes, so there's nothing to scroll to find. A menu, SHIFT + SYNTH, SHIFT + KIT, a browser, a waveform or the song view opens at the top with its selection in view. Choose a new kit or synth, or change track, and the page centres on its main panel, ready to play. Back out of a menu without changing anything and you're where you left off. Open a setting on the Deluge and its knob scrolls into view.
- **NAV:** a column down the left side lists the sections the track shows: TOP, PANEL (the engine panel), GOLD, ENGINE (the engine's own controls), OSC, FILTER, ENV 1, ENV 2, VOICE, FX and LFO, plus ROWS and SAMPLES on a kit. Tap one and the page glides to it, centred. The section in view stays lit as you scroll, and while a menu or browser is up on the Deluge it's listed on top.
- **Menus (new in v1.48):** whenever a menu is open on the Deluge (SELECT in a clip, the song menu, SHIFT + SELECT settings), the companion shows it whole page: every open level side by side as columns, like a file browser. Tap any entry at any level and the Deluge goes straight there (it goes back up to that level, turns to the entry and presses SELECT, faster than you can on the select knob), and the NAV column lists the menu's top level so any section is one tap away. A setting being edited gets its own column with its value large, **-10**, **-**, **+** and **+10**, and its choices as tiles when it has named ones. **Back** and **Close menu** sit at the top. When the menu closes, the companion goes back to what it showed before. A single setting opened from a shortcut pad (or by tapping a knob on the companion) doesn't take over the page.
- **Waveforms:** audio clips, sample markers and Start offset, full width with every playing note's playhead. Drag the start, loop and end markers, or the offset.
- **Song:** rows view and grid view in the pads' order, each clip with its steps, playhead, the pads' colours and the section pads' glow by track type. Tap a clip or a section to launch it. The arranger shows the same stretch of the song as the pads, with the playhead.

### BRUNO106 panel

With a BRUNO106 synth or kit row selected, the companion shows a panel of sliders, switches and buttons laid out left to right like the synth BRUNO106 comes from. It works both ways: drag a slider and the Deluge follows, as if you'd turned its knob (automation recording, an open menu and the gold knob lights follow too); turn a knob on the Deluge and the slider moves.

- **First row:** **LFO** rate. **DCO** range (16', 8', 4'), LFO (vibrato, up to 4 semitones), PWM with its LFO / MAN switch, pulse and saw, sub, noise and Slop. **HPF** (bass boost, flat, 236 Hz, 754 Hz). **VCF** frequency, resonance, envelope polarity, envelope amount, LFO and keyboard follow. **VCA** ENV / GATE and level. **ENV 1**, the amp envelope.
- **Second row:** **ENV 2**, the filter envelope. **Chorus** I and II (both for I+II), Rate and Depth. **Drive** (the Bruno106 filter's drive), Crush, Deci and Sat. **Delay** amount, rate and feedback. **Reverb** amount.
- Sliders move with your finger from where they sit, so touching one doesn't make it jump. Several fingers can move several sliders at once.
- PWM on LFO works as on the original: the LFO sweeps the pulse width between square and the slider. GATE sets envelope 1 to an organ gate; ENV gives it envelope 2's shape back.
- On a phone or a narrow tablet the columns narrow so each row fits; on a short screen the sliders get shorter.

### BROPHET panel

With a BROPHET synth or kit row selected, the companion shows a panel of knobs and LED buttons in the order of the synth BROPHET comes from, left to right. It works both ways like the BRUNO106 panel: drag a knob up or down and the Deluge follows as if you'd turned its knob; turn a knob on the Deluge and the panel's knob moves.

- **First row:** **Poly-mod** filter envelope and osc B amounts, to Freq A and / or PW A. **LFO** rate, saw / triangle / square, amount to Freq and to Filter. **Osc A** frequency (semitones), saw and pulse, pulse width, Sync.
- **Second row:** **Osc B** frequency, fine, saw / triangle / pulse, pulse width, LO and KBD. **Mixer** osc A, osc B and noise. **Filter** cutoff, resonance, envelope amount, keyboard follow and drive.
- **Third row:** **Filter env** and **Amp env** (A, D, S, R). **Master** glide, analog and volume.
- **Fourth row:** **Dirt** (crush, deci, sat), **Delay** (amount, rate, feedback) and **Reverb**.
- Buttons follow the synth's rules: an oscillator keeps at least one wave on, and the LFO shapes pick one. Osc B's frequency reads two octaves each way on the keyboard and four with KBD off.
- Two looks, from the faint **P5 | P8** switch in the panel's header: **P8** (black panel, red LEDs, silver-capped knobs) or **P5** (wood cheeks, cream lettering and buttons). The tablet remembers which.

### WAVE panel

With a synth whose oscillator 1 or 2 plays a wavetable selected (any WAVE preset, or your own), the companion shows the table itself, like a wavetable synth's display, with the settings that move through it beside it. It works both ways, like the other panels.

- **The table:** its frames drawn as a stack going back, the first at the front. The bright blue frame is where the position knob sits; each note playing is an orange line moving through the stack, with everything patched to the position (envelope 2, LFO 1, velocity) included, and a tick on the rail at the side so you can follow it. Osc B gets its own view when it plays a wavetable.
- **Drag up or down on a table** to move its position, as with the knob. **3D / 2D** in its corner switches to one flat cycle, the knob's frame large with the notes over it.
- **Beside it:** **Osc A** and **Osc B** position, envelope 2 and LFO 1 amounts on the position (centre is none, either way from there), level and pitch.
- **Underneath:** **LFO 1** rate, **Env 2** (the one that sweeps the position on the WAVE presets), **Filter** cutoff and resonance, **Amp env**, **Tone** (wavefolder and [Feedback](#22-feedback)) and **Out** (volume and reverb).
- The Deluge sends a table once, a little at a time, when it's loaded or the panel opens (about a quarter of a second for a big one), then only the positions while they move.

### Engine panels

TRIBE, CYC, LXR and GIN kit rows (and synths in those SYNTH MODEs) each get a panel of their own, new in v1.44, and from v1.47 so do ULTRAKIK, XIA, BRIBERING, the 303, DX7 and the Deluge's own SUBTRACTIVE, FM and RINGMOD. From v1.45, touching a control on any panel lights the mod button whose gold knobs turn it, and **SHORTCUT** opens its setting on the Deluge. See [Engine panels](#33-engine-panels).

### Using it

1. Connect the phone or tablet to the Deluge's USB port (with a USB-C or OTG cable).
2. Open the page in Chrome and allow MIDI when asked. It finds the Deluge by itself.
3. Optional: Chrome's menu > **Add to Home screen**. It then opens fullscreen from its icon, works offline, keeps the screen awake and reconnects on its own.

### Good to know

- It needs a browser with Web MIDI: Chrome or Edge on Android, Windows, macOS or Linux. Safari, and every browser on iPhone and iPad, doesn't have it.
- The Deluge only sends the companion's messages while a companion is connected, and DEx and other editors keep working alongside it.
- To charge a tablet while it's connected you need a USB-C hub with Power Delivery pass-through; not every tablet charges while it powers a USB device.

[Back to top](#readme-top)

## 28. Master clip

The very end of the song: a clipper or limiter after the master compressor, just before the output. Without it, anything over full scale hits the Deluge's plain digital clip, which is harsh. With it, the output stops at the ceiling with the curve you pick, and **Clip drive** pushes the mix into it for more density and loudness.

### Where it is

Press **SELECT** in song view, then **MASTER**, after Volume and Pan:

- **Master clip** (**MASTER CLIP**): **Off**, **Soft**, **Tanh**, **Hard**, **Tape**, **Fold** or **Limit**.
- **Clip drive** (**CLIP DRIVE**): 0 to +24 dB into it.
- **Ceiling** (**CEILING**): where the output stops, -12 to 0 dB. -1 to start.

Drive and Ceiling appear once a type is picked.

| Type | 7-seg | Sound |
|---|---|---|
| **Soft** | **SOFT** | Clean to 80% of the ceiling, then a cubic knee into it. The most transparent curve. |
| **Tanh** | **TANH** | Clean to 70%, then a tanh shoulder: the classic warm clip. |
| **Hard** | **HARD** | Straight up to the ceiling and flat. Loud and bright. |
| **Tape** | **TAPE** | Bends from halfway, rounder and earlier: saturated, a little squashed. |
| **Fold** | **FOLD** | Folds back down from the ceiling instead of flattening: drive it for metallic, synthy distortion on the whole mix. |
| **Limit** | **LIMT** | A peak limiter with 0.7 ms lookahead instead of a curve: it turns the peaks down just ahead of time, so the mix gets louder with drive without the clip's distortion. A hard clip at the ceiling after it catches what little gets through. |

### Good to know

- The curves run at twice the sample rate, so the clipping's top harmonics don't fold back down as noise: about 14 dB less of it than a plain clip on a hard driven tone.
- Every type adds the same 1.2 ms of latency, so switching between types while it plays is seamless. Turning it on or off crossfades over 12 ms, with no click.
- **Off** touches nothing and adds no latency. Songs from before v1.37 load with it Off, so they sound the same.
- It's on the output, so resampling and stem export (with song FX) record it too.
- Songs save it (`masterClip`, `masterClipDrive`, `masterClipCeiling`), only when it isn't Off. Other firmware ignores it.
- It costs a few percent of the CPU while on, and nothing while Off.

[Back to top](#readme-top)

## 29. SHIFT

A three-band frequency shifter as a **Mod FX** type (**SHIFT**). It splits the sound at 250 Hz and 2.5 kHz and moves every frequency in each band by its own number of hertz. A pitch shift keeps a sound's harmonics in tune with each other; a frequency shift doesn't, so a little makes things wobble and detune, and more turns them clangorous, metallic and inharmonic. Past 0 Hz frequencies fold back up.

On synths, kit rows, kits, audio clips and the song: pick **SHIFT** in the **MOD FX** menu.

| Control | 7-seg | What it does |
|---|---|---|
| **Depth** (shown as **Shift amount**) | **SHIFT AMOUNT** | How far each band moves. At 0 it's off; the shifted sound comes in over the first quarter of the knob and the shift keeps growing to the top. |
| **Rate** | **RATE** | Glide: how long a change of amount takes to arrive, 30 ms to 2.4 s. Slow it down and sweep Depth for falling and rising smears. |
| **Feedback** | **FEEDBACK** | Sends the output back in through 30 ms, so each pass is shifted again: spiralling barber pole sounds. It comes in with Depth and is level-compensated. |
| **Offset** (shown as **Shift morph**) | **SHIFT MORPH** | Morphs between two sets of band shifts. Set A: low +90, mid -300, high -1500 Hz. Set B: low -190, mid +900, high +2500 Hz. |

### Good to know

- Depth is a normal Mod FX parameter: gold knob, automation, patch cables and parameter locks all work.
- In stereo the right side's shift runs a quarter turn ahead of the left, so a mono sound spreads out as it moves.
- It runs once per track, not per voice, but costs more than the other Mod FX types (a few percent of the CPU each): use it on a handful of tracks, or the kit or song.
- Each track with it on uses about 17 kB of memory, freed when you pick another type.
- Songs and presets save it (`modFXType` = `freqShift`). Other firmware loads it as no Mod FX.

[Back to top](#readme-top)

## 30. TRIBE

An 808 / 909 drum machine as a drum synth engine: eight voices (kick, snare, clap, rim, tom, hat, cymbal and cowbell), each with an **808 > 909** knob that runs smoothly from the way the 808 makes that sound to the way the 909 makes it. The kick goes from the 808's boom to the 909's swept VCO and click on one knob, with no engine change. Every other knob is centred on the real machine: at 64 it does what the 808 or 909 (or the blend the 808 > 909 knob points at) does, and turning it down or up goes past what either machine could. All synthesised, no samples, the 909's hats and cymbals included.

Both ends of every voice are fitted to recordings of a real 808 and a real 909 at known knob settings: their envelope, their spectrum over time and their pitch. On top sit extras after Hexinverter's Mutant drums: the BD9's wave switch and square sub on the kick, and the Mutant Snare's snappy resonance.

### Getting it going

- **A kit:** in clip view on an empty clip, press **SHIFT + KIT** and pick **TRIBE** (**TRIBE**). Eight rows, from the bottom: **KICK**, **SNARE**, **CH**, **OH**, **RIM**, **TOM**, **CLAP**, **CYM**. The two hats choke each other and the kick feeds the sidechain. With [Gate out](#15-gate-out) the kick, snare and hats fire gates 1 to 4.
- **Kits:** turn **SELECT** in the clip (or **SHIFT + KIT** for the list) to step through the eleven kits built in. Your own TRIBE kits saved to `KITS/TRIBE` come after them.
- **One voice on any row:** **SYNTH MODE** has **TRIBE KICK**, **SNARE**, **HAT**, **RIM**, **TOM**, **CLAP**, **CYMBAL** and **COWBELL**. Each starts as it sits in the TRIBE kit. On a synth track a TRIBE voice plays at the note, so the kick and tom play bass lines.
- **Every new kit track:** set **Defaults > Clip type > Kit** to TRIBE (see [Instrument Picker](#14-instrument-picker)).
- TRIBE rows are tinted red.

### The knobs

The same knobs and pads as the Cyc engines. **Gold knobs:** Custom 2 is **808 > 909**, Custom 3 is **Tone**, mod depth / mod rate are **Sweep** / **Sweep time**, attack / release are **Drive** / **Decay**. All twelve are parameters: lockable, automatable and patchable.

| Knob | Pad | What it does |
|---|---|---|
| **808 > 909** | MOD1, row 6 | 0 is the 808, 127 the 909, everything between a clean blend. The level stays put as you turn it, so it's safe to automate |
| **Tone** | MOD1, row 7 | Brightness. Kick: below 64 a softer click and a purer sine, above 64 the wave goes triangle then square (the BD9's WAVE switch). Snare: the 808's head balance, the 909's snappy brightness. Cymbal: low band against high |
| **Sweep** | MOD1, row 4 | Pitch drop depth (clap: spacing between bursts) |
| **Sweep time** | MOD1, row 5 | How long the drop takes, the 909's TUNE (clap: number of bursts, 1 to 8) |
| **Drive** | MOD1, row 2 | Soft clip after the envelopes |
| **Attack** | MOD1, row 8 | The transient: click, stick or pulse. Velocity drives it too |
| **Noise** | MOD2, row 1 | The noise layer: snappy on the snare, skin on the tom, sizzle on the hats, tail on the clap, clang on the cowbell. Kick: **Sub**, a square sub oscillator, off at 0 |
| **Noise tone** | MOD2, row 2 | Its colour (cymbal and cowbell: resonance). Kick: **Sub tone**, dark to raw |
| **Noise decay** | MOD2, row 3 | Its length (cymbal: low band decay). Kick: **Sub octave**, in thirds of the knob: two octaves down, one, or on the note |
| **Spread** | MOD2, row 4 | Kick: Hold, the boom held open. Tom: overtone above 64. Clap: humanise. Others: the tuning between their parts |
| **Character** | MOD2, row 5 | Kick: fold. Snare: **resonance**, the snappy's filter ringing up to a pitched ring. Clap: resonance. Tom: bend up or down for syndrum zaps, 64 none. Rim: clave at 127. Hat, cymbal, cowbell: ring mod |
| **Decay** | MOD1, row 1 | The main decay, a sixth to six times the machine's; 127 holds while the note does. On the hats one knob runs from the 808's closed hat (about 8) to its open hat (64) |
| **Punch** | MOD2, row 6 | On / off: a transient compressor, the peak stays and the body right after it comes up |
| **Crush** | MOD2, row 7 | Sample rate and bit depth down, past the 909's 6-bit sound |

Pitch (MOD1, row 3) is the Deluge's own transpose. The kick, snare and tom put their body on the note; the others move their whole sound with it, like the tuning trimmer inside the machine. Both machines' kicks sit at 49 Hz, so the kits play them on G1.

**Accent:** every TRIBE row has a velocity cable to Attack, as well as to level. Accented steps hit harder rather than just louder, as on the real machines.

### Kits

| Kit | What it is |
|---|---|
| **TRIBE** | The hybrid: an 808 body with some 909 punch on the kick, a 909 snare, 808 clap, rim and tom, 909-leaning hats and cymbal |
| **808** | Every voice at the 808 end, the cowbell in for the cymbal |
| **909** | Every voice at the 909 end |
| **MIAMI** | The long 808 boom, a bright snappy snare, clave, a conga, cowbell |
| **TECHNO** | A driven 909 kick tuned long, a dark square sub on its note under it, tight bright hats, a ride |
| **HOUSE** | The 909 with Punch on the kick, a looser clap, an open hat for the offbeats, a crash |
| **ELECTRO** | A short droopy 808 kick, a high snappy snare, a syndrum zap on the tom, cowbell |
| **TRAP** | An 808 that holds and rings with a sub an octave under it, a cracking hybrid snare, wide clap, rapid 909 hats |
| **HARDGROOVE** | Everything 909 and driven, a square sub growling under the kick, the snare's snappy ringing, hats crushed a little |
| **LOFI** | Half way between the machines and through the crusher |
| **INDUSTRIAL** | Past both machines: a square kick folded and subbed, a self-ringing snare, ring modulated metal, driven hard |

### How to approach it

1. Play the **808**, **909** and **TRIBE** kits to hear both machines and the blend.
2. On each row set **808 > 909** first, then shape it with **Decay** and **Tone**. Most classic sounds need nothing else.
3. Leave the rest at 64 until you want something new, then reach for the extras: the kick's sub and square wave, the snare's resonance, the tom's bend, ring mod on the metal.
4. Automate it: 808 > 909 across a section, Decay on the open hat, the kick's Sweep time, the tom's Bend.

### Good to know

- No TRIBE voice uses more CPU than its Cyc counterpart (kick against Cyc Kik, snare against Cyc Snr, clap against clap eng, tom and rim against Cyc Perc, hat, cymbal and cowbell against Cyc Metal) at any setting, with Punch, Drive and modulation on or off. The metal voices run at about a third of Cyc Metal.
- Every voice peaks about 1.5 dB under full scale at its centred knobs, at any 808 > 909 setting.
- The 909 never had a cowbell: TRIBE's 909 end of it is built the 909's way. The 909 cymbal's long tail is set by ear, as the recordings stop short.

[Back to top](#readme-top)

## 31. Scrolling 7SEG text

Four letters don't say much. With **7SEG text** set to **SCROLL**, the 7-segment display flashes each menu item's and option's four letter name, then scrolls its full name: **CTYP** then **Crush type**, **ENV1** then **Envelope 1**. You read the short name at once and get the full one if you wait.

To turn it on: **SHIFT + press SELECT** to open Settings, go to **Community Features** (**FEAT**) and set **7SEG text** (**TEXT**) to **SCROLL**. It starts on **7SEG**, the four letter names, as before.

- **Menu names and options:** the four letter name flashes three times (with its dot), then the full name scrolls back and forth until you move on.
- **When the full name says nothing more,** the four letter name shows as it always did, with no flash and no scroll: a name that fits (**FX**), the same letters in other case or spacing (**LFO1** for LFO 1, **ULAW** for u-Law), or one that fits once its spaces go (**LP18** for 18 dB).
- **Context menus:** the four letter option blinks, then its full name scrolls.
- Turning SELECT replaces the text at once. You never wait for a scroll to finish.

### Good to know

- The setting only shows on a 7-segment display, real or emulated. OLED Deluges don't change.
- A few menus still show four letters: those that build their own display text, such as DX7 parameters and MIDI channels, and option names inside Community Features such as **SCAL** and **FILL**.
- Some letters (M, W, K, X, V) are rough on seven segments, as with any scrolling name on the Deluge.

[Back to top](#readme-top)

## 32. Kit mixer

Balancing a kit used to mean holding each row and turning its LEVEL knob, one row at a time, with nothing showing how the rows sat against each other. The kit mixer turns the grid into a fader per row.

In a kit clip, hold the **LEVEL/PAN** gold knob button and press **KEYBOARD**. The display shows **MIX** (**Mixer** on OLED) and **KEYBOARD** blinks. Do the same again to go back to the steps (**STEP**).

- **The bars:** each row's pads show its level, from the bottom of the LEVEL knob on the far left to the top on the far right. The brightest pad is where it sits now.
- **Setting a level:** press a pad on the row. It does what turning that row's LEVEL gold knob would: the value pops up, undo takes it back and MIDI follow sends it.
- **The bars keep up** when the level changes some other way: the gold knob, automation playing back, MIDI or the [companion](#27-bribeluge-companion).
- **Mute and audition pads** work as normal. A muted row's bar goes grey.
- **SHIFT + pad** shortcuts still open their menus.
- Scroll up and down to reach more rows. Scrolling left and right does nothing, as there are no steps on screen.

### Good to know

- It works on every kit: the Bribeluge kits (TRIBE, Cycles, LXR, GIN) and your own, sample and synth rows included. MIDI and gate rows stay dark.
- Notes, automation and parameter locks are never touched. While the bars show, the pads can't reach the steps, and the note editors and Euclidean edits stay closed.
- Automation behaves as it does with the knob: a pad press holds the new level until the next automation point, or records it if you're recording.
- Leaving the clip, or changing it from a kit to something else, brings the steps back.

[Back to top](#readme-top)

## 33. Engine panels

BRUNO106, BROPHET and the wavetable synths had panels on the [companion](#27-bribeluge-companion) that looked and worked like the instruments they come from. The other engines only had a row of knobs. Now every engine gets a panel with its name across the top: the drum machines from v1.44, and every other engine and the Deluge's own synth modes from v1.47.

With a kit row or a synth on one of these engines selected, the companion shows its panel.

**Drum machines** (built in kits, a row per voice):

- **TRIBE:** an 808 on the left (dark panel, cream knobs, orange lettering) and a 909 on the right (silver panel, black knobs), blending into each other in the middle, where the big **MORPH** knob sits. Pitch sweep, attack and **PUNCH**, the noise (or the kick's sub, the snare's snappy, the clap's tail), the voice's own two, tone, decay, drive and crush, then the row's tuning, level, pan, filters and sends.
- **CYC:** bone and grey, with the four big machine knobs (**Color**, **Shape**, **Sweep**, **Contour**, or what the machine calls them), decay, drive and **PUNCH**, and a row of lights showing which machine the row plays.
- **LXR:** black with pink LED rings around every knob. The layout follows the voice: kick and toms (osc, pitch envelope, FM), snare (osc, pitch envelope, noise and its filter) or cymbals and hats (osc and two modulators), then the transient, decay and drive.
- **GIN:** machined gunmetal with aluminium knobs, and a scope showing the tone's wave bent by its pitch modulation next to the noise burst. Tone, pitch mod, mix, the noise and its filter and envelope, drive, decay, EQ and the row's tuning, level, pan and sends.

**Drum voices** (one engine on a row, new in v1.47):

- **ULTRAKIK:** an oxblood kick drum shell with a chrome hoop and chrome knobs, and a drum head drawing the pitch drop as you turn it. Pitch (a big **PUNCH**, sweep, bend), body (wave, fold, grit, sub, hold), click, drive and its type, crush, decay, tuning and a **PRESET** knob that loads its 16 kicks as its preset menu does.
- **XIA:** silver modules on black rails. DXIA shows its three operators (blendex and frequency each), DIIA its partials (weight, alloy, shape) and strike, then drive, decay, **PUNCH** and the **VARIANT** (L, B, C or G, I, H), which loads that variant as SYNTH MODE does.

**Synths** (new in v1.47, next to BRUNO106, BROPHET and WAVE):

- **BRIBERING:** deep teal, with a resonator drawn in rings that follow **Structure**, **Brightness** and **Damping** and a string struck at **Position**. Model, strings per voice, bow, drive, the four big knobs, tuning, attack and release, filters and sends.
- **303:** brushed silver and black knobs: tuning, a big cutoff, resonance, env mod, decay, accent, the saw to square wave, slide, the filter type (303, LP18, DIRT) and its drive, amp decay and sends.
- **DX7:** a brown body with a green screen showing the voice's name, which operators are on, the algorithm and feedback. Six operator strips (on, ratio and fine beside a tall level fader), the algorithm and feedback, the LFO, transpose and sends.
- **SUBTRACTIVE, FM and RINGMOD:** the Deluge's own synth modes, in aluminium with dark sections and a strip of pads, pink, teal and amber. SUBTRACTIVE: both oscillators (type, transpose, pulse width, level, sync), noise, both filters and their modes, two envelopes, two LFOs, mod FX, delay, reverb and unison. FM: both modulators (amount, transpose, feedback, where modulator 2 goes) and both carriers, with a drawing of the routing. RINGMOD: both oscillators ring modulated, through the filters. An oscillator can switch between the plain waves here; a wavetable or sample is picked on the Deluge.

The **BRUNO106** panel is rebuilt in v1.47: three rows that fill the width (the synth's own panel, then the amp and both envelopes, then the effects), shorter sliders, and clearer names (**PWM SRC**, **ENV POL**, **ENV AMT**, **SLOP** in its own **VOICE** section).

Every panel works both ways: drag a knob up or down and the Deluge follows, as if you'd turned it there; turn it on the Deluge and the panel's knob moves. Buttons pick a setting (a wave, a filter type, **PUNCH** on or off).

- **The voice's names:** knobs are labelled the way the Deluge names them for that voice. TRIBE's kick shows **Sub**, **Hold** and **Fold** where the snare shows **Snappy** and **Resonance**; the Cyc clap and Vtg snare rename the machine knobs.
- **Row keys:** a key for each of the kit's rows on that engine runs along the bottom, the one being edited lit. Press one and the Deluge selects that row and sounds it for as long as you hold the key, as its audition pad would, and the panel follows it.
- **Gold knobs follow your finger:** touch any control on any engine panel (BRUNO106, BROPHET and WAVE too) and the Deluge lights the mod button whose gold knobs turn it: touch **LPF** and cutoff/resonance lights, touch **Tune** on a drum row and **CUSTOM 1** lights. Controls no gold knob holds (a wave, **PUNCH**) leave the buttons as they are.
- **SHORTCUT:** a button at the bottom right of every panel. While it's lit, touching a control also opens its setting on the Deluge, as holding **SHIFT** and pressing its shortcut pad would. It stays as you left it on that tablet.
- **The kit picker** draws TRIBE, CYC, LXR and GIN as these panels look, so a new kit shows what you're about to get.
- **Every row's own settings** sit on each drum panel too: tuning (48 semitones each way), level, pan, the filters and the delay and reverb sends.
- **What stays as it was:** sample kit rows and audio inputs keep their own views, and wavetable sounds keep the WAVE panel.

[Back to top](#readme-top)

## Quick reference

| Control | What it does |
|---|---|
| **SHIFT + turn TEMPO** | Swing amount (Classic) or level 0 to 6 (Stumble). The display stays up while SHIFT is held. |
| **SHIFT + push and turn TEMPO** | Step through the Stumble swing styles: HOPP, DEEP, SQEZ, FOLD (Stumble on) |
| **SHIFT + click TEMPO** | Clear tempo automation, as before (now on release) |
| **SYNC SCALING** | Kit pattern mode on/off (with Sync Scaling Action set to Kit pattern mode) |
| **Hold a row's audition pad + turn SELECT** | Step that row through its saved patterns (kit pattern mode) |
| **Turn SELECT, then press SELECT** | Pick a pattern bank, then load it into all six rows (kit pattern mode) |
| **Hold a row's audition pad + SAVE** | Save that row's pattern over its slot (kit pattern mode) |
| **TAP** | Play a fill (with Tap Tempo Action set to Autofill). Hold for a longer fill. |
| **Hold TAP + turn TEMPO** | Pick the fill: Ghost, Drive, Build, Climb, Stutter (Autofill) |
| **SHIFT + TAP** | Metronome on/off, as before |
| **Hold a note + turn the up/down knob** | Shift the note's octave, up to 4 either way (Mono sequencer) |
| **Hold a note + press and turn the up/down knob** | Ratchet the note (note repeat), as normal (Mono sequencer) |
| **Hold a note + click the up/down knob** | Slide on or off for that step (Mono sequencer) |
| **Hold a row's audition pad + turn the lower gold knob** | Set that row's voltage (Mono sequencer, CV CUSTOM) |
| **RECORD while playing** | Start recording an empty playing clip with no loop limit (Endless Record on) |
| **RECORD again** | Stop recording at the next bar. RECORD blinks until then; press it again to keep going (Endless Record on) |
| **FX > DISTORTION > CTYP** | How Bitcrush and Decimation sound: **HARD**, **VINT**, **ULAW**, **JITR**, **DECY** or **CLAS** (Crush types) |
| **SELECT in song view > MASTER > MASTER CLIP** | Clip or limit the song's output: **SOFT**, **TANH**, **HARD**, **TAPE**, **FOLD** or **LIMT**, with **CLIP DRIVE** and **CEILING** (Master clip) |
| **MOD FX > SHIFT** | Three-band frequency shifter: Depth is the amount, Rate the glide, Feedback, Offset morphs between two sets of shifts (SHIFT) |
| **SHIFT + KIT** | New kit: choose **Kit** (samples), **Cycles**, **LXR**, **GIN** or **TRIBE** (eight rows each; on one of them, picking another swaps it in place, row for row, keeping rows you added above or below), or **ULTRAKIK** or **XIA** on the selected row only |
| **SHIFT + KIT on an LXR, Cycles, GIN or TRIBE kit** | Kit presets: turn SELECT to play each preset on the kit's rows, SELECT to keep, BACK to go back (Drum synth) |
| **Turn SELECT on an LXR, Cycles, GIN or TRIBE kit** | Step to the kit's next or previous preset and keep it (Instrument Picker, new in v1.19) |
| **Tap an empty audition pad on an LXR, Cycles, GIN or TRIBE kit** | Add a row there and open SYNTH MODE to choose its sound (Drum synth) |
| **Hold a row's audition pad + SYNTH MODE pad** | Put the row on any drum synth engine or variant, or back to **Sample**. On a drum synth row the OSC1 TYPE pad opens the same list |
| **SHIFT + a MOD1 / MOD2 pad on a drum synth row** | That engine's setting: MOD1 from the bottom is Decay, Drive, Pitch, Pitch env amount, Pitch env speed, Character A, Character B, Extra 1; MOD2 holds Extras 2 to 9 (Drum synth, new in v1.16) |
| **Attack / Release gold knobs** | Drive / Decay (drum synth rows and the 303) |
| **Mod rate / Mod depth gold knobs** | Pitch envelope speed / amount: Contour / Sweep on the Cyc engines, the filter envelope's Decay / Env mod on the 303, vibrato on BROPHET and BRUNO106 |
| **CUSTOM 2 / CUSTOM 3 gold knobs** | Character A / B: Color / Shape on the Cyc engines, Mix / Noise freq on GIN, Accent / Saw-square on the 303. Hold a step and turn to parameter lock |
| **Hold SHIFT on a drum synth** | Its setting pads pulse pink, and stay lit while you edit one; purple on BRINGS, BROPHET and BRUNO106. Shows with the Shortcut Overlay on or off (Pad Guides) |
| **Hold a gold knob button** | Its two settings' pads flash: red for the top knob, yellow for the bottom (Pad Guides) |
| **SHIFT + a shortcut pad** | If the setting is on a gold knob, that knob's button LED blinks (Pad Guides, new in v1.29) |
| **Hold SHIFT + hold a shortcut pad** | The 7-segment display scrolls that setting's full name; let go to see its value (Pad names, new in v1.20) |
| **SHIFT + OSC1 WAVE INDEX pad on an ULTRAKIK row, turn SELECT** | Play through ULTRAKIK's sixteen presets, each loading as you turn (**KPRE**) (ULTRAKIK, new in v1.21) |
| **SHIFT + OSC1 PULSE WIDTH / RETRIGGER / FEEDBACK pad on an ULTRAKIK row** | Body wave / Snap / Drive type (ULTRAKIK, new in v1.21) |
| **SHIFT + SYNTH** | Synth browser: pick a type (**SUBT**, **FM**, **WAVE**, **RING**, **BRINGS**, **DX7**, **BROPHET**, **BRUNO106**, **303**, **INIT**), then a category, then turn SELECT to play through its presets. The audition pads play the type's init (or your own patch) the whole way. SHIFT + SYNTH again moves on, BACK goes up a level (Synth browser) |
| **SETTINGS > DEFAULTS > UI > CLIP TYPE > KIT / SYNT** | The kit and synth new tracks start as (Instrument Picker, new in v1.19) |
| **Drum synth setting open + a mod source pad** | Patch that source (LFO, envelope, velocity, random...) to the setting (Drum synth, new in v1.14) |
| **SHIFT + the pad below FOLD** | **Feedback** (**FDBK**): the voice's filter output fed back into its input (Feedback) |
| **CUSTOM 2 / CUSTOM 3 gold knobs on a WAVE preset** | Wavetable position / LFO 1's sweep of it (Synth browser) |
| **SHIFT + SATURATION pad** | Saturation drive, 0 to 50. Press BACK, then turn SELECT to reach **Type** |
| **SHIFT + SATURATION pad, then hold LEARN and turn a gold knob** | Put saturation drive on that gold knob, in the context its button has selected (Saturation, new in v1.16.1) |
| **SHIFT + OSC1 / OSC2 PULSE WIDTH pad** | Sample start offset, when that oscillator plays a sample |
| **Automation view: OSC1 / OSC2 PULSE WIDTH pad** | Draw the start offset step by step, when that oscillator plays a sample |
| **SYNTH MODE pad, choose 303** | Turn a synth into the 303 (303 synth) |
| **SYNTH MODE pad, choose BMOD, BSYM, BSTR, BFM or BCHD** | Turn a synth or kit row into BRIBERING MODE on that model (BRIBERING MODE, new in v1.25) |
| **SYNTH MODE pad, choose BROPHET** | Turn a synth or kit row into BROPHET (BROPHET, new in v1.28) |
| **SHIFT + an OSC1, OSC2 or FM MOD pad on BRINGS, BROPHET or BRUNO106** | That engine's setting, by the pad's own label: levels on LEVEL, pitch on TRANSPOSE, waves on TYPE (new in v1.28) |
| **LPF MODE: Brophet** | Pro-53's filter on any synth, kit row, audio clip or the song. LPF MORPH is its drive (BROPHET, new in v1.28) |
| **SYNTH MODE pad, choose BRUNO106** | Turn a synth or kit row into BRUNO106 (BRUNO106, new in v1.31) |
| **LPF MODE: Bruno106** | The Juno-106's IR3109 filter on any synth, kit row, audio clip or the song. LPF MORPH is its drive (BRUNO106, new in v1.31) |
| **SHIFT + FM MOD 1 LEVEL pad on BRUNO106** | **HPF**: **BOST**, **FLAT**, **236** or **754** (BRUNO106, new in v1.31) |
| **SHIFT + FM MOD 1 TRANSPOSE pad on BRUNO106** | BRUNO CHORUS on or off, flipping with each press (BRUNO106, new in v1.31) |
| **MOD FX > TYPE > BRUNO CHORUS** | The Juno's chorus on any track; **Chorus mode** (**CMOD**: **I**, **II**, **I-II**) appears below it (BRUNO106, new in v1.31) |
| **Cutoff/Res and Attack/Release gold knobs** | Cutoff / Resonance and Drive / Amp decay (303 synth) |
| **SHIFT + LPF MODE pad on a 303** | The 303's filter: **303**, **LP18** or **DIRT** (303 synth, new in v1.22) |
| **SHIFT + LPF MORPH / ENV1 DECAY / ENV2 DECAY pad on a 303** | Drive / Amp decay / Decay (303 synth, new in v1.22.1) |
| **Audition pad + SELECT > GATE** | That kit row's gate output: off or 1 to 4 (Gate out, first in the row's menu from v1.22.2) |
| **Kit menu (AFFECT ENTIRE on) > Gate out** | Rows 1 to 4 play out of gate outputs 1 to 4, one kit at a time (Gate out, new in v1.22) |
| **Audition pad + SELECT > MIDI** | That kit row's MIDI out: channel and note, sent as the row plays, gate or not (second in the row's menu from v1.23) |
| **SHIFT + MIDI** | **MIDI** track, **MKIT** or **LOOP**, then for MKIT the layout: **1CH**, **16CH** or **BLNK**. SHIFT + MIDI again moves on, SELECT or MIDI picks (MIDI kits, new in v1.23; LOOP, new in v1.24) |
| **MIDI track menu > ECHO** | **ON**, **OFF** or **REC**: whether what you play into the track goes back out (MIDI loop tracks, new in v1.24) |
| **Hold a MIDI row's audition pad + SELECT** | That row's **CHAN** and **NOTE**, first in the note row editor (MIDI kits, new in v1.23) |
| **Hold a MIDI row's audition pad + turn a gold knob** | Change that row's channel or note, as before |
| **CV track on BOTH > CV 2 Source > LOCK** | The gold knobs set CV 2 in semitones, 12 to an octave. Hold a step and turn to lock it (CV2 lock, new in v1.23) |
| **SETTINGS > Community Features > Elektron P-locks** | Parameter locks stay on their own step (**ELEK**, new in v1.23) |
| **SETTINGS > Community Features > 7SEG text** | **7SEG**: four letter names. **SCROLL**: the four letter name flashes three times, then the full name scrolls (**TEXT**, new in v1.42, flash first from v1.46) |
| **In a kit clip: hold LEVEL/PAN + press KEYBOARD** | Kit mixer: each row's pads show and set its level, left at the bottom of the knob, right at the top. The same again goes back to the steps (Kit mixer, new in v1.43) |
| **SHIFT + turn the delay Amount gold knob** | Delay feedback, 0 to 50. The knob on its own still sets the delay amount (Delay feedback and tone) |
| **SHIFT + turn the delay Rate gold knob** | Delay tone: lowpass to the left, flat in the middle, highpass to the right (Delay feedback and tone) |
| **SHIFT + PAN pad, press again** | **Pan spread**: each poly note gets its own place in the stereo field. The pad blinks yellow; SELECT goes on to **Spread mode**: **ALT**, **KEY**, **RAND** or **PING** (Pan spread, new in v1.30) |
| **SHIFT + delay AMOUNT pad, press again** | Delay feedback. The pad blinks yellow; press again to go back to Amount (Delay feedback and tone) |
| **SHIFT + delay RATE pad, press again** | Delay tone. The pad blinks yellow; press again to go back to Rate (Delay feedback and tone) |
| **SHIFT + AFFECT ENTIRE on an LXR, Cycles or GIN kit** | Snapshot the kit and move every drum at once. AFFECT ENTIRE flashes (Affect all) |
| **AFFECT ENTIRE during the snapshot** | Swap between All voices (ALL) and the kit's FX (FX), keeping the snapshot (Affect all) |
| **SHIFT + AFFECT ENTIRE again** | Put the snapshot back on the next bar. AFFECT ENTIRE flashes twice as fast until then (Affect all) |


[Back to top](#readme-top)

## About

My approach to Bribeluge isn't to stack features on top of the Deluge's existing architecture. It's to make the Deluge a more deliberate and direct instrument for my needs: almost a brand new ultra version of what the Deluge has been for me since about 2018.

- **It isn't built for everyone.** I haven't optimised it for widespread use.
- **Backwards compatibility isn't the priority.** I haven't worried too much about songs made on earlier firmware. That said, I've tested a lot of older songs I've cut in the past and haven't found errors in any of them, so most of it seems to be backwards compatible.
- **A studio in a box.** I'm not working towards an infinite canvas with a million different tracks playing at once, or a multitrack mini DAW. I'm working towards a curated collection of tracks: a handful of drum machines, synths and effects, each with an exceptional amount of capability. There's no track limit, and a song can still hold dozens of tracks.
- **Performance first.** I'd rather it be super optimised and performance friendly, with the features I've been missing since the Deluge was first released, like sample start offset.

[Back to top](#readme-top)

## Changelog

Newest first: what changed in each release, why, and what it taught me.

- **v1.49: More room in the Deluge's fast memory.** A TRIBE kit now takes 79 KB of the Deluge's on-chip RAM, down from 135 KB, and a 16-row sample kit loaded next to it stays in on-chip RAM instead of spilling 87 KB into the slower SDRAM. Three changes, and only the first is one you can hear, on hits that used to overlap: each [drum engine](#6-drum-synth) row plays one voice and retriggers it, the store of drum engine voices starts at 8 and grows only as far as a song needs (it made 48 up front), and every kit row and kit fits a 2 KB block again. *Why:* the more of a song that lives in on-chip RAM, the less the Deluge has to fall back on SDRAM, which is slower for voices and, once full, takes room from loaded samples. *Learned:* measure before guessing. The Deluge now streams its CPU load, time per engine and free memory over USB, and can list every block of memory in use, so I could see what each kit really takes. The Deluge hands out memory in power-of-two blocks: Bribeluge's extra settings had pushed every kit row from 1,864 to 2,384 bytes, just past 2 KB, so each row took a 4 KB block. Moving the settings only some sounds use (303, BRUNO106, the newer crush types and saturation, drum engine settings) out of the row put it back at 2,024. The stream also showed a TRIBE voice costs about 1.5 times a sample voice, which is the next thing to work on. See [Measuring CPU and memory](#measuring-cpu-and-memory).
- **v1.48: The Deluge's menu, whole page, by touch.** With a menu open on the Deluge (a clip's, the song's or SHIFT + SELECT settings), the [companion](#27-bribeluge-companion) shows every open level as a column you can tap: any entry at any level is one tap away, a setting gets its value, steps and named choices as tiles, and the page goes back to what it showed when the menu closes. *Why:* the select knob walks a long menu one entry at a time, and a screen can show the whole tree at once. *Learned:* the companion doesn't need its own copy of the menu: the Deluge sends each level as it is (only what applies to this sound), and a tap is played back as the presses a hand would make (BACK up, turn, SELECT), so everything the Deluge does on the way still happens.
- **v1.47: A panel for every engine.** The [companion](#27-bribeluge-companion) now has a hardware-style panel for ULTRAKIK, XIA, BRIBERING, the 303, DX7 and the Deluge's own SUBTRACTIVE, FM and RINGMOD, next to the drum machines, BRUNO106, BROPHET and WAVE, and the BRUNO106 panel is rebuilt in three rows that fill the width with clearer names. See [Engine panels](#33-engine-panels). *Why:* once the drum machines had panels, every other engine looked unfinished next to them. *Learned:* the same table that drives the drum panels covers the Deluge's own synth too, once it knows a few more kinds of setting (oscillator types, filter modes, unison, DX7 voice bytes), and a preset or variant can be loaded exactly as its menu does it.
- **v1.46: Scrolling 7SEG text flashes the short name first.** On **SCROLL**, a menu name or option now flashes its four letter 7SEG name three times, then scrolls the full name, and names where the full one says nothing more (**LFO1**, **ULAW**, **LP18**) show as they always did. See [Scrolling 7SEG text](#31-scrolling-7seg-text). Also has the v1.45.1 kit name fix. *Why:* a suggestion from Sean.Good.Vibes on the community Discord. With only the full name, ENV1 to ENV4 all start "Envelope", so you wait for the scroll to tell them apart; the community docs show both, short then long. *Learned:* the full name isn't always better. Plenty of OLED names are the 7SEG ones with a space added, and scrolling those just costs time.

- **v1.45.1: Preset kits keep their name.** Choosing a preset kit renames the kit to the preset, so the name no longer goes back to **KIT 0xx** on the next audition or in the companion. LXR and Cycles **Default** keeps the kit's name, and the renamed kit is the song's own until saved. See [Kit presets](#kit-presets). *Why:* the preset's name only flashed up, then the kit's old name came back the moment you played a row. *Learned:* showing a name and giving it are different things: the display only shows what the kit is called, so the kit has to carry the name.
- **v1.45: Row keys you can hear, gold knobs that follow, SHORTCUT.** On the [drum engine panels](#33-engine-panels), holding a row key sounds that row like its audition pad. Touching a control on any companion panel lights the mod button whose gold knobs turn it, and with **SHORTCUT** lit it opens that control's setting on the Deluge too. The kit picker draws the four drum machines as their panels look, and TRIBE's I is solid pink. *Why:* the panel and the hardware should feel like one instrument: pick a sound, hear it, and have the knobs under your hand already on what you touched. *Learned:* the Deluge already knows where every setting lives (its gold knob pairs and its shortcut pads), so the companion only has to say which control was touched, and the Deluge works out the rest.
- **v1.44: Drum engine panels.** The [companion](#27-bribeluge-companion) shows a panel for each Bribeluge drum engine: TRIBE as an 808 on the left and a 909 on the right with MORPH on the seam, CYC in bone and grey, LXR in black with pink LED rings and a layout per voice, and GIN in machined gunmetal with a scope of its tone and noise. Every knob and button works both ways, the labels follow the voice, and a key per kit row selects the row to edit. See [Drum engine panels](#33-engine-panels). *Why:* the synth engines had panels that felt like the instruments, and the drum engines deserved the same. *Learned:* each engine keeps its settings in one of a few ways (a control slot, a choice, a number), so one table per panel covers all four, and the kit's rows come along in the same message so the keys always match the kit.

- **v1.43: Kit mixer.** In a kit clip, hold **LEVEL/PAN** and press **KEYBOARD**: each row's pads become a bar for its level, left at the bottom of the knob, right at the top. Press a pad to set it, as turning that row's gold knob would. The bars follow the level from the knob, automation, MIDI and the companion. The same again brings the steps back, untouched. Works on every kit. See [Kit mixer](#32-kit-mixer). *Why:* balancing a kit meant holding each row and turning a knob, one row at a time, with nothing showing how the rows sat against each other. *Learned:* the bars only had to be a different picture of the same knob. Setting the level the way the gold knob does brings undo, automation and MIDI follow along with it, and the notes are never in play.

- **v1.42: Scrolling 7SEG text.** A new **Community Features** setting, **7SEG text** (**TEXT**): on **SCROLL**, the 7-segment display shows every menu name and option by its full name instead of four letters, flashing then scrolling when it doesn't fit, the way context menu options already did. On **7SEG**, the default, nothing changes. OLED Deluges don't see the setting. See [Scrolling 7SEG text](#31-scrolling-7seg-text). *Why:* four letter names are a code you have to learn, and the full names were already in the firmware for the OLED. *Learned:* the change is small because every name already exists in two versions: showing the OLED one on the 7SEG is a matter of which list the menu reads from.

- **v1.41: Every companion knob works both ways.** On the [companion](#27-bribeluge-companion), every knob it shows now turns from the screen, not just the BRUNO106, BROPHET and WAVE panels: the main settings (oscillators, filters, envelopes, voice, effects, LFOs), each drum engine's controls, the 303's knobs and the gold knobs. Drag up or down with a finger or the mouse and the Deluge follows; turn a knob on the Deluge and the screen follows. A tap still opens the setting on the Deluge, and a tap on a switch (BRUNO106 saw, pulse, HPF and chorus, the 303 filter) steps it. Gold knob moves go through the Deluge's own knob, so popups, affect all and parameter locks behave as on the hardware. A gold knob on a patch cable now shows its whole range, -50 to +50; a negative amount used to show as 0. *Why:* the panels showed that two-way control works, and a screen of knobs you can't turn is half a control surface. *Learned:* turning a gold knob from the screen is best done as the turn a hand would make to get there, not by writing the value, so everything the Deluge does around a knob turn still happens.

- **v1.40: Eight-row kits that swap in place.** Every Bribeluge kit (TRIBE, Cycles, LXR, GIN) now has eight rows, so they swap in and out of each other easily: **SHIFT + KIT** to another kit changes it in place, row for row, with the pattern still on its rows. You can add rows under the kick or over the top row, and they stay where they are, with their sounds and notes, when you swap kits or change preset. A Cycles kit gains **CLAP** and **PERC2**, an LXR kit gains **PERC**, and every Cycles and LXR preset has the new rows (copy the preset folders to the card again). A kit's own eight rows keep their order and can't be deleted; rows you added delete as before. Kits in older songs get their missing rows the first time you swap them or change their preset. See [Making a drum synth kit](#making-a-drum-synth-kit). *Why:* a Cycles kit had six rows and an LXR kit seven, so a swap moved things about, and a kit with rows added couldn't be swapped at all. *Learned:* the swap used to build a whole new kit and pour the pattern back in from the bottom. Changing the sounds under the rows, the way the presets already did, is simpler and leaves everything else alone.

- **v1.39.3: Data crush type removed.** The **Data** crush type from v1.37 is gone. Its Bitcrush knob mostly added clicks, not the looping, corrupted sound it was meant to have. **Crush type** now offers Hard, Vintage, u-Law, Jitter, Decay and Classic (see [Crush types](#23-crush-types)). Songs and presets saved with Data load as **Hard**: Decimation sounds the same, and Bitcrush becomes Hard's bit depth. The other types sound exactly as they did. *Why:* a type that isn't worth using is one more stop in a menu you scroll with one knob. *Learned:* Decay came over from Seal Eggs already tuned by ear on hardware, and Data was designed from scratch for this build without that. It showed.

- **v1.39.2: Persistent overlay for Bribesynths and kits.** Hold **SHIFT** and the pink pads on a Bribeluge kit row and the purple pads on a Bribesynth (BRINGS, BROPHET, BRUNO106) now pulse, and they stay whatever the community firmware's **Shortcut Overlay** is set to: Off, Menu Only or Menu + Clip. With the overlay up they pulse at full brightness over its dimmed colours. With it off they fade in and out of the notes underneath. The pulse is the two-beat breath synth tracks have on their section pads in song view (see [Persistent overlay](#persistent-overlay)). *Fixed:* with the overlay on Menu + Clip, the Bribeluge pads didn't show in a clip at all, and in a sound menu they came out dim and mixed with the stock colour. *Why:* the overlay repaints every pad with the stock shortcut colours and dims the lot, which left no way to see where Bribeluge puts its own settings. *Learned:* a colour can't mark a pad on a grid that's already colour coded, as the stock FM pads are purple too. Movement can.

- **v1.39.1: OLED and overlay fixes.** *Fixed:* on a Deluge with the OLED screen, choosing **Bribering sympathetic** as the synth mode froze the Deluge. With Shortcut Overlay set to On - Menu + Clip, pressing **SHIFT** in a clip on a drum engine sound (a TRIBE, Cycles, LXR or GIN row, or a BRIBERING, BROPHET or BRUNO106 synth) froze it too, until a sound menu had been opened. *New:* in the drum synth pad editor, **SCALE** and **CROSS SCREEN** step to the setting on the left and right, as they page through the OLED's menus. Both are lit while the editor is open. *Why:* the OLED's notification bar shortens the title until the value fits beside it, and that name is too long to ever fit, so it never stopped. The overlay asked each shortcut pad about its setting through a part of the sound menu that isn't set up until a menu has been opened. *Learned:* my Deluge has the 7-segment display and the overlay off, so neither showed up here. Thanks to the beta testers who reported them.

- **v1.39: TRIBE.** A new drum engine: an 808 / 909 drum machine with eight voices, each running from the 808 to the 909 on one knob, every other knob centred on the real machine, extras after Hexinverter's Mutant BD9 and Mutant Snare, and eleven kits. Built on v1.38.1. *Why:* one engine for every 808 and 909 sound on the Cycles layout, as close to the real machines as possible, and never heavier than the Cyc engines. *Learned:* the published numbers were off in places. Measured against recordings, the 808 kick sweeps rather than steps and sighs down two semitones as it rings, the 909's TUNE only sets how fast its sweep falls, and both kicks settle at 49 Hz.

- **v1.38.1: WAVE panel fix.** *Fixed:* moves made on the companion's WAVE panel never reached the Deluge. Dragging the table or turning a control showed the new place while your finger was on it, then sprang back to where it was. Every control on the panel was affected, position, sweeps, envelopes, filter and the rest; the BRUNO106 and BROPHET panels were fine. *Why:* the Deluge only applied the tablet's panel moves when a BRUNO106 or BROPHET move was waiting, and the WAVE panel was never added to that check. *Learned:* the tablet holds a moved control for a moment, then shows what the Deluge says, so a move the Deluge ignores looks like a spring back, not like nothing happening.

- **v1.38: Stability.** No new features: this one is about older songs and staying up. It takes in the community's 18 fixes since 1.3.0, among them the freeze when a menu refuses to open, the undo crash in the note editor, crashes around deleted clips and stuck MIDI notes. It's now built as a release candidate, not a developer build, so the extra internal checks that stopped the Deluge with an error code on some older songs are left out, as on the official release. Older songs' delays work as they did: feedback follows the amount, automation included, until you set the feedback, and the delay stays on its single, lighter path. Older songs that use Bitcrush or Decimation always load as Classic. *Fixed:* switching from BRUNO CHORUS to another chorus, flanger, warble or dimension could burst; a modulated sample start offset stuttered on looping samples; deleting a kit clip during an Autofill could crash; the companion rebuilt everything it shows on every screen redraw, which could take longer than an audio buffer, and now does it at most 40 times a second. *Why:* reports of crashes, clicks and older songs sounding different. *Learned:* a developer build halts on checks the official release skips, so some of the crashes were the Deluge stopping itself.

- **v1.37: Master clip, SHIFT, Decay and Data.** Things from my other firmware, brought over. **Master clip** puts a clipper or limiter at the very end of the song (Soft, Tanh, Hard, Tape, Fold or Limit, with drive and a ceiling), with the curves from KALI SMASH's SQUASH section. **SHIFT** is KALI SMASH's three-band frequency shifter as a Mod FX type. Two new crush types: **Decay**, the dying BBD chip from Seal Eggs' BBD character, on a BBD-style clock, and **Data**, new for this build, which corrupts the sound as 16-bit words (removed in v1.39.3). *Why:* the Deluge's output had nothing between a clean mix and a harsh digital clip, and these had already proved themselves on the Kali and the Sealegs. *Learned:* a clipper's filters start from silence, and the processed sound runs a little late, so switching it on mid-song clicked; now the filters are primed with the last samples that went past, every type has the same latency, and on and off crossfade.

- **v1.36: WAVE panel.** With a wavetable synth selected, the companion draws the table as a stack of its frames, with the position knob's frame lit and every playing note moving through it, envelope and LFO sweeps included (see [WAVE panel](#wave-panel)). Drag on it to move the position; a 3D / 2D switch flattens it to one cycle. The oscillators' position, sweep amounts, level and pitch sit beside it, envelope 2, filter, amp envelope, fold, feedback, volume and reverb underneath, both ways like the other panels. The WAVE presets' **CUSTOM 3** is LFO 1's sweep of the position again, not Feedback: with the position on CUSTOM 2, the pair reads as where and how much. *Fixed:* 128 BROPHET programs and 9 DX7 voices played off C (BROPHET where the original's osc A sat on another note, DX7 where the transpose or the carriers did); each now plays C on C, its intervals kept. *Why:* a wavetable is a picture of the sound, so you should be able to see where you are in it. *Learned:* the 3D view was slow on a tablet because it drew all 64 frames, and a blurred glow, every time a note moved; now the stack is drawn once and only the moving lines after it.

- **v1.35: BROPHET panel.** With a BROPHET track selected, the companion shows a knob panel laid out like the Prophet: poly-mod, LFO, both oscillators, mixer, filter, both envelopes, master, then crush, deci, saturation, delay and reverb (see [BROPHET panel](#brophet-panel)), in a P8 or a P5 look. It works both ways, like the BRUNO106 panel. Turning a knob on the Deluge now shows on either panel right away: an open panel is checked on its own every 15 ms, and knob updates no longer wait behind a busy USB buffer for the preset browser when it isn't open. *Fixed:* the 85 BROPHET presets with vibrato had almost none, the same squared pitch cable as the KR-106 presets in v1.34. *Why:* the second engine on the panel pattern, so the next ones are mostly a table. *Learned:* the lag wasn't the tablet: the Deluge held every knob update back 100 ms whenever its send buffer was more than half full, waiting for room for a browser window that wasn't there.

- **v1.34: BRUNO106 panel.** With a BRUNO106 track selected, the companion shows a slider panel laid out like the Juno: LFO, DCO, HPF, VCF, VCA and envelope 1, then envelope 2, the chorus, drive, crush, decimation, saturation, delay and reverb on a second row (see [BRUNO106 panel](#bruno106-panel)). It works both ways: drag a slider and the Deluge moves as if you'd turned its knob, turn a knob and the slider follows. BRUNO CHORUS gets a Rate and a Depth, centred on each mode's own. *Fixed:* the 34 KR-106 presets with DCO vibrato had almost none; copying a BRUNO106 track reset its chorus mode to I. *Why:* a synth this hands-on wants faders, not one menu per setting. *Learned:* the Deluge squares any patch cable that goes to pitch, so small amounts stay small. Converted like a filter cable, KR-106's 4 semitones of vibrato came out at about 0.06 of a semitone; the cable needs the square root of the linear amount. The Deluge also deletes a patch cable when it reaches zero, so the panel remembers PWM's LFO / MAN switch and the envelope's polarity itself while their slider sits at the bottom.

- **v1.33: Synth browser inits and DX7 presets.** SHIFT + SYNTH now always has something on the audition pads: each type plays its init synth through the type list, the categories and the folder, a synth track plays its own patch on its own type, and BACK from the types puts the track back as it was. Your own inits go in `SYNTHS/INIT`. DX7 is now a type like the others, with six categories, 288 presets and a two-operator FM init. The 99 WAVE presets are rebuilt. The companion names each engine knob by its own control. *Fixed:* loading a DX7 voice from a cartridge copied 10 of each operator's 11 scaling settings, so its right-hand keyboard scaling kept the previous voice's; DX7 algorithms 4 and 6 with feedback now use the core that plays their feedback loop after a voice loads. *Why:* audition pads in the first two layers cancelled the picker, and some found it crashed there. *Learned:* the old WAVE presets all sat in the first 40% of their wavetables, where the Distorted tables are close to a sine and the PWM ones are dull, and every pad came from one family of tables. Measuring each table's brightness along its length and starting where it has body fixed them. If you had presets loose in `SYNTHS/DX7`, move them into a category.

- **v1.32: BRIBELUGE COMPANION.** A phone or tablet companion screen over USB (see [BRIBELUGE COMPANION](#27-bribeluge-companion)). Also: ULTRAKIK and XIA on a single row from SHIFT + KIT, kit types in the order Kit, Cycles, LXR, GIN; the 303 as a synth type; affect all on any kit; the DX7 engine always on; synth categories LEAD first; the synth browser picks up where you left a category; 199 more BRUNO106 presets and 26 more LXR kits. *Fixed:* SHIFT + the pulse width pad on a sample oscillator flashed **CANT** before opening Start offset. *Why:* the 7-segment display shows four letters at a time, and a tablet next to it can show everything else. *Learned:* the 7-segment texts are stored once and shared: one **BASS** serves the synth category and Bass Probability, and **FX** is the end of "Kit FX". So the companion only spells a word out when it knows which setting asked for it, never by matching the letters. Menu items read whatever sound the editor last opened, and asking one for its name outside the editor froze the Deluge, so the companion reads settings straight from the sound.

- **v1.31: BRUNO106.** A Juno-style poly engine from Ultramaster KR-106, with its IR3109 filter in every LPF list, the Juno-106's HPF with bass boost on the track, and BRUNO CHORUS as a Mod FX type with its mode menu and an on / off pad. On BROPHET and BRUNO106, Mod rate and Mod depth are now the Deluge's vibrato, as on any synth. *Why:* the Juno sound next to BROPHET in the palette, at no more CPU a voice. *Learned:* KR-106's filter solves every stage's saturation with a Newton step, about 13 divides a sample, and the Deluge's A9 waits on each one: it cost about 2100 ns a voice. Keeping the feedback stage's saturation and running the four stages clean matched the original within 0.1 dB at normal levels and brought it to about 1300, and moving the DCO's phase to integers took out the float compares that stall the A9.

- **v1.30: Pan spread.** Each note of a poly synth takes its own place in the stereo field: alternating, by key, random or ping pong, on the PAN pad's second layer. *Why:* unison spread only spreads one note's copies, and I wanted a chord spread out like the Prophet '08's voices. *Learned:* the Deluge already had a path where each voice pans itself, used only when something is patched to Pan, so spread is that path plus one number per voice set at note-on.

- **v1.29: Knob button LEDs.** Pressing a shortcut pad blinks the button of the gold knob that edits the same setting, the reverse of the gold knob buttons flashing their pads. *Why:* to learn which pads sit on the knobs from either side. *Learned:* the knob layouts already live in one table per sound, so the lookup is twelve comparisons on a press and costs the audio nothing.
- **v1.28: BROPHET.** A two-oscillator poly engine from Pro-54, the open source port of NI's Pro-53, with its filter in every LPF list and all 512 Pro-53 programs in the synth browser. BRINGS and BROPHET now lay out on the OSC1, OSC2 and FM MOD pads by their labels, and glow purple. *Why:* Pro-54's release put a classic poly voice in the open, written for 2002 CPUs. *Learned:* Cmajor starts every variable at zero and C++ doesn't, so the first translation left two of sync's anti-aliasing terms holding junk. The first CPU pass took an 8-note chord from 64% to 59%; a second one, which swapped float compares for NEON tricks in the middle of the oscillator maths, measured slower and was rolled back.
- **v1.27: Crush types, BRINGS and scrolling names.** **Crush type** sets how Bitcrush and Decimation sound: Hard, Vintage, u-Law, Jitter, or Classic for the original. The BRIB synth type is now **BRINGS** (folder `SYNTHS/BRINGS`: rename yours), and 7-segment context menu options longer than four letters blink, then scroll. *Why:* the stock Decimation smoothed between samples, so turning it up sounded like closing a cheap low pass filter, and Bitcrush had only eight steps, a DC offset and volume drops. *Learned:* at half the knob, the stock Decimation had about 20 dB less top end above 6 kHz than a true sample and hold. Airwindows DeRez3 was considered and dropped: its curved rebuild between samples is smoother still.
- **v1.26: Synth browser and Feedback.** SHIFT + SYNTH became a full browser: type, then BASS, LEAD, PAD or MISC, then presets playing as you turn, with 99 wavetable presets on the free BVKER tables and 37 BRIBERING MODE presets, plus a tool to sort your own. New **Feedback** control on every synth. *Why:* the v1.16 picker (Deluge, DLFM, DX7) only loaded one folder's first preset, so finding a sound meant scrolling hundreds of files by name. *Learned:* the first WAVE presets had the filter half closed, which hid what makes each wavetable different, so they're wide open now except where the sweep is the sound (basses, plucks). Their CUSTOM 2 and 3 both moved the wavetable position and felt like one knob, so CUSTOM 3 became Feedback. If your default synth was DX7, pick it again: the setting's list changed.
- **v1.25: BRIBERING MODE.** A resonator synth engine on the DSP of Mutable Instruments Rings: five models, Bow and Poly. *Why:* Rings-style strikes and strings, polyphonic, inside the Deluge's own voices and FX. *Learned:* sympathetic and chord voices with four strings each cut out when four notes played at once, purely from CPU, so Poly trades voices for strings the way the module does: 4 voices of 2 strings by default, or 2 of 4.
- **v1.24: MIDI loop tracks.** LOOP tracks and ECHO. *Why:* a MIDI track sends what it receives straight back out, so looping a synth with local control on played every note twice.
- **v1.23: community firmware 1.3.0.** Rebuilt on the final 1.3.0 release, with its fixes; added MKIT, CV2 lock, Elektron P-locks and track types in song view; a kit row's MIDI out moved up the menu. *Fixed:* mono sequencer clips load whole again: from v1.2 to v1.22.2 loading one lost the rest of the clip and every clip after it (E044). *Learned:* some gear ignores a MIDI note that ends the moment it starts, so one-shot rows hold theirs for 12 ms.
- **v1.22.2: Gate out on one press.** GATE first in a row's menu, CV clips keep off the kit's gates, kick engines send full to the sidechain. *Why:* the gate took a menu dive, and a CV clip could fight a kit row for the same gate.
- **v1.22.1: 303 Drive and Decay.** Drive became an overdrive after the filter, and Decay changes the sound across its whole knob. *Learned:* driving DIRT's own clipper squashed the resonance and jumped in level, and Decay barely changed a 16th-note pattern above half way.
- **v1.22: DIRT and Gate out.** A saturating 303 filter, and kit rows on the gate outputs. *Why:* Open303 leaves the 303's filter saturation out, so high resonance rang clean instead of growling.
- **v1.21: ULTRAKIK.** A kick engine with sixteen presets. *Fixed:* songs with named kits came up CORRUPTED from v1.12, because the kit's name was read as its preset entry. Nothing on the card was damaged.
- **v1.20: Pad names.** A held shortcut pad scrolls its full name on the 7-segment display. *Why:* four-letter codes are hard to learn.
- **v1.19: Default instruments.** New tracks start as a chosen kit or synth; SELECT steps an LXR, Cycles or GIN kit through its presets.
- **v1.18: Cycles engines for less.** Sines from a lookup table, about a third to a quarter of the cost. *Learned:* working out every sine every sample was most of what the Cyc engines cost.
- **v1.17: Lighter on the CPU.** *Learned:* every voice carried the drum synths' memory whether it used it or not, about seven times a stock voice, so the Deluge cut notes on ordinary songs. Now only drum rows carry it, drum tails end at -72 dB, and quiet tails are cut first.
- **v1.16.3: No more freezes** when a busy song with a 303 ran out of CPU. *Learned:* the voice culling read from an empty voice list.
- **v1.16.2:** Pad Guides glow stays on with SHIFT held in a menu, and new synths no longer come up as an unsaved 303.
- **v1.16.1:** Saturation drive can go on a gold knob, be automated and MIDI learned; mono clips always play in scale mode.
- **v1.16: One drum pad layout.** Every engine's settings on MOD1 and MOD2 in one standard layout, Pad Guides, and the first synth instrument picker. *Why:* each engine had its own pad map to remember.
- **v1.15.1:** The mono sequencer grid no longer jumps an octave.
- **v1.15: Affect all.** Plus Custom 1 tune on preset kits, Cyc Kik and Perc Contour.
- **v1.14:** Drum synth settings in the mod matrix and automation view.
- **v1.13: GIN.** A PO-32 style drum voice with sixteen kits built in.
- **v1.12: Kit presets.** Cycles and LXR preset banks, rows added from empty pads, one drum envelope.
- **v1.11:** Cycles-style controls for the 303 and every drum engine; LXR and Cycles kits on SHIFT + KIT.
- **v1.10:** Delay tone, and feedback and tone on the delay pads.
- **v1.9:** Delay feedback on its own control. *Why:* the stock Amount set both how loud the echoes are and how many come back.
- **v1.8:** Cyc drum engines, one drum pad layout, Stumble on for new songs.
- **v1.7.1:** The mono sequencer grid follows octave transposes.
- **v1.7:** 303 synth and mono sequencer slide.
- **v1.6:** Sample start offset, ported from Owlet.
- **v1.5:** Saturation. *Why:* the stock saturation squashed hard at its lowest and got quieter as you turned it up.
- **v1.4:** Drum synth.
- **v1.3:** Endless Record.
- **v1.2:** Mono sequencer for synth, MIDI and CV tracks.
- **v1.1:** Kit pattern mode, Autofill and the swing shortcuts.
- **v1:** The community beta with Stumble swing.

[Back to top](#readme-top)

## Design and credit

Bribeluge stands on other people's work. The Deluge and its firmware were made by Rohan Hill and Synthstrom Audible, who open sourced the firmware. The [Deluge Community Firmware](https://delugecommunity.com/) this build is based on was written by [its contributors](https://github.com/SynthstromAudible/DelugeFirmware/graphs/contributors): volunteers who spent years getting the code to a point where additions like these are possible. Everything in the firmware that isn't described here is theirs.

The additions described here were designed by [thisisbribery](https://github.com/thisisbribery), on these sources:

- **The swing styles** came out of a swing visualiser built to study and sketch shuffle timings ([stolperbeats_v2](https://www.thisisbribery.com/stolperbeats/visualiser/)). DEEP, SQEZ and FOLD are original designs. HOPP follows the well-known MPC and Linn swing ladder (around 54, 58, 62, 66 and 71%), placed on whole ticks the way a 96 PPQN drum machine would.
- **Autofill's five fills** were first designed and played as an experimental mod on my own Stolperbeats module, then ported here.
- **The Mono sequencer** is an original design for writing basslines on the Deluge.
- **Endless Record** reuses the Deluge's own linear recording, started from the RECORD button while playing.
- **Saturation** is an original design: five antialiased curves on a single drive control with no level compensation, so it behaves like an overdriven input stage.
- **The 303 synth's** voice is ported from [Open303](https://github.com/RobinSchmidt/Open303) by Robin Schmidt (MIT licence), in single precision so it runs on the Deluge. Its Deluge integration, controls and the mono sequencer's slide steps were designed for this build, and so is the DIRT filter: Open303's filter with a saturating input stage added.
- **Gate out** is an original design for this build, using the Deluge's own gate outputs. A kit row's MIDI out is the community firmware's own; v1.23 moves it up the menu and holds one-shot notes long enough to be seen.
- **MIDI loop tracks** are an original design for this build, on the Deluge's own MIDI tracks and Endless Record.
- **BRIBERING MODE's** resonators, exciters and models are ported from the open source firmware of [Mutable Instruments Rings](https://github.com/pichenettes/eurorack) by Emilie Gillet (MIT licence), with its copyright and licence notice kept in the source. The port runs one Rings voice per Deluge voice at 44.1 kHz, rewritten on NEON for the Deluge's CPU. Its Deluge integration, controls, Bow and Poly were designed for this build.
- **MIDI kits, CV2 lock, Elektron P-locks and the song view track types** are original designs for this build. MKIT rows are the Deluge's own MIDI rows; Elektron P-locks keep locks to their steps using the Deluge's own automation. Elektron is named for the behaviour only; no Elektron code or data is used.
- **The sample start offset** is ported from the open source [Owlet Deluge firmware](https://github.com/owlet-labs/DelugeFirmware) (GPL-3.0). This build adds saving the offset with songs and presets, the 7-segment menus, automation view support and the pulse width pad shortcut, and leaves out Owlet's other sampler features.
- **Affect all** is an original design: a temporary snapshot of a kit that every drum moves through together, put back on the bar line.
- **Pad Guides, the standard drum pad layout and the synth browser** are original designs for this build. The browser reuses the Deluge's own preset browsing.
- **Feedback** is an original design for this build, inside the Deluge's own filters.
- **BROPHET's** oscillators, poly mod, mixer and filter are ported from [Pro-54](https://github.com/cmajor-lang/cmajor/tree/main/examples/patches/Pro54) by Cmajor Software (GPL-3.0), which opened up Native Instruments' Pro-53; its copyright and licence notice are kept in the source. The 512 programs come from the preset bank Pro-54 ships, converted for the Deluge. The Deluge integration, controls, drive and the 24 BRIB presets were made for this build.
- **BRUNO106's** DCO, IR3109 filter, HPF with bass boost and BBD chorus are ported from [Ultramaster KR-106](https://github.com/kayrockscreenprinting/ultramaster_kr106) by Karl LaRocca (GPL-3.0); its copyright and licence notice are kept in the source. The filter's stages run without their per-stage saturation, and the chorus leaves out KR-106's modelled noise, clicks and hum. The Deluge integration, controls, BRUNO CHORUS as a Mod FX type and 13 of the presets were made for this build; the other 199 are converted from the preset data KR-106 ships (its factory bank and David Churcher's patch library), under the same GPL-3.0.
- **Master clip** and **SHIFT** are ported from KALI SMASH, my own firmware for the dsp.coffee Kali, and relicensed under GPL-3.0 for this build: the clip curves from its SQUASH section, run here at twice the sample rate, and the frequency shifter from its MOTION section, rebuilt for 44.1 kHz. Its Hilbert pair is Olli Niemitalo's published allpass design. The limiter, the click-free switching and the Deluge integration were made for this build.
- **The Decay crush type's** sputters, stutters and sags and its level-riding grit come from the BBD character in Seal Eggs, my own firmware for the Sealegs, relicensed under GPL-3.0 for this build; its BBD clock is an original design for this build.
- **Crush types** are an original design for this build. u-Law uses the segmented μ-law companding of the G.711 telephone standard, the scheme Mutable Instruments Clouds and Beads use for their lo-fi modes.
- **The WAVE presets** were made for this build and play the free [BVKER Custom Wavetables](https://bvker.com/free-serum-wavetables/) pack, which isn't included here: all credit for the wavetables goes to BVKER. The BRINGS presets were made for this build.
- **The DX7 presets** are voices from the DX7 patch collection on [Dave Benson's DX7 page](https://homepages.abdn.ac.uk/d.j.benson/pages/html/dx7.html), converted for the Deluge's DX7 engine. The first are Yamaha's original DX7 ROM cartridges, and the sounds belong to Yamaha and the collection's patch authors. The picker's DX7 init was made for this build.
- **Delay feedback and tone** are small changes to the Deluge's own delay: each echo is scaled twice, once for what you hear and once for what goes back into the delay, and passes through a one-pole DJ filter on its way out of the delay line.
- **The Cycles presets** are my own Model:Cycles kits, made on my own machine and converted for the Cyc engines.
- **The LXR presets** are sixteen kits by **Hrtl**, released free by Erica Synths for the LXR-02 ([Fresh kits and patterns for the LXR-02 from Hrtl!](https://www.ericasynths.lv/news/fresh-kits-and-patterns-lxr-02-hrtl/), [Hrtl on SoundCloud](https://soundcloud.com/hrtl)), ten kits by **EntropiaLabs** from [ELABS RLX](https://github.com/mcamaradev/ELABS-RLX-02-LXR02-CLONE-VST) (GPL-3.0), both converted for the drum synth, and sixteen kits made for this build. Credit for those sounds goes to Hrtl and EntropiaLabs.
- **BRIBELUGE COMPANION** is an original design for this build: a web page on Web MIDI, and SysEx messages the firmware sends next to the community firmware's display mirror.
- **The drum synth's** layout, controls and Deluge integration were designed for this build. Its kick / tom, snare and cymbal / hat voices are a modified version of the drum voices in the open source LXR-02 firmware by Erica Synths (GPL-3.0). DXIA and DIIA were written from scratch, from the manuals and published descriptions of Noise Engineering's BIA and IIA modules, first for the Elektron Model:Cycles and then ported to the Deluge. The Cyc engines are original code, modelled on how the Model:Cycles and Syntakt machines respond, measured knob by knob; no Elektron code or data is used.
- **TRIBE** is original code for this build. Both ends of every voice were fitted, by rendering and measuring, to free recordings of a real TR-808 (Michael Fischer, 1994) and TR-909 (Rob Roy, 1995); the recordings were only measured and nothing of them is included. It was checked against open source models of both machines (9W9, Drum9, iO-808, Niner), with no code from them, and its extras follow the published descriptions of Hexinverter's Mutant BD9, Mutant Bassdrum and Mutant Snare.
- **GIN's** voice is ported from the MIT licensed synthesis core of [GIN by SquareWave Studio](https://github.com/squarewave-studio/op1-mods) and [libpo32 by Eric Lewis](https://github.com/ericlewis/libpo32), with their copyright and licence notices kept in the source. The sixteen GIN kits, the controls and the Deluge integration were made for this build; GIN's own factory kits are not used.
- **The ideas behind the swing, pattern and fill features were inspired by the Stolperbeats Eurorack module by [Making Sound Machines](https://makingsoundmachines.com/stolperbeats/),** which shuffles beats on tuplet grids and stores patterns in banks. None of its firmware, timing tables, factory timings (Trip, Shake, Push and Clave) or factory patterns are used or included here.

[Back to top](#readme-top)

## Not affiliated or endorsed

This is an independent, unofficial project. It is not affiliated with, endorsed by or supported by **Making Sound Machines**, **Synthstrom Audible**, **Erica Synths**, **Hrtl**, **EntropiaLabs**, **Elektron**, **Roland**, **SquareWave Studio**, **Teenage Engineering**, **Sonic Charge**, **Mutable Instruments**, **Native Instruments**, **Noise Engineering**, **Cmajor Software**, **Sequential**, **Karl LaRocca (Ultramaster KR-106)**, **dsp.coffee**, **Michigan Synth Works**, **Hexinverter** or **BVKER**. Stolperbeats is a product of Making Sound Machines, the Deluge is a product of Synthstrom Audible, the LXR-02 is a product of Erica Synths, the Model:Cycles and Syntakt are products of Elektron, the TB-303, Juno-106, TR-808 and TR-909 are products of Roland, the Mutant drum modules are products of Hexinverter, the OP-1 and PO-32 are products of Teenage Engineering, Rings is a product of Mutable Instruments, Pro-53 is a product of Native Instruments, the Prophet-5 is a product of Sequential, the Kali is a product of dsp.coffee, and the Sealegs is a product of Michigan Synth Works. All trademarks belong to their owners. No rights to the Erica Synths, LXR or LXR-02 trademarks are granted.

Use it at your own risk, and please don't contact Making Sound Machines, Synthstrom Audible, Erica Synths, Elektron, Roland, SquareWave Studio, Teenage Engineering, Mutable Instruments, Native Instruments, Noise Engineering, Cmajor Software, Sequential, Karl LaRocca or BVKER for help with this build.

[Back to top](#readme-top)

## Source code

The Deluge firmware is free software under the GNU General Public License v3, and so is this build.

The complete source of every release is published in three places:

- **The source repo:** [thisisbribery/DelugeFirmware](https://github.com/thisisbribery/DelugeFirmware/tree/bribes), a fork of the community firmware that keeps its full history and contributors. This is the link to share as Bribeluge's source. Branch `bribes` has every change since the first release as separate commits, and each release is tagged (`bribes-v1.32` onwards). Compare it with the community repo: [all Bribes changes against v1.3.0](https://github.com/SynthstromAudible/DelugeFirmware/compare/v1.3.0...thisisbribery:DelugeFirmware:bribes).
- **In this repo:** [`source/DelugeFirmware`](source/DelugeFirmware) is a git submodule pinned to the exact commit each bin was built from. Clone with `git clone --recursive https://github.com/thisisbribery/deluge-bribes-v1.git` to get it all.
- **Download:** the full source tree as a `.tar.gz`, next to the bin on each [release](https://github.com/thisisbribery/deluge-bribes-v1/releases).

The same changes as a single patch on the official firmware:

- **Base:** [SynthstromAudible/DelugeFirmware](https://github.com/SynthstromAudible/DelugeFirmware) at the `v1.3.0` tag (commit `156500e7c`, community firmware 1.3.0), plus the fixes on the community's `release/1.3` branch up to `ff14b0762`. Up to v1.22.2 the base was commit `a616dd8e`, the 1.3 beta.
- **Changes:** [`source/stumble-swing.patch`](source/stumble-swing.patch)

To build it yourself (or check out `v1.3.0` from the official repo and `git apply` the patch):

```bash
git clone -b bribes https://github.com/thisisbribery/DelugeFirmware.git
cd DelugeFirmware
./dbt configure
./dbt build release
```

The firmware is written to `build/Release/deluge.bin`.

### Measuring CPU and memory

For anyone working on the firmware's performance. From v1.49, over USB, the Deluge streams its render load, its slowest render, voices playing and voices cut, free on-chip RAM and SDRAM, the time each engine's voices take, and the time spent in each part of the render (kit rows, kit FX, reverb, song FX and the rest). It can also list every block of memory in use, grouped by size. Nothing is sent or timed unless a computer asks for it.

[`tools/deluge_bench.py`](tools/deluge_bench.py) reads it on a computer (Python 3 with `mido` and `python-rtmidi`): a live readout, a timed run that starts the song and saves the results, a voice count sweep, memory snapshots and maps per kit with the difference between two, and a before and after comparison of two builds on the same song. The protocol is at the top of the script.

[Back to top](#readme-top)

## Licence

GNU General Public License v3.0. See [LICENSE](LICENSE).

[Back to top](#readme-top)
