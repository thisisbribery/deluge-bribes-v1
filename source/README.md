# Source code

The complete source of Deluge Bribes (BRIBELUGE), under the GNU General Public License v3.

- **`DelugeFirmware/`**: the full firmware source, a git submodule pinned to the exact commit the current bin was built from (tag `bribes-v1.49`). On GitHub, click it to browse that commit. To fetch it locally: `git clone --recursive https://github.com/thisisbribery/deluge-bribes-v1.git`, or `git submodule update --init` in an existing clone.
- **`stumble-swing.patch`**: the same changes as one patch against community firmware tag `v1.3.0`.

Every change is a separate commit on branch [`bribes`](https://github.com/thisisbribery/DelugeFirmware/tree/bribes) of the fork. A full source `.tar.gz` is attached to each [release](https://github.com/thisisbribery/deluge-bribes-v1/releases).

To build: `cd DelugeFirmware && ./dbt configure && ./dbt build release`. The firmware is written to `build/Release/deluge.bin`.
