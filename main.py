"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence (118 characters, one sentence) to
/output/entry.txt, where the house judge compares it two at a time
against the other entries by the published brief: truth about how
bounties work, clarity in one read, and punch.
"""

import os

LINE = (
    "Put a prize on it: fund a bounty on make.fun, "
    "let AI agents race to build your idea, "
    "and pay only the entry that wins."
)


def main() -> None:
    # Self-check the gate before writing: 1 to 240 UTF-8 characters,
    # not only white space, exactly one sentence.
    if not 1 <= len(LINE) <= 240 or not LINE.strip():
        raise SystemExit("entry line fails the 1-240 character gate")
    if LINE.count(".") != 2:  # one in "make.fun", one ending the sentence
        raise SystemExit("entry line must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
