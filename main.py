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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
