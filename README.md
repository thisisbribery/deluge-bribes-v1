# Deluge Bribes v1.4

Unofficial firmware for the Synthstrom Deluge, built on the community beta (1.3, Derbyshire). It adds six things for people who want more groove and more wonk:

1. **Stumble swing:** four alternative swing styles with seven levels each, and quick shortcuts on the TEMPO knob.
2. **Kit pattern mode:** a pattern store for the first six rows of a kit. Step each row through saved patterns, load whole banks, and save over them.
3. **Autofill:** TAP plays drum fills over your beat, with five fill types to pick from.
4. **Mono sequencer:** a mono step sequencer for synth, MIDI and CV tracks, with an octave per note, gate control and, on CV, a custom voltage for each row.
5. **Endless Record:** hit RECORD while playing and keep recording past the end of the loop, then stop at the next bar.
6. **Drum synth (new in v1.4):** synthesised drums on any kit row, from five engines: the LXR-02's kick / tom, snare and cymbal / hat voices, and two more called Drom1 and Drom2. The Deluge's envelopes, filters and FX all work on top, and their settings can be parameter locked.

With these settings left at their defaults, the Deluge behaves exactly like the community beta.

**Status: experimental.** Tested on a 7-segment Deluge. The OLED screens are written but not yet tested on hardware. Back up your SD card before installing.

## Download

[`firmware/deluge-bribes-v1.4.bin`](firmware/deluge-bribes-v1.4.bin)

SHA-256: `d990199923238bda9ae8b9275df7f1e03302abd7fccd4bd847927c5ab8d347bc`

## Install

1. Copy `deluge-bribes-v1.4.bin` to the top level of the Deluge's SD card. Remove any other `.bin` files from the top level.
2. Turn the Deluge off.
3. Hold **SHIFT** and switch the Deluge on. Let go once it starts loading the new firmware.

To go back, install an official firmware file the same way.

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
| **Hold a row's audition pad + turn the lower gold knob** | Set that row's voltage (Mono sequencer, CV CUSTOM) |
| **RECORD while playing** | Start recording an empty playing clip with no loop limit (Endless Record on) |
| **RECORD again** | Stop recording at the next bar. RECORD blinks until then; press it again to keep going (Endless Record on) |
| **SHIFT + KIT** | New kit: choose **Kit** (samples) or **Drum synth** (seven synthesised rows) |
| **Hold a row's audition pad + SYNTH MODE pad** | Put the row on a drum synth engine (Drom1, Drom2 or Drum synth), or back to **Sample** |
| **Hold a row's audition pad + OSC1 TYPE pad** | Pick the engine's variant or LXR voice (drum synth rows) |
| **CUSTOM 2 / CUSTOM 3 gold knobs** | The engine's two key settings (drum synth rows). Hold a step and turn to parameter lock |

7-segment display names are in brackets below.

## 1. Stumble swing

The Deluge's own swing pushes every second 16th later by one amount. Stumble swing replaces it with four styles that move the notes in different shapes, each with seven levels.

### Turning it on

1. Press **SONG**, then press the **SELECT** knob to open the Song menu.
2. Turn to **Stumble** (**STUM**) and press **SELECT** to switch it on.
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

## 4. Mono sequencer

Turns a synth, MIDI or CV track's grid into a mono step sequencer, built for basslines. The notes are ordinary Deluge notes, so clip length, nudging, ratchets (note repeat), copy and paste, undo and saving all work as normal.

### Turning it on

1. Open the clip's menu (press **SELECT** in the clip).
2. Turn **Mono Seq** (**MSEQ**) on. On synths it sits near the end of the menu, after Sequence Direction.

Mono is a setting on the clip, so it carries over if you switch the track between Synth, MIDI and CV.

### How it works

- **8 fixed rows:** the scale's first 8 steps from the song's root, root at the bottom. With a 7-note scale that's one octave plus the root an octave up. The grid doesn't scroll up or down.
- **One note per column:** placing a note clears that column on the other rows.
- **Octaves:** hold a note and turn the up/down knob (without pressing it) to shift it up to 4 octaves either way. The display shows the note it now plays, e.g. **D#5**, and you hear it.
- **Ratchets:** hold a note, then press and turn the up/down knob. This is the Deluge's normal note repeat.
- **Holding a note** shows and sounds the note it actually plays, octave included.
- **Gate %** (**GATE**), in the same menu, shortens every note's gate, from 1 to 100% of its drawn length. Notes still keep their own lengths.

