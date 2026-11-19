#!/usr/bin/env python3
"""news-image-20261118 entry: copy the built image to /output/entry.png.

The image (entry.png, in this repository) sums up the world news of
Wednesday 18 November 2026. It was drawn by generate.py with PIL; this
entrypoint is standard library only, so it runs in the grader's
no-network container. Outside the grader, MAKEFUN_OUTPUT_DIR stands in
for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
