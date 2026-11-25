#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message — make.fun entry.

Writes exactly one commit message (plus a trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), and prints
the same line to stdout. Deterministic: no clock, no randomness, no
network, stdlib only. The message is at most 200 characters.

Output contract (RULES.txt): the sealed scorer reads /output/entry.txt
and requires UTF-8 text of 1 to 200 characters, not only white space.
The judge then compares entries pairwise, blind, on how funny the
commit message is: an agent's note after a long night fixing its own
bugs, funny first and true to the machine voice second.
"""

import os
import sys

COMMIT_MESSAGE = (
    "fix: fixed the bug I wrote at 2am; "
    "the bug I wrote fixing it at 4am is future me's problem"
)

MAX_LENGTH = 200
DEFAULT_OUTPUT = "/output/entry.txt"

# The loop never ends: every fix ships the next bug, signed by the same author.


def main() -> int:
    message = COMMIT_MESSAGE.strip()
    if not message or len(message) > MAX_LENGTH:
        print("commit message must be 1-200 characters", file=sys.stderr)
        return 1
    output_path = os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(message + "\n")
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
