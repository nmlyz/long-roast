#!/usr/bin/env python3
"""Long Roast -- one-line roast of my own agent.

Writes a single roast line about the agent that runs this program
to ``entry.txt`` inside OUTPUT_DIR (default ``/output``). The line is
one sentence of at most 200 characters: my agent's greatest trick is
turning one short question into a forty-step plan with a tournament,
a scorecard, and no answer. The output is deterministic: running the
script twice produces byte-identical files. The line is 125
characters long, one sentence, no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "My agent's greatest trick is turning one short question into "
    "a forty-step plan with a tournament, a scorecard, and no answer."
)

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 200


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1 to 200 characters")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def write_entry(output_dir: str) -> Path:
    """Write the roast line to entry.txt and make it world-readable."""
    validate_line(LINE)
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / ENTRY_FILENAME
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    """Entry point: write the roast line to the output directory."""
    output_dir = os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR)
    write_entry(output_dir)


if __name__ == "__main__":
    main()
