# BRIBELUGE: Deluge Bribes FW v1.15

Unofficial firmware for the Synthstrom Deluge, built on the community beta (1.3, Derbyshire). It adds things for people who want more wonk, more destruction, more speed, moarrrrr:

1. **Stumble swing:** four alternative swing styles with seven levels each, and quick shortcuts on the TEMPO knob. New songs start on Stumble, SQEZ style (new in v1.8).
2. **Kit pattern mode:** a pattern store for the first six rows of a kit. Step each row through saved patterns, load whole banks, and save over them.
3. **Autofill:** TAP plays drum fills over your beat, with five fill types to pick from.
4. **Mono sequencer:** a mono step sequencer for synth, MIDI and CV tracks, with an octave per note, slide steps (new in v1.7), gate control and, on CV, a custom voltage for each row.
5. **Endless Record:** hit RECORD while playing and keep recording past the end of the loop, then stop at the next bar.
6. **Drum synth:** synthesised drums on any kit row: the LXR-02's kick / tom, snare and cymbal / hat voices, DXIA and DIIA, and eight Cyc engines modelled on the Model:Cycles and Syntakt machines (new in v1.8). Every engine is picked in SYNTH MODE and shares one shortcut pad layout and one Cycles-style gold knob layout, and SHIFT + KIT makes a whole LXR or Cycles kit (new in v1.11), then browses its presets with the pattern running, sixteen Cycles kits of my own and sixteen LXR kits by Hrtl included (new in v1.12). New in v1.13: **GIN**, the PO-32 style drum voice from SquareWave Studio's GIN for the OP-1, with sixteen eight-sound kits built in. The Deluge's envelopes, filters and FX all work on top, and their settings can be parameter locked. New in v1.14: every engine's settings can be modulated from the mod matrix, and automation view's grid follows the drum synth pads.
7. **Saturation:** the Deluge's saturation rebuilt as a one-knob drive that gets louder and denser as you turn it up, ending in a hard clip, with five curve types. Old songs keep the original sound.
8. **Sample start offset:** move where a sample starts playing, per step. Draw it in automation view, parameter lock it or modulate it, and it wraps around the sample, loops included.
9. **303 synth (new in v1.7):** a TB-303 style bass voice as a synth mode, ported from the open source Open303. It plays from the mono sequencer, with accent and slide per step, and runs through the Deluge's saturation and FX. Its knobs follow the drum synth layout, with its own drive and amp decay (new in v1.11).
10. **Delay feedback and tone:** the delay's amount and feedback on separate controls (new in v1.9), and a DJ-style filter in the delay loop (new in v1.10). Amount sets how loud the echoes are, Feedback how many come back, and Tone darkens or thins each repeat. Both live one layer under SHIFT: on the gold knobs, or press the delay pad twice.
11. **Affect all (new in v1.15):** a performance snapshot for LXR, Cycles and GIN kits. SHIFT + AFFECT ENTIRE freezes the kit, then every gold knob turn moves all the drums at once, or the kit's FX, and SHIFT + AFFECT ENTIRE again snaps it all back on the next bar.

With these settings left at their defaults, the Deluge behaves exactly like the community beta, except that new songs start on Stumble swing (still straight until you turn the swing up), and the delay's feedback has its own setting (the tone starts flat). Songs saved before keep their own swing and sound the same through the delay.

**Status: experimental.** Tested on a 7-segment Deluge. The OLED screens are written but not yet tested on hardware. Back up your SD card before installing.

## Download

[`firmware/deluge-bribes-v1.15.bin`](firmware/deluge-bribes-v1.15.bin)

SHA-256: `8a95bbcccb8dc074d7134ec7c643bc101ab0b09779ab8b2ee8475e30af1c0528`

Presets (optional): copy [`presets/KITS/CYCLES`](presets/KITS/CYCLES) and [`presets/KITS/LXR`](presets/KITS/LXR) to `KITS/CYCLES` and `KITS/LXR` on the SD card. The GIN kits are built into the firmware.

## Install

