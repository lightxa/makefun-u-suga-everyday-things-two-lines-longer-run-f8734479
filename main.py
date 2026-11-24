#!/usr/bin/env python3
"""Everyday Things, Two Lines: a shadow explained to a 10-year-old.

Writes one two-line text to /output/entry.txt.

Line 1 explains a shadow in a single vivid sentence built on one
concrete, surprising analogy: a dark twin who copies your every move
but can never pick anything up. Line 2 says in one sentence why that
analogy works: what it maps (the shadow follows your shape and your
steps) and what it leaves out (the twin has no body of its own and
vanishes the moment the light goes away).

Pure standard library, deterministic, no network at runtime.
"""

ENTRY = (
    "A shadow is like a dark twin who copies your every move "
    "but can never pick anything up.\n"
    "It maps how the shadow keeps your shape and follows your steps, "
    "but it leaves out that the twin has no body of its own "
    "and vanishes the moment the light goes away.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    for line in lines:
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError(f"each line must be exactly one sentence: {line!r}")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