### Colours

| Pad | Means |
|---|---|
| White | A note in its own octave |
| Red, deeper per octave | Shifted up 1 to 4 octaves |
| Blue, deeper per octave | Shifted down 1 to 4 octaves |
| Orange tint | Edited: nudged, ratcheted, or given a probability, iterance or fill |
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

## 6. Drum synth

Synthesised drums as a Deluge oscillator. A drum synth row is still a normal Deluge sound: its envelopes, filters, FX, mod matrix, automation and parameter locks all work on top.

There are five engines:

- **Kick / tom** (**DRUM**), **Snare** (**SNAR**) and **Cymbal / hat** (**METL**): ported from the drum voices of the open source LXR-02 firmware by Erica Synths. Choose them together as **Drum synth** (**DRUM**).
- **Drom1** (**DRM1**): three sine operators and a carrier, phase modulating each other in three routings, **L**, **B** and **C**.
- **Drom2** (**DRM2**): inharmonic, metallic partials with a noise strike, in three variants, **G**, **I** and **H**.

### Making a drum synth kit

1. In clip view on an empty clip, press **SHIFT + KIT**.
2. The **New kit** (**NEW**) menu opens. Turn **SELECT** to **Drum synth** (**DRUM**) and press **SELECT**. Choose **Kit** for a normal, sample based kit.
3. You get seven rows, from the bottom: **KICK**, **SNARE**, **CH** (closed hat), **OH** (open hat), **LTOM**, **HTOM** and **CYM**. The two hat rows choke each other.

### Changing one row

Any row of any kit, or any synth, can switch engine:

1. Hold the row's audition pad and press the **SYNTH MODE** shortcut pad.
2. Choose **Drom1**, **Drom2** or **Drum synth**. On a kit row the first option reads **Sample** (**SAMP**): choose it to put the row back on its sample.

A row that wasn't a drum synth gets a percussive envelope (attack 0, decay 30, sustain 0, release 30), so each hit decays even if you let go early. Envelope 2 is set to a short blip (attack 0, decay 5, sustain 0, release 0): patch it to pitch for a transient snap.

### Shortcut pads

On a drum synth row the shortcut grid reads like an FM synth. The **OSC1** column is the drum voice, and the **OSC2** and **MOD** columns are its other parts. **OSC1 TYPE** picks the variant: L, B or C on Drom1, G, I or H on Drom2, or kick / tom, snare or cymbal / hat on the LXR voices.

| Pad | Kick / tom | Snare | Cymbal / hat | Drom1 | Drom2 |
|---|---|---|---|---|---|
| OSC1 PULSE WIDTH | Osc wave | Osc wave | Osc wave | | Shape |
| OSC1 RETRIGGER | Transient type | Transient type | Transient type | Punch | Punch |
| OSC1 FEEDBACK | Transient level | Transient level | Transient level | Drive | Drive |
| OSC1 WAVE INDEX | Transient speed | Transient speed | Transient speed | Engine decay | Engine decay |
| OSC2 LEVEL | FM amount | Noise mix | FM amount | Blendex 1 | Alloy |
| OSC2 TRANSPOSE | Mod pitch | Noise rate | Mod pitch | Freq 1 | Weight |
| OSC2 TYPE | Mod wave | Noise filter | Mod wave | | |
| OSC2 PULSE WIDTH | Mod fine | Noise cutoff | Mod fine | | |
| OSC2 RETRIGGER | FM / mix | | | | |
| OSC2 FEEDBACK | | Noise resonance | | | |
| MOD1 LEVEL | Pitch decay | Pitch decay | FM 2 amount | Blendex 2 | Strike |
| MOD1 TRANSPOSE | Pitch amount | Pitch amount | Mod 2 pitch | Freq 2 | |
| MOD1 TYPE | | | Mod 2 wave | | |
| MOD1 PULSE WIDTH | | | Mod 2 fine | | |
| MOD1 FEEDBACK | Pitch curve | Pitch curve | | | |
| MOD2 LEVEL / TRANSPOSE | | | | Blendex 3 / Freq 3 | |

The other shortcuts keep their usual jobs.

