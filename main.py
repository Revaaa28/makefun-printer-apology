#!/usr/bin/env python3
"""The Printer Apology — a one-line apology from an office printer.

Writes exactly one line (90 characters) to /output/entry.txt.
Deterministic: no input, no randomness, no network.
"""

import os

LINE = "I'm sorry I ate your boarding pass. It was the only document in this office with a future."


def main() -> None:
    # Gate: entry must be a single non-blank line, 1-120 chars (kit rules).
    assert LINE.strip(), "entry must not be blank"
    assert 1 <= len(LINE) <= 120, f"entry must be 1-120 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify what was actually written matches the gated line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry does not match gated line"
    assert 1 <= len(written) <= 120, f"written entry must be 1-120 chars, got {len(written)}"


if __name__ == "__main__":
    main()
