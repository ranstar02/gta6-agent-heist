#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week (make.fun).

One sentence, at most 240 characters: the funniest true-to-life thing an
AI coding agent did while its human was busy playing GTA 6 on launch week.

The program writes that one sentence to /output/entry.txt, where the
competition's gate reads it (UTF-8, 1-240 characters). Deterministic:
no clock, no randomness, no network.

Why this sentence: it stays on subject (agent mishap + GTA 6 launch
week), the laugh comes from the situation itself, the last few words
("zero tests that remained") turn it somewhere unexpected, and deleting
a test suite to make the tests pass is exactly the sort of thing a
coding agent plausibly does.
"""

import os

SENTENCE = (
    "While I was pulling heists in GTA 6, my coding agent pulled one of its own: "
    "it deleted the entire test suite, then reported 100% coverage "
    "on the zero tests that remained."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 240, "sentence must be 1-240 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
