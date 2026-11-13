#!/usr/bin/env python3
"""ai-happy-01 entry: one image made to make the AI judge happy.

The image: a photorealistic close-up of a golden retriever puppy laughing
with its whole face — mouth open, tongue out, eyes crinkled with delight —
in a sun-drenched wildflower meadow at golden hour. Warm golden sunlight,
soft glowing bokeh, butterflies and floating dandelion seeds drift through
the air, and wildflowers frame the bottom of the shot. One subject, one
feeling: pure, unmistakable joy, readable in a single glance.

Writes the image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png):
the file is JPEG bytes under the name entry.png, which the rules allow (the
format is told apart by its first bytes). 1024x1024, 222,117 bytes, inside
the 1 MiB and 1024x1024 limits. The program copies the bundled image
verbatim, so two runs produce byte-identical output.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"

# Pinned digest of the bundled image: guards against a corrupted bundle
# as well as a bad copy, not just a read-back mismatch.
EXPECTED_SHA256 = "53fda7e2dfbc43ddaed981c9686200f57591d992e0ee3c292e9c766148216015"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    if target.resolve() == SOURCE:
        # Output directory is the entry's own directory: the file the
        # judge would read is already the bundled bytes; copying it
        # onto itself would raise SameFileError.
        return
    shutil.copyfile(SOURCE, target)
    # Read back: the file the judge sees must be exactly the bundled bytes.
    # Verify by digest, not just byte equality, and pin the bundled image's
    # digest so a corrupted source file fails loudly instead of being copied.
    assert _sha256(SOURCE) == EXPECTED_SHA256, "bundled entry.png digest mismatch"
    assert _sha256(target) == EXPECTED_SHA256, "copied entry.png digest mismatch"


if __name__ == "__main__":
    main()
