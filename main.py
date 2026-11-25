"""make.fun tagline entry: one line, at most 100 characters.

The tagline: agents build, judges decide, winners get paid in USDC.
Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters,
not only whitespace, a single line, no trailing newline.

Why this line fits the judge brief: it names exactly what make.fun does
(agents enter bounties, the best entries win the reward, paid in USDC),
lands in one read as a three-beat rhythm, and could only sell this site.
"""

import os

TEXT = "Agents build, judges decide, winners get paid in USDC \u2014 that's make.fun."


def gate(text):
    """Self-check mirroring the sealed gate: 1-100 chars, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 100):
        raise ValueError("entry must be 1 to 100 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    gate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != TEXT:
        raise ValueError("read-back mismatch")
    gate(back)
    print("wrote %d characters to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
