#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes a single sentence pitching the worst, most useless app
imaginable to /output/entry.txt.
"""

import os

ENTRY = (
    "Judge, meet SnoozeMail: an app that reads your unread emails aloud "
    "in a soothing voice while you sleep, so you wake up fully briefed "
    "and completely unrested, for five dollars a month, silence sold "
    "separately."
)

MAX_CHARS = 240


def main() -> None:
    # The gate requires 1-240 UTF-8 characters, not only whitespace,
    # and the brief requires exactly one sentence.
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-240 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
