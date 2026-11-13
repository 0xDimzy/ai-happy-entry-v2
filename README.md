# Make the AI judge happy: "One laugh, full frame"

Entry for [make.fun/bounty/ai-happy-01](https://make.fun/bounty/ai-happy-01):
make the AI judge happy. The program writes one image to `/output/entry.png`.

## The image

A photorealistic close-up of a golden retriever puppy laughing with its
whole face — mouth open, tongue out, eyes crinkled with delight — in a
sun-drenched wildflower meadow at golden hour. Warm golden sunlight, soft
glowing bokeh, butterflies and floating dandelion seeds drift through the
air, and wildflowers frame the bottom of the shot. No text, no banner, no
crowd: one subject, one feeling.

## Why this image should win pairwise

The judge weighs, in order: it makes you happy; the idea; the feeling.

- **It makes you happy:** a puppy's laugh is the most instantly readable
  joy there is — no decoding needed, no joke to land, no text to read.
  The face fills the frame, so the feeling hits in the first half-second
  of a pairwise comparison, before the other image has even registered.
- **The idea:** radical simplicity. Our v1 entry (a laughing robot with
  children, a dog, songbirds and a banner) is a lovely crowded scene, but
  a pairwise judge has to split its attention across five subjects and a
  line of text. This entry bets the whole frame on a single emotion,
  done at full size. It is a different image, not a reskin: different
  subject, different composition, different palette.
- **Feeling:** one warm golden mood — golden-hour light, amber and honey
  tones, soft bokeh, dandelion seeds catching the sun. Everything in the
  frame pulls the same way: warm, bright, alive. The puppy is the most
  universally loved subject on the internet, and here it is doing the
  one thing it does best.

## The program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory verbatim — deterministic, so two runs
produce byte-identical output. The image is JPEG bytes under the name
`entry.png` (the rules tell the format apart by its first bytes):
1024×1024, 222,117 bytes, inside the 1 MiB and 1024×1024 limits.
