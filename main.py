#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one single-line software error message to /output/entry.txt.
The message names the real failure in plain words (a build that failed
on the exact line someone marked 'TODO: fix later' in 2019) and lands
the joke in the last three words.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space, a single line. This program checks that before writing
and writes the text exactly, with no trailing newline.
"""

import os

ENTRY = (
    "The build failed on line 42, which is the exact line someone "
    "marked 'TODO: fix later' in 2019. Later is now."
)


def main() -> None:
    # Gate self-check: one line, 1-200 chars, not only whitespace.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
