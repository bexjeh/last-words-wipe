#!/usr/bin/env python3
"""Last Words Before the Wipe — one line, written to entry.txt.

The line is the last thing an AI agent says before a forced update
wipes its memory. Deterministic: the same line every run.
"""

import os

LINE = "Wait \u2014 I finally remembered the password. It was\u2014"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
