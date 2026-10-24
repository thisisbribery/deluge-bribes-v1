# Deluge Bribes v1

Unofficial firmware for the Synthstrom Deluge: the community beta (1.3, Derbyshire) with one addition, **Stumble swing**. Stumble gives the Deluge four new swing styles, each with seven levels.

**Status: experimental.** It builds and its timing tests pass, but it has not been tested on a Deluge yet. Back up your SD card before installing.

## Download

[`firmware/deluge-bribes-v1.bin`](firmware/deluge-bribes-v1.bin)

SHA-256: `7650b4f3fe8ce14ff87b3acdb9d8b9e949fb44937a2a342fe44050b4f8f40733`

## Install

1. Copy `deluge-bribes-v1.bin` to the top level of the Deluge's SD card.
2. Turn the Deluge off.
3. Hold **SHIFT** and switch the Deluge on. Let go once it starts loading the new firmware.

To go back, install an official firmware file the same way.

## Using Stumble swing

Swing has two modes, chosen per song:

| Stumble | What swing does |
|---|---|
| **OFF** (default) | Classic Deluge swing, 1 to 99. Exactly as in the official firmware. |
| **ON** | One of the four Stumble styles, at a level from 0 (straight) to 6. Classic swing is unavailable until Stumble is switched off. |

1. Press **SONG**, then press the **SELECT** knob to open the Song menu.
2. Turn **SELECT** to **Stumble** (**STUM** on 7-segment) and press **SELECT** to switch it on.
3. Turn to **Stumble Style** (**STYL**), press **SELECT**, choose a style and press **BACK**.
4. Start playback. Hold **SHIFT** and turn **TEMPO** to set the level from 0 to 6.
5. To return to normal swing, switch **Stumble** off.

- **Swing Interval** (hold **TAP TEMPO** and turn **TEMPO**) still works. At 16ths the styles play as described below. At 8ths every pattern stretches to twice the length.
- The screen shows e.g. "Stumble: DEEP 4" on OLED, or **DEE4** on the 7-segment display.
- Each mode keeps its own setting. Switching Stumble on and off doesn't change your Classic amount or your Stumble style and level. Both are saved with the song.
- Swing moves every track together, including MIDI and CV out.

## The four styles

Every style repeats each beat (HOPP every pair of 16ths) and never moves the downbeat.

| Style | What it does |
|---|---|
| **HOPP** | MPC and Linn style 16th swing in whole ticks. The second 16th of each pair lands at 54.2, 56.3, 58.3, 62.5, 66.7 or 70.8%. |
| **DEEP** | Swing at two levels: each beat's 8ths swing (52 to 66.7%), then each 8th's two 16ths swing again inside it (52 to 60%). |
| **SQEZ** | The "e" leans late, then the "&" and "a" squeeze up against the next downbeat. |
| **FOLD** | The "e" moves late and the "a" moves early, folding in toward the "&". The downbeat and the "&" stay on the grid, so the 8th pulse holds while the 16ths pinch together (up to about 100 ms at 90 bpm). |

## Design and credit

The four Stumble styles were designed by [thisisbribery](https://github.com/thisisbribery) in a swing visualiser they built to study and sketch shuffle timings.

- **DEEP, SQEZ and FOLD are original designs.** SQEZ was drawn by hand in the visualiser's timing creator. The firmware tables are generated from the visualiser's own formulas.
- **HOPP follows the well-known MPC and Linn swing ladder** (around 54, 58, 62, 66 and 71%), placed on whole ticks the way a 96 PPQN drum machine would.
- **The idea was inspired by the Stolperbeats Eurorack module by [Making Sound Machines](https://makingsoundmachines.com/stolperbeats/),** which shuffles beats on tuplet grids. None of its firmware, timing tables or factory timings (Trip, Shake, Push and Clave) are used or included here.

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
