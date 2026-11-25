"""Everyday Things, Two Lines — round 3 entrypoint.

Writes exactly two lines to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when the harness sets it). Deterministic, no network, no randomness.

Design — three candidates were weighed before this file was written:

  A. Toaster as a little sunbed tanning bread brown on both sides.
     Concrete, but a sunbed is not something every 10-year-old has
     seen or stood in, so the picture lands weakly.
  B. Traffic jam as a river of cars frozen solid.
     Strong picture, but "frozen traffic" is a familiar phrase, so
     the surprise is smaller, and the second line has to work hard
     to say anything beyond "cars cannot move".
  C. A queue as a human caterpillar.  <-- chosen
     Most on-theme for a 10-year-old: a caterpillar is something a
     child can picture holding and watching, the shuffling body
     maps the way a whole line creeps forward one tiny step at a
     time, nobody jumps ahead, and the honest second line has a
     sharp, specific limit ready — the feelings of the people
     waiting, which a real caterpillar never has.

Line 1 is a single vivid sentence with one metaphor only, no list
of comparisons and no second metaphor crowding it. Line 2 is a
single sentence naming what the caterpillar maps (moving together
in one line, in order) and what it leaves out (boredom, tiredness,
grumpiness while waiting), instead of praising the analogy.
"""

import os

# The entry text: exactly two lines, one sentence each.
LINE_1 = (
    "A queue is a human caterpillar, each person standing right behind "
    "the one in front as the whole long body shuffles forward one tiny "
    "step at a time."
)

LINE_2 = (
    "The caterpillar shows how everyone moves together in one line and "
    "nobody can jump ahead, but it leaves out that the people in it get "
    "bored, tired, and grumpy while waiting, feelings a real caterpillar "
    "never has."
)

ENTRY_TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def output_path() -> str:
    """Resolve the output file without ever touching a relative path.

    The grader sandbox may run with a read-only working directory, so
    this program writes nowhere except the harness output directory:
    $MAKEFUN_OUTPUT_DIR when set, otherwise /output. No ./entry.txt,
    no other file, no fallback that could crash the run.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def validate(text: str) -> None:
    """Gate-check the entry the same way the sealed scorer does."""
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    for line in lines:
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError(f"each line must be exactly one sentence: {line!r}")


def main() -> None:
    validate(ENTRY_TEXT)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