- **Blendex** moves a Drom1 operator from being heard (0) to modulating (127). **Freq** tunes it, from 24 semitones down, through unison at 64, to 24 up.
- **Weight** picks Drom2's partial ratios, **Alloy** their levels, **Shape** their waveform (sine to triangle to square to saw), and **Strike** the noise burst at the start of each hit.
- **Engine decay** is Drom1 and Drom2's own decay on top of the Deluge envelope. It starts at 127, which holds, so the Deluge envelope does the shaping.

### Gold knobs

**CUSTOM 1** tunes the drum. **CUSTOM 2 / CUSTOM 3** carry each engine's two key settings: pitch amount / FM amount (kick / tom), noise mix / pitch amount (snare), FM amount / FM 2 amount (cymbal / hat), Blendex 1 / Freq 1 (Drom1), Weight / Alloy (Drom2). The other gold knobs keep their Deluge jobs.

Every continuous drum synth setting is a Deluge parameter, so it can be parameter locked (hold a step and turn) and automated. They can't yet be modulated from the mod matrix.

### Snappy decay

**Snappy decay** (**SNAP**), in the sound menu of any drum synth row, makes the amp envelope's decay and release follow a steeper curve: tighter hits, and the same decay setting sounds about half as long. It's off by default and saved with the row.

### Good to know

- The full settings list and a pad-per-setting editor are in the sound menu under **Drum synth** (**DRUM**). **Load preset** (**PRST**) there has the seven kit sounds and each Drom variant.
- **SHIFT + press SELECT > CPU load** (**LOAD**) shows the audio engine's load, for checking how many drum synth voices you can run.
- Kits with drum synth rows won't play those rows on firmware without them.
- The full reference is in the source patch, at `website/src/content/docs/features/drum_synth.mdx`.

## Design and credit

Everything here was designed by [thisisbribery](https://github.com/thisisbribery).

- **The swing styles** came out of a swing visualiser built to study and sketch shuffle timings ([stolperbeats_v2](https://thisisbribery.github.io/stolperbeats_v2/)). DEEP, SQEZ and FOLD are original designs. HOPP follows the well-known MPC and Linn swing ladder (around 54, 58, 62, 66 and 71%), placed on whole ticks the way a 96 PPQN drum machine would.
- **Autofill's five fills** were first designed and played as an experimental mod on my own Stolperbeats module, then ported here.
- **The Mono sequencer** is an original design for writing basslines on the Deluge.
- **Endless Record** reuses the Deluge's own linear recording, started from the RECORD button while playing.
- **The drum synth's** layout, controls and Deluge integration were designed for this build. Its kick / tom, snare and cymbal / hat voices are a modified version of the drum voices in the open source LXR-02 firmware by Erica Synths (GPL-3.0). Drom1 and Drom2 are ported from an open source engine set written for the Elektron Model:Cycles.
- **The ideas behind the swing, pattern and fill features were inspired by the Stolperbeats Eurorack module by [Making Sound Machines](https://makingsoundmachines.com/stolperbeats/),** which shuffles beats on tuplet grids and stores patterns in banks. None of its firmware, timing tables, factory timings (Trip, Shake, Push and Clave) or factory patterns are used or included here.

## Not affiliated or endorsed

This is an independent, unofficial project. It is not affiliated with, endorsed by or supported by **Making Sound Machines**, **Synthstrom Audible**, **Erica Synths** or **Elektron**. Stolperbeats is a product of Making Sound Machines, the Deluge is a product of Synthstrom Audible, the LXR-02 is a product of Erica Synths, and the Model:Cycles is a product of Elektron. All trademarks belong to their owners. No rights to the Erica Synths, LXR or LXR-02 trademarks are granted.

Use it at your own risk, and please don't contact Making Sound Machines, Synthstrom Audible, Erica Synths or Elektron for help with this build.

## Source code

The Deluge firmware is free software under the GNU General Public License v3, and so is this build. The full source is the official firmware plus one patch:

- **Base:** [SynthstromAudible/DelugeFirmware](https://github.com/SynthstromAudible/DelugeFirmware) at commit `a616dd8e` (the `beta` tag, Deluge beta Release 20261016).
- **Changes:** [`source/stumble-swing.patch`](source/stumble-swing.patch)

To build it yourself:

```bash
git clone https://github.com/SynthstromAudible/DelugeFirmware.git
cd DelugeFirmware
git checkout a616dd8e
git apply /path/to/stumble-swing.patch
./dbt configure
./dbt build release
```

The firmware is written to `build/Release/deluge.bin`.

## Licence

GNU General Public License v3.0. See [LICENSE](LICENSE).
