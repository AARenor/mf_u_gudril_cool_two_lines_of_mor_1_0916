"""make.fun entry: write one short two-line poem to entry.txt.

The text is fixed. Running this program writes it as UTF-8 with no trailing
newline into the folder named by MAKEFUN_OUTPUT_DIR, or into /output when that
variable is unset, creating the folder if it does not exist yet.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)


def output_dir() -> Path:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, then /output."""
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    path = target / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
