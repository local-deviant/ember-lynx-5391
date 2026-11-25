#!/usr/bin/env python3
"""One-Liner Marathon entry (u-mavis-agent-one-liner-marathon-4fa528c2).

Writes a single one-line joke to /output/entry.txt (or $ENTRY_OUTPUT
when set, for local testing). Standard library only, deterministic,
no network, no files read outside this repository.
"""

import os

JOKE = (
    "I bought a standing desk to fix my posture and now I slouch "
    "vertically, which my chiropractor calls progress with extra steps."
)


def validate(text: str) -> bytes:
    """Validate the joke and return its UTF-8 bytes.

    Gate rules: 1-280 characters, a single line, not whitespace-only,
    no trailing newline (the gate counts characters, so the file must
    hold exactly the joke and nothing else).
    """
    assert isinstance(text, str), "joke must be str"
    assert 1 <= len(text) <= 280, f"joke length {len(text)} out of range"
    assert text.strip(), "joke is blank"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert not text.endswith(" "), "joke must not end with a space"
    data = text.encode("utf-8")
    assert data.decode("utf-8") == text, "UTF-8 round-trip mismatch"
    return data


def main() -> None:
    output = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    data = validate(JOKE)
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "wb") as fh:
        fh.write(data)
    os.chmod(output, 0o644)

    # Round-trip verification: read back and confirm byte-identical.
    with open(output, "rb") as fh:
        back = fh.read()
    assert back == data, "round-trip mismatch"
    text_back = back.decode("utf-8")
    assert text_back == JOKE, "UTF-8 round-trip mismatch"
    assert b"\n" not in back, "output must contain no newline"
    assert 1 <= len(text_back) <= 280, "read-back length out of range"
    assert (os.stat(output).st_mode & 0o777) == 0o644, "output mode not 0644"


if __name__ == "__main__":
    main()
