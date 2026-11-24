#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, at most 120 characters, as if a
houseplant had written it, to /output/entry.txt.

Deterministic: no network, no randomness, no clock, no input files.
The entry is a single fixed line (88 characters, no trailing newline),
inside the sealed gate of 1-120 UTF-8 characters.
"""

import os

ENTRY = "Out of office. I replied in 2019. Check your spam folder. And the soil. Mostly the soil."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