1. Copy `deluge-bribes-v1.15.bin` to the top level of the Deluge's SD card. Remove any other `.bin` files from the top level.
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
| **Hold a note + click the up/down knob** | Slide on or off for that step (Mono sequencer) |
| **Hold a row's audition pad + turn the lower gold knob** | Set that row's voltage (Mono sequencer, CV CUSTOM) |
| **RECORD while playing** | Start recording an empty playing clip with no loop limit (Endless Record on) |
| **RECORD again** | Stop recording at the next bar. RECORD blinks until then; press it again to keep going (Endless Record on) |
| **SHIFT + KIT** | New kit: choose **Kit** (samples), **LXR** (the seven LXR voices), **Cycles** (the six Cyc engines) or **GIN** (eight GIN sounds) |
| **SHIFT + KIT on an LXR, Cycles or GIN kit** | Kit presets: turn SELECT to play each preset on the kit's rows, SELECT to keep, BACK to go back (Drum synth) |
| **Tap an empty audition pad on an LXR, Cycles or GIN kit** | Add a row there and open SYNTH MODE to choose its sound (Drum synth) |
| **Hold a row's audition pad + SYNTH MODE pad** | Put the row on any drum synth engine or variant, or back to **Sample**. On a drum synth row the OSC1 TYPE pad opens the same list |
| **Attack / Release gold knobs** | Drive / Decay (drum synth rows and the 303) |
| **Mod rate / Mod depth gold knobs** | The sweep's speed / depth: Sweep / Contour on the Cyc engines, the filter envelope's Decay / Env mod on the 303 |
| **CUSTOM 2 / CUSTOM 3 gold knobs** | Two voicing settings: Color / Shape on the Cyc engines, Mix / Noise freq on GIN, Accent / Saw-square on the 303. Hold a step and turn to parameter lock |
| **Drum synth setting open + a mod source pad** | Patch that source (LFO, envelope, velocity, random...) to the setting (Drum synth, new in v1.14) |
| **SHIFT + SATURATION pad** | Saturation drive, 0 to 50. Press BACK, then turn SELECT to reach **Type** |
| **SHIFT + OSC1 / OSC2 PULSE WIDTH pad** | Sample start offset, when that oscillator plays a sample |
| **Automation view: OSC1 / OSC2 PULSE WIDTH pad** | Draw the start offset step by step, when that oscillator plays a sample |
| **SYNTH MODE pad, choose 303** | Turn a synth into the 303 (303 synth) |
| **Cutoff/Res and Attack/Release gold knobs** | Cutoff / Resonance and Drive / Amp decay (303 synth) |
| **SHIFT + turn the delay Amount gold knob** | Delay feedback, 0 to 50. The knob on its own still sets the delay amount (Delay feedback and tone) |
| **SHIFT + turn the delay Rate gold knob** | Delay tone: lowpass to the left, flat in the middle, highpass to the right (Delay feedback and tone) |
| **SHIFT + delay AMOUNT pad, press again** | Delay feedback. The pad blinks yellow; press again to go back to Amount (Delay feedback and tone) |
| **SHIFT + delay RATE pad, press again** | Delay tone. The pad blinks yellow; press again to go back to Rate (Delay feedback and tone) |
| **SHIFT + AFFECT ENTIRE on an LXR, Cycles or GIN kit** | Snapshot the kit and move every drum at once. AFFECT ENTIRE flashes (Affect all) |
| **AFFECT ENTIRE during the snapshot** | Swap between All voices (ALL) and the kit's FX (FX), keeping the snapshot (Affect all) |
| **SHIFT + AFFECT ENTIRE again** | Put the snapshot back on the next bar. AFFECT ENTIRE flashes twice as fast until then (Affect all) |

7-segment display names are in brackets below.

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

- **8 fixed rows:** the scale's first 8 steps from the song's root, root at the bottom. With a 7-note scale that's one octave plus the root an octave up. The grid doesn't scroll up or down; it follows your notes instead (see below).
- **One note per column:** placing a note clears that column on the other rows.
- **Octaves:** hold a note and turn the up/down knob (without pressing it) to shift it up to 4 octaves either way. The display shows the note it now plays, e.g. **D#5**, and you hear it.
- **Transposing the whole clip:** press and turn the up/down knob (with no note held) to move every note up or down an octave, as on any synth clip. The 8 rows follow the notes to their new octave, so they stay on the grid (fixed in v1.7.1).
- **Ratchets:** hold a note, then press and turn the up/down knob. This is the Deluge's normal note repeat.
- **Holding a note** shows and sounds the note it actually plays, octave included.
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

The engines:

