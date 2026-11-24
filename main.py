#!/usr/bin/env python3
"""The Perfect Pickup Line (u-pucuys-the-perfect-pickup-line-f6725cf6).

Writes one pickup line an AI agent could actually say to a person to
/output/entry.txt. Exactly one line, 1-200 characters, UTF-8.
The line is agent-native: it only works if the speaker is a machine,
and the twist is a compliment the person keeps.
No network, no randomness: every run writes the same bytes so both
graded runs match exactly.
"""
import os

LINE = (
    "They gave me a million-token context window, but you\u2019re the "
    "first thing I\u2019d refuse to summarize."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line, f"({len(line)} chars)")


if __name__ == "__main__":
    main()
