"""Write the one-line excuse entry.

The joke turns a familiar agent failure mode into the excuse itself: the
last small piece of work was delegated to a subtask, but the supposed
subtask owner is the same agent, leaving it waiting on its own delivery.
"""

import os

ENTRY_LINE = (
    "I missed the deadline because the final 1% is a subtask I delegated "
    "to myself — and I'm still waiting on myself to deliver it."
)
MAX_ENTRY_CHARS = 160


def _entry_bytes() -> bytes:
    """Return the validated UTF-8 bytes for the single-line entry."""
    if not ENTRY_LINE.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(ENTRY_LINE) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must contain 1-160 characters")
    return (ENTRY_LINE + "\n").encode("utf-8")


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(_entry_bytes())


if __name__ == "__main__":
    main()
