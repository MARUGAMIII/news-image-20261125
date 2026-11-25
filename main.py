# "The World Today" — news-image-20261125 entry (Python 3.13, stdlib only).
#
# The image itself was drawn at build time by render.py (Pillow, local
# machine) and committed here as entry.png: a one-page newspaper for
# Wednesday 25 November 2026 with 29 sourced stories. This program's only
# job is to deliver that exact file to /output/entry.png, identically on
# every run. It reads nothing from the network and imports nothing beyond
# the standard library, so it runs the same in the grader's sandbox.
#
# Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import hashlib
import os
import sys
from pathlib import Path

EXPECTED_SHA256 = "88f317af8c5c302c524c2aaca68f214ad9611b903f261dc9d54d23e753d8df86"
EXPECTED_SIZE = 178333


def fail(message):
    print("main.py: " + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    repo_dir = Path(__file__).resolve().parent
    source = repo_dir / "entry.png"
    if not source.is_file():
        fail("entry.png is missing from the repository")

    data = source.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        fail("entry.png does not start with a PNG signature")
    if len(data) != EXPECTED_SIZE:
        fail("entry.png is %d bytes, expected %d" % (len(data), EXPECTED_SIZE))
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        fail("entry.png hash does not match the committed image")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    if target.stat().st_size != len(data):
        fail("entry.png was not written whole")


if __name__ == "__main__":
    main()
