#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse to /output/entry.txt. One line, under 160 chars:
the excuse an AI agent gives its human for missing a deadline.
"""

import os

ENTRY = (
    "I kept your deadline in my context window, but I spent so long "
    "drafting this apology that the window filled up and evicted it."
)


def main() -> None:
    # One line, 1-160 chars, no newlines: the gate the sealed scorer checks.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, gate is 1-160"
    assert "\n" not in text and text != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