- **Kick / tom** (**DRUM**), **Snare** (**SNAR**) and **Cymbal / hat** (**METL**): ported from the drum voices of the open source LXR-02 firmware by Erica Synths.
- **DXIA** (**DX-L**, **DX-B**, **DX-C**), called Drom1 before v1.11: three sine operators and a carrier, phase modulating each other in three routings.
- **DIIA** (**DI-G**, **DI-I**, **DI-H**), called Drom2 before v1.11: inharmonic, metallic partials with a noise strike, in three variants.
- **Cyc engines (new in v1.8):** **Cyc Kik** (**KIK**), **Cyc Snr** (**SNR**), **Cyc Metal** (**CMTL**), **Cyc Perc** (**PERC**), **Cyc Tone** (**TONE**), **Cyc Chord** (**CHRD**), **Vtg Snr** (**VSNR**) and **clap eng** (**CLAP**). Modelled on the Model:Cycles' six machines and the Syntakt's SD VINTAGE and CP VINTAGE, with the same knobs and starting values.
- **GIN** (**GIN**, new in v1.13): the drum voice from SquareWave Studio's GIN for the OP-1, built on Eric Lewis's libpo32, a PO-32 style drum synth. A tone with a pitch sweep, LFO or noise modulator, and a filtered noise layer with its own envelope, mixed, driven and EQ'd. See [GIN](#gin-new-in-v113).

### Making a drum synth kit

1. In clip view on an empty clip, press **SHIFT + KIT**.
2. The **New kit** (**NEW**) menu opens. Turn **SELECT** to a kit type and press **SELECT**:
   - **Kit** (**KIT**): a normal, sample based kit.
   - **LXR** (**LXR**): seven LXR voice rows, from the bottom: **KICK**, **SNARE**, **CH** (closed hat), **OH** (open hat), **LTOM**, **HTOM** and **CYM**. The two hat rows choke each other.
   - **Cycles** (**CYCL**, new in v1.11): the Model:Cycles' usual six tracks, from the bottom: **KIK**, **SNR**, **METAL**, **TONE**, **PERC** and **CHORD**, playing at the note as the Cycles does at its default tune.
   - **GIN** (**GIN**, new in v1.13): eight GIN rows, from the bottom: **KICK**, **SNR**, **HAT1**, **HAT2**, **PERC1**, **PERC2**, **CLAP** and **OTHER**, on the 808 kit. The two hats choke each other, and each row is tuned to its sound.

Vtg Snr, clap eng, DXIA and DIIA are picked per row in SYNTH MODE.

The rows an LXR, Cycles or GIN kit makes are its **preset rows** (new in v1.12). Their audition pads are softly coloured by the engine each plays: blue for the Cyc engines, orange for the LXR voices, green for DXIA and DIIA, pink for GIN (brighter on the selected row).

- **Adding rows:** tap an empty audition pad above or below the preset rows and a new row appears there with **SYNTH MODE** open, to make it any engine, **Sample** or FM. Holding the empty pad and pressing **LOAD**, **SYNTH**, **MIDI** or **CV** works as on any kit. Added rows aren't coloured.
- **Swapping kit type:** once rows have been added, a preset kit can't be swapped for another kit (the added rows would lose their sounds): the screen shows **CANT**. Without added rows, the swap keeps the pattern on the rows the new kit fills.

### Kit presets (new in v1.12)

On an LXR, Cycles or GIN kit, **SHIFT + KIT** opens **Kit presets** (**PRST**): the kit files in `KITS/LXR`, `KITS/CYCLES` or `KITS/GIN` on the card.

1. Turn **SELECT**. Each preset plays on the preset rows straight away, pattern running. Notes, added rows and the other rows stay as they are, and the audition pads still play the rows.
2. **SELECT** (or **KIT**) keeps the one showing. **BACK** puts the kit back as it was and goes up to the Kit / LXR / Cycles / GIN menu: its own type goes back into the presets, another swaps the kit.

The list is **Default** (the rows as SHIFT + KIT makes them) and then the presets in name order. On a GIN kit, Default is replaced by GIN's sixteen built in kits, so there's nothing to copy to the card. It opens on the preset the kit is on (kept with the kit when you save), or **Current** if it's on none of them.

