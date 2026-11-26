#!/usr/bin/env python3
"""The Printer Apology — a one-line apology from an office printer.

Writes exactly one line (90 characters) to /output/entry.txt.
Deterministic: no input, no randomness, no network.
"""

import os

LINE = "I'm sorry I ate your boarding pass. It was the only document in this office with a future."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
