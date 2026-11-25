#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes exactly one Wi-Fi network name to /output/entry.txt:

    MyExTookTheDogAndTheRouter

26 characters, no trailing newline, so the gate counts exactly 26.
The name is a whole breakup story: the ex left, took the dog, and
took the router too — the very network you are reading.
"""

import os

ENTRY = "MyExTookTheDogAndTheRouter"


def entry_line():
    """Return the entry text: one Wi-Fi name, 26 characters."""
    return ENTRY


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry_line())
    # The grader collects outputs as another user: leave it readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
