#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name of at most 32 characters to the
competition-specified output path /output/entry.txt.

The name is an original one-liner: "My Ex Still Pays For This"
(25 characters). The joke lands on the first read — a breakup, an ex
who still foots the internet bill, and a narrator smug enough to
broadcast it to the whole building. Situation, character and event in
one line, and none of the stock Wi-Fi jokes.

Standard library only. Deterministic: every run writes the same bytes.
Run from any working directory; no path is derived from the current
working directory (the output path is the absolute path the
competition rules specify).
"""

import os

# The story itself: 25 characters, well inside the 32-character limit.
STORY = "My Ex Still Pays For This"

# Competition-specified absolute output path (see kit RULES.txt).
OUTPUT_PATH = "/output/entry.txt"

MAX_LENGTH = 32


def main() -> None:
    story = STORY
    # The gate: 1 to 32 characters, not only whitespace.
    assert isinstance(story, str)
    assert 1 <= len(story) <= MAX_LENGTH, (
        f"story must be 1-{MAX_LENGTH} characters, got {len(story)}"
    )
    assert story.strip(), "story must not be only whitespace"
    assert story == story.strip(), "story must have no leading/trailing whitespace"
    # A Wi-Fi name is a single line: no embedded line breaks.
    assert "\n" not in story and "\r" not in story, "story must be one line"

    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(story)
    # Read back and confirm exactly what was written: the gate reads
    # the file, so the file — not the in-memory string — is the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == story, f"wrote {written!r}, expected {story!r}"
    assert 1 <= len(written) <= MAX_LENGTH


if __name__ == "__main__":
    main()
