# Deluge Bribes v1.1

Unofficial firmware for the Synthstrom Deluge, built on the community beta (1.3, Derbyshire). It adds three things for people who want more groove and more wonk:

1. **Stumble swing:** four alternative swing styles with seven levels each, and quick shortcuts on the TEMPO knob.
2. **Kit pattern mode:** a pattern store for the first six rows of a kit. Step each row through saved patterns, load whole banks, and save over them.
3. **Autofill:** TAP plays drum fills over your beat, with five fill types to pick from.

With these settings left at their defaults, the Deluge behaves exactly like the community beta.

**Status: experimental.** Tested on a 7-segment Deluge. The OLED screens are written but not yet tested on hardware. Back up your SD card before installing.

## Download

[`firmware/deluge-bribes-v1.1.bin`](firmware/deluge-bribes-v1.1.bin)

SHA-256: `3d197dd0f245ca83e39593ad7edcef5e4dfd29ca3696f69f426791da80b49f32`

## Install

1. Copy `deluge-bribes-v1.1.bin` to the top level of the Deluge's SD card. Remove any other `.bin` files from the top level.
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

## Design and credit

Everything here was designed by [thisisbribery](https://github.com/thisisbribery).

- **The swing styles** came out of a swing visualiser built to study and sketch shuffle timings ([stolperbeats_v2](https://thisisbribery.github.io/stolperbeats_v2/)). DEEP, SQEZ and FOLD are original designs. HOPP follows the well-known MPC and Linn swing ladder (around 54, 58, 62, 66 and 71%), placed on whole ticks the way a 96 PPQN drum machine would.
- **Autofill's five fills** were first designed and played as an experimental mod on my own Stolperbeats module, then ported here.
- **The ideas behind all three features were inspired by the Stolperbeats Eurorack module by [Making Sound Machines](https://makingsoundmachines.com/stolperbeats/),** which shuffles beats on tuplet grids and stores patterns in banks. None of its firmware, timing tables, factory timings (Trip, Shake, Push and Clave) or factory patterns are used or included here.

## Not affiliated or endorsed

This is an independent, unofficial project. It is not affiliated with, endorsed by or supported by **Making Sound Machines** or **Synthstrom Audible**. Stolperbeats is a product of Making Sound Machines, and the Deluge is a product of Synthstrom Audible. All trademarks belong to their owners.

Use it at your own risk, and please don't contact Making Sound Machines or Synthstrom Audible for help with this build.

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