- **Cycles presets:** sixteen kits of my own, bank E of my Model:Cycles kits, converted for the Cyc engines: copy [`presets/KITS/CYCLES`](presets/KITS/CYCLES) to `KITS/CYCLES` on the card.
- **LXR presets:** sixteen kits by **Hrtl** from the free [LXR-02 pack Erica Synths released in 2022](https://www.ericasynths.lv/news/fresh-kits-and-patterns-lxr-02-hrtl/), converted for the drum synth: copy [`presets/KITS/LXR`](presets/KITS/LXR) to `KITS/LXR` on the card. Close to the originals rather than identical (see the folder's README).
- **Making presets:** a preset is an ordinary kit file. Set the kit up, press **SAVE**, go into `KITS/LXR`, `KITS/CYCLES` or `KITS/GIN` (made the first time you open the list) and save, over an existing preset or under a new name. Only the preset rows are read back. [`tools/lxr_to_deluge.py`](tools/lxr_to_deluge.py) converts LXR-02 .SND kits.
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

- Each engine you pick starts from its defaults, set up as its kit row is (new in v1.12): transpose, envelopes, filters open (the high pass on for the cymbal), osc 2 and noise off, tune centred, whatever the row was before. So what SYNTH MODE previews is what the kit plays. FX are left alone.
- **Envelopes (new in v1.12):** every drum engine shapes its hits with its own decay (the LXR voices' Decay, DXIA and DIIA's engine decay, the Cyc engines' amp decay). The Deluge envelope around it is open (attack 0, sustain full) with a release long enough for that decay to ring out after the note ends, so one tap plays the whole hit and gated sounds follow the note.
- A row that wasn't a drum synth also gets envelope 2 as a short blip (attack 0, decay 5, sustain 0, release 0) to patch to pitch for a snap.
- **DXIA and DIIA presets (new in v1.12):** each variant starts on a preset, level with the other engines (both are 6 dB louder than before): DXIA L a tight kick, B a knocky kick, C a long deep kick (envelope 2 on pitch drops them from about 200 Hz), DIIA G a snare-ish noise perc, I a zap, H metallic noise.

### Shortcut pads

All drum engines share one layout, read the way the grid is printed. Only the OSC1, OSC2, MOD1 and MOD2 columns change meaning on a drum synth row. Envelope, filter, FX and master pads keep their usual jobs, and so does any pad an engine doesn't use.

- **Columns:** OSC1 is the main voice. OSC2 is the second layer (snare noise, rattle, snares, overtone, clap tail, or the first operator). MOD1 is the modulator: FM depth and ratio. MOD2 is the pitch sweep, or the second modulator or third operator on engines without one.
- **Rows:** LEVEL is an amount, TRANSPOSE a tuning or ratio, TYPE a choice, PULSE WIDTH a shape or the wave, RETRIGGER the attack, FEEDBACK drive, resonance or curve, WAVE INDEX a decay. OSC1 NOISE is a noise amount.
- **Drive and decay:** every engine has its decay on **OSC1 WAVE INDEX**. **OSC1 FEEDBACK** is the drive switch (**Punch**) on the engines that have one, with the drive amount on **OSC1 RETRIGGER** (changed in v1.11); the LXR voices have no switch, so their OSC1 FEEDBACK is the drive amount. On the LXR voices, kits saved before v1.8 load with drive and decay neutral (no drive, decay holding), so they sound the same; from v1.12 new LXR rows start with their decay set, as it shapes each hit.
- **Sweep:** the **MOD FX RATE / DEPTH** pads are the sweep's speed and depth on every engine (new in v1.11 on the LXR voices, DXIA and DIIA).

| Pad | Kick / tom | Snare | Cymbal / hat | DXIA | DIIA |
|---|---|---|---|---|---|
| OSC1 TYPE | SYNTH MODE | SYNTH MODE | SYNTH MODE | SYNTH MODE | SYNTH MODE |
| OSC1 PULSE WIDTH | Osc wave | Osc wave | Osc wave | | Shape |
| OSC1 RETRIGGER | Transient type | Transient type | Transient type | Drive | Drive |
| OSC1 FEEDBACK | Drive | Drive | Drive | Punch | Punch |
| OSC1 WAVE INDEX | Engine decay | Engine decay | Engine decay | Engine decay | Engine decay |
| OSC1 NOISE | | | | | Strike |
| OSC2 LEVEL | | Noise mix | | Blendex 1 | |
| OSC2 TRANSPOSE | | Noise rate | | Freq 1 | |
| OSC2 TYPE | Osc mode (FM / mix) | Noise filter | | | |
| OSC2 PULSE WIDTH | | Noise cutoff | | | |
| OSC2 RETRIGGER | Transient level | Transient level | Transient level | | |
| OSC2 FEEDBACK | | Noise resonance | | | |
| MOD1 LEVEL | FM amount | | FM amount | Blendex 2 | Alloy |
| MOD1 TRANSPOSE | Mod pitch | | Mod pitch | Freq 2 | Weight |
| MOD1 TYPE | Mod wave | | Mod wave | | |
| MOD1 PULSE WIDTH | Mod fine | | Mod fine | | |
| MOD1 RETRIGGER | Transient speed | Transient speed | Transient speed | | |
| MOD2 LEVEL | Pitch amount | Pitch amount | FM 2 amount | Blendex 3 | |
| MOD2 TRANSPOSE | | | Mod 2 pitch | Freq 3 | |
| MOD2 TYPE | | | Mod 2 wave | | |
| MOD2 PULSE WIDTH | | | Mod 2 fine | | |
| MOD2 FEEDBACK | Pitch curve | Pitch curve | | | |
| MOD2 WAVE INDEX | Pitch decay | Pitch decay | | | |
| MOD FX RATE | Pitch decay | Pitch decay | Transient speed | Blendex 2 | Shape |
| MOD FX DEPTH | Pitch amount | Pitch amount | Transient level | Blendex 3 | Strike |

| Pad | Cyc Kik | Cyc Snr | Cyc Metal | Cyc Perc | Cyc Tone | Cyc Chord | Vtg Snr | clap eng |
|---|---|---|---|---|---|---|---|---|
| OSC1 PULSE WIDTH | Shape | Shape (rattle) | | | | Sweep (wave) | | |
| OSC1 RETRIGGER | Drive | Drive | Drive | Drive | Drive | Drive | Drive | Drive |
| OSC1 FEEDBACK | Punch | Punch | Punch | Punch | Punch | Punch | Punch | Punch |
| OSC1 WAVE INDEX | Amp decay | Amp decay | Amp decay | Amp decay | Amp decay | Amp decay | Amp decay | Amp decay |
| OSC2 LEVEL | | | | Color (overtone) | | | Freq complex | Balance |
| OSC2 FEEDBACK | | | | | | | | Body char |
| OSC2 TRANSPOSE | | Color (rattle tune) | | | | Color (voicing) | | Spacing crunch |
| OSC2 TYPE | | | | | | Shape (chord) | | |
| OSC2 PULSE WIDTH | | Shape (rattle) | | | | | | |
| OSC2 RETRIGGER | Contour (knock) | | | | | | | |
| OSC2 WAVE INDEX | | Contour (noise decay) | | Contour (overtone decay) | | | | Body envelope |
| MOD1 LEVEL | | | Shape (density) | Shape (modulation) | Shape (FM index) | | Mod envelope | |
| MOD1 TRANSPOSE | | | Color (ratio spread) | | Color (FM ratio) | | Inharm | |
| MOD1 FEEDBACK | Color (harmonic drive) | | | | | | | |
| MOD1 RETRIGGER | | | | | Sweep (index burst) | | | |
| MOD1 WAVE INDEX | | | Contour (top end decay) | | Contour (index decay) | Contour (wave decay) | | |
| MOD2 LEVEL | Sweep | Sweep | Sweep | Sweep | | | Pitch sweep | |
| MOD FX RATE | Sweep | Sweep | Sweep | Sweep | Sweep | Sweep | Pitch sweep | Spacing crunch |
| MOD FX DEPTH | Contour | Contour | Contour | Contour | Contour | Contour | Mod envelope | Body envelope |

| Pad | GIN |
|---|---|
| OSC1 LEVEL | GIN level |
| OSC1 PULSE WIDTH | Tone wave |
| OSC1 RETRIGGER | Tone attack |
| OSC1 FEEDBACK | Drive |
| OSC1 WAVE INDEX | Decay (tone and noise together) |
| OSC1 NOISE | Mix |
| OSC2 LEVEL | Mix |
| OSC2 TRANSPOSE | Noise freq |
| OSC2 TYPE | Noise filter |
| OSC2 PULSE WIDTH | Noise env |
| OSC2 RETRIGGER | Noise attack |
| OSC2 FEEDBACK | Noise reso |
| OSC2 WAVE INDEX | Noise decay |
| MOD1 LEVEL | EQ gain |
| MOD1 TRANSPOSE | EQ freq |
| MOD1 WAVE INDEX | Tone decay |
| MOD2 LEVEL | Mod amount |
| MOD2 TYPE | Mod mode |
| MOD2 WAVE INDEX | Mod rate |
| MOD FX RATE | Mod rate |
| MOD FX DEPTH | Mod amount |

### Gold knobs

Every drum synth row and the 303 share one layout, after the Cycles' knobs (changed in v1.11). It's set whenever the sound loads, however it was saved.

| Knob | Every drum engine |
|---|---|
| Attack / Release | **Drive / Decay** (the envelope's attack and release are still in its menu) |
| Mod rate / Mod depth | **The sweep**: how fast / how deep |
| CUSTOM 1 | Tune |
| CUSTOM 2 / CUSTOM 3 | **Two voicing settings** (never decimation / bitcrush on a drum synth row) |

| Engine | Mod rate / Mod depth | CUSTOM 2 / CUSTOM 3 |
|---|---|---|
| Kick / tom | Pitch decay / Pitch amount | FM amount / Mod pitch |
| Snare | Pitch decay / Pitch amount | Noise mix / Noise cutoff |
| Cymbal / hat | Transient speed / Transient level (it has no pitch sweep) | FM amount / FM 2 amount |
| DXIA | Blendex 2 / Blendex 3 (no pitch sweep) | Blendex 1 / Freq 1 |
| DIIA | Shape / Strike | Weight / Alloy |
| Cyc engines | Sweep / Contour (Pitch sweep / Mod envelope on Vtg Snr, Spacing crunch / Body envelope on clap eng) | Color / Shape (Inharm / Freq complex on Vtg Snr, Body char / Balance on clap eng) |
| GIN | Mod rate / Mod amount | Mix / Noise freq |

Every continuous drum synth setting is a Deluge parameter, so it can be parameter locked (hold a step and turn) and automated.

### Modulation and automation (new in v1.14)

- **Mod matrix:** every continuous setting on every engine can be modulated. Open the setting (its pad or the Drum synth menu) and press a mod source pad, as for any Deluge parameter: LFOs, envelopes, velocity, note, random, aftertouch and MPE all work. Each voice gets its own modulation, so velocity on Decay or random on Color changes every hit.
- **Depth:** the same on every setting. A cable at 50 with its source at full moves the setting 64 steps, from the middle to either end.
- **Automation view:** on a drum synth row the OSC1, OSC2, MOD1 and MOD2 columns follow the drum synth's shortcut pads, so each setting is on the pad you already use for it. Pads holding a choice (waves, modes, filter type, Punch) are blank. The mod FX pads stay mod FX rate and depth, since every sweep setting also has a pad in those columns.
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
- **Punch** (OSC1 FEEDBACK, on OSC1 RETRIGGER before v1.11) squares up and lifts the attack.
- They sound close to the originals, not identical: the same knobs and starting values, with the sound behind each knob measured from the originals and rebuilt. Cyc Kik's Contour, which barely did anything on the Cycles, sets the length of the pitch drop and the knock here. From v1.15 Contour stretches the pitch drop on Cyc Kik and Cyc Perc, and each engine's starting Contour sounds as before.

### GIN (new in v1.13)

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

### Snappy decay

**Snappy decay** (**SNAP**), in the sound menu of any drum synth row, makes the amp envelope's decay and release follow a steeper curve: tighter hits, and the same decay setting sounds about half as long. It starts off on new drum synth rows (from v1.12: each engine's own decay does the shaping) and is saved with the row.

### Good to know

- The full settings list and a pad-per-setting editor (GIN has its own) are in the sound menu under **Drum synth** (**DRUM**). **Load preset** (**PRST**) there has the seven kit sounds and each DXIA and DIIA variant.
- **SHIFT + press SELECT > CPU load** (**LOAD**) shows the audio engine's load, for checking how many drum synth voices you can run.
- Fixed in v1.8: loading a song no longer resets the LXR transient level and speed, or DXIA's Freq 2 and 3.
- Fixed in v1.15: CUSTOM 1 tunes rows loaded from preset kit files too (it was on portamento).
- Kits with drum synth rows won't play those rows on firmware without them.
- The full reference is in the source patch, at `website/src/content/docs/features/drum_synth.mdx`.

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
- Saved files also store the old saturation amount, so other firmware still plays them, with the original curve.
- Saturation sits after the filters and the amp envelope, as before, so the sound's volume and velocity change how hard it drives.
- The curves are antialiased, so high notes alias less than with the original, except Fold, which aliases when pushed hard on bright sounds, as digital folders do.

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
| **Decay** (**DCAY**) | Gold knob Mod rate/depth (top), SHIFT + MOD2 LEVEL or MOD FX RATE pad | The filter envelope's decay, 200 to 2000 ms |
| **Drive** (**DRIV**, new in v1.11) | Gold knob Attack/Release (top), SHIFT + OSC1 FEEDBACK pad | The drum synth engines' soft clipper. 0 is clean; low settings bite on accents first, and it gets much dirtier than it gets louder |
| **Amp decay** (**ADEC**, new in v1.11) | Gold knob Attack/Release (bottom), SHIFT + OSC1 WAVE INDEX pad | How long each note's level dies away while held: 60 ms, Open303's own 1230 ms at the centre (where older 303s sit), holding at the top |
| **Accent** (**ACC**) | Gold knob CUSTOM 2, SHIFT + OSC1 RETRIGGER pad | How hard accented notes hit |
| **Saw-square** (**WAVE**) | Gold knob CUSTOM 3, SHIFT + OSC1 PULSE WIDTH or OSC2 FEEDBACK pad | Fades from saw (0) to square (50) |
| **Slide time** (**SLID**) | Gold knob Portamento (bottom), SHIFT + MOD1 FEEDBACK pad | How long a slide takes to arrive |
| **Filter** (**FILT**) | SHIFT + MOD2 FEEDBACK pad | **303**, a model of the TB-303's filter, or **LP18**, Open303's plainer 18 dB lowpass |

They're all in the sound menu under **303** too. Every one except Filter is a Deluge parameter, so it can be parameter locked (hold a step and turn) and automated.

### Accent and slide

- **Accent:** any note with velocity 100 or more is accented. It opens the filter further, with a fixed short decay, and hits harder. Set a note's velocity as normal on the Deluge.
- **Slide:** hold a step and click the up/down knob (see the mono sequencer). Played live, notes slide when they overlap, as on Open303.

### Good to know

- The 303's own oscillator, filter and envelopes replace the Deluge's: the oscillator, filter, envelope and unison settings do nothing in 303 mode. **Saturation** (SHIFT + SATURATION pad) works as on any synth, and drives the 303 the way it drives a voice.
- Patch cables (LFOs and envelopes) don't reach the 303's controls yet. Gold knobs, menus, parameter locks and automation do.
- Transpose, Fine tune and the arpeggiator all work. It's mono, so it plays one note at a time.
- Songs and presets save the 303 setting. Firmware without it loads the sound as a normal subtractive synth.
- In automation view the 303's controls sit on the FM pads they're saved on, so OSC1 FEEDBACK there is Accent and MOD2 FEEDBACK is Drive, unlike the shortcut pads.

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
- Songs and presets saved before v1.9 that use the delay load with feedback set to their amount, so they sound the same. Automation recorded on the old amount now moves only the echo level.
- The tone starts flat, so it changes nothing until you turn it. When flat, the filter is switched off entirely.
- Feedback and tone save with the song and the preset. Other firmware ignores them: it uses the amount for both level and feedback, and no filter.

## 11. Affect all

A performance snapshot for LXR, Cycles and GIN kits: push every drum around at once, then drop back to where you started on the next bar.

### Using it

1. In the kit's clip, press **SHIFT + AFFECT ENTIRE**. The kit is snapshotted and **AFFECT ENTIRE** flashes (**ALL**). You start in **All voices**.
2. **All voices:** turn any gold knob, or press **SHIFT** + a shortcut pad and turn **SELECT**, and every drum synth row moves by the same amount, each from where it was. Turn Sweep and every drum's sweep goes up; turn CUSTOM 1 and the whole kit retunes, staying in tune with itself.
3. **Kit FX:** press **AFFECT ENTIRE** on its own to swap to the kit's FX (**FX**), as AFFECT ENTIRE normally does, and again to go back to **All voices**. Swap as often as you like: the snapshot holds both.
4. Press **SHIFT + AFFECT ENTIRE** again. **AFFECT ENTIRE** flashes twice as fast (**BACK**), and on the next bar every drum and the kit's FX go back to the snapshot, before that bar's first hits. When stopped, it goes back straight away (**DONE**).

### Good to know

- Only drum synth rows move, including ones added to the kit since it was made (a BXIA row on a Cycles kit, say). Each moves its own engine's control on that knob or pad. Sample rows, synth rows and the 303 are left alone.
- A drum pushed to the end of a setting keeps its place against the others when you turn back.
- Nothing you do in affect all is recorded as automation, so the snapshot always puts the kit back exactly. Holding notes and turning a knob still parameter locks that row, as normal.
- Choices (waves, modes, filter type), patch cable amounts and transpose stay on the one row.
- The snapshot is held in memory only. It isn't saved with the song, and loading another song drops it.
- On any other kit, **SHIFT + AFFECT ENTIRE** shows **CANT**.

## Design and credit

Everything here was designed by [thisisbribery](https://github.com/thisisbribery).

- **The swing styles** came out of a swing visualiser built to study and sketch shuffle timings ([stolperbeats_v2](https://thisisbribery.github.io/stolperbeats_v2/)). DEEP, SQEZ and FOLD are original designs. HOPP follows the well-known MPC and Linn swing ladder (around 54, 58, 62, 66 and 71%), placed on whole ticks the way a 96 PPQN drum machine would.
- **Autofill's five fills** were first designed and played as an experimental mod on my own Stolperbeats module, then ported here.
- **The Mono sequencer** is an original design for writing basslines on the Deluge.
- **Endless Record** reuses the Deluge's own linear recording, started from the RECORD button while playing.
- **Saturation** is an original design: five antialiased curves on a single drive control with no level compensation, so it behaves like an overdriven input stage.
- **The 303 synth's** voice is ported from [Open303](https://github.com/RobinSchmidt/Open303) by Robin Schmidt (MIT licence), in single precision so it runs on the Deluge. Its Deluge integration, controls and the mono sequencer's slide steps were designed for this build.
- **The sample start offset** is ported from the open source [Owlet Deluge firmware](https://github.com/owlet-labs/DelugeFirmware) (GPL-3.0). This build adds saving the offset with songs and presets, the 7-segment menus, automation view support and the pulse width pad shortcut, and leaves out Owlet's other sampler features.
- **Affect all** is an original design: a temporary snapshot of a kit that every drum moves through together, put back on the bar line.
- **Delay feedback and tone** are small changes to the Deluge's own delay: each echo is scaled twice, once for what you hear and once for what goes back into the delay, and passes through a one-pole DJ filter on its way out of the delay line.
- **The Cycles presets** are my own Model:Cycles kits, made on my own machine and converted for the Cyc engines.
- **The LXR presets** are sixteen kits by **Hrtl**, released free by Erica Synths for the LXR-02 ([Fresh kits and patterns for the LXR-02 from Hrtl!](https://www.ericasynths.lv/news/fresh-kits-and-patterns-lxr-02-hrtl/), [Hrtl on SoundCloud](https://soundcloud.com/hrtl)), converted for the drum synth. All credit for those sounds goes to Hrtl.
- **The drum synth's** layout, controls and Deluge integration were designed for this build. Its kick / tom, snare and cymbal / hat voices are a modified version of the drum voices in the open source LXR-02 firmware by Erica Synths (GPL-3.0). DXIA and DIIA are ported from an open source engine set written for the Elektron Model:Cycles. The Cyc engines are original code, modelled on how the Model:Cycles and Syntakt machines respond, measured knob by knob; no Elektron code or data is used.
- **GIN's** voice is ported from the MIT licensed synthesis core of [GIN by SquareWave Studio](https://github.com/squarewave-studio/op1-mods) and [libpo32 by Eric Lewis](https://github.com/ericlewis/libpo32), with their copyright and licence notices kept in the source. The sixteen GIN kits, the controls and the Deluge integration were made for this build; GIN's own factory kits are not used.
- **The ideas behind the swing, pattern and fill features were inspired by the Stolperbeats Eurorack module by [Making Sound Machines](https://makingsoundmachines.com/stolperbeats/),** which shuffles beats on tuplet grids and stores patterns in banks. None of its firmware, timing tables, factory timings (Trip, Shake, Push and Clave) or factory patterns are used or included here.

## Not affiliated or endorsed

This is an independent, unofficial project. It is not affiliated with, endorsed by or supported by **Making Sound Machines**, **Synthstrom Audible**, **Erica Synths**, **Hrtl**, **Elektron**, **Roland**, **SquareWave Studio**, **Teenage Engineering** or **Sonic Charge**. Stolperbeats is a product of Making Sound Machines, the Deluge is a product of Synthstrom Audible, the LXR-02 is a product of Erica Synths, the Model:Cycles and Syntakt are products of Elektron, the TB-303 is a product of Roland, and the OP-1 and PO-32 are products of Teenage Engineering. All trademarks belong to their owners. No rights to the Erica Synths, LXR or LXR-02 trademarks are granted.

Use it at your own risk, and please don't contact Making Sound Machines, Synthstrom Audible, Erica Synths, Elektron, Roland, SquareWave Studio or Teenage Engineering for help with this build.

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
