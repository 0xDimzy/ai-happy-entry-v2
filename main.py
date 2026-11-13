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

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"

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
    assert target.read_bytes() == SOURCE.read_bytes()


if __name__ == "__main__":
    main()
