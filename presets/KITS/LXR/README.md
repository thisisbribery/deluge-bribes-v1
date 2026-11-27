# LXR presets

Sixteen kits by **Hrtl**, from the free LXR-02 pack Erica Synths released in 2022: [Fresh kits and patterns for the LXR-02 from Hrtl!](https://www.ericasynths.lv/news/fresh-kits-and-patterns-lxr-02-hrtl/) ([Hrtl on SoundCloud](https://soundcloud.com/hrtl)). Converted from the pack's .SND kit files to Deluge kits on the drum synth's LXR voices with [`tools/lxr_to_deluge.py`](../../../tools/lxr_to_deluge.py). They are close to the originals, not identical: the drum synth's LXR voices are a port of the LXR-02's, but the amp envelopes, filters and drive are converted, and LFOs, velocity modulation and the LXR-02's FX aren't carried over.

Kits 16 to 25 (TEKKNO, BOOM808, ELECTRO, LOFIDUST, INDUSTRL, MINIMAL, NTRPBT1, CONCRETO, FERRUGEM, MADRUGA) are **EntropiaLabs**' own kits from [ELABS RLX](https://github.com/mcamaradev/ELABS-RLX-02-LXR02-CLONE-VST) (GPL-3.0), converted the same way. Kits 26 to 41 (DEEP808, PUNCH909, TIGHT606, CR78SOFT, FOUNDRY, CLICKS, BRONX, DUBPLATE, TAPEDUST, SUBBOOM, TWOSTEP, HEXPADS, BELLTREE, AMENISH, ACIDHAUS, BITROT) are new Bribes kits, built from the LXR-02's init kit. Kits that use snare or clap repeat, decimation or LFOs (ELECTRO, LOFIDUST, FERRUGEM, MADRUGA) lose those, as the drum synth has no equivalent. Details in [`CREDITS.txt`](CREDITS.txt).

From v1.40 every Bribeluge kit has eight rows, so each kit here has an eighth, **PERC**: the kit's own high tom voice a fifth up with a shorter decay, added with [`tools/add_perc_rows.py`](../../../tools/add_perc_rows.py). It is not part of the original kit.

Copy this folder to `KITS/LXR` on the Deluge's SD card. On an LXR kit, **SHIFT + KIT** browses them.

Credit for the sounds goes to Hrtl and EntropiaLabs. Not affiliated with or endorsed by Hrtl, EntropiaLabs or Erica Synths.
