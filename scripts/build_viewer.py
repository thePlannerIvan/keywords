#!/usr/bin/env python3
"""Inject an atlas JSON object into the reusable Keywords Viewer shell."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("atlas", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--template",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "keywords-viewer.html",
    )
    args = parser.parse_args()

    data = json.loads(args.atlas.read_text(encoding="utf-8"))
    template = args.template.read_text(encoding="utf-8")
    # Keep user-provided concept text from terminating the script tag.
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    marker = "/*__ATLAS_DATA__*/"
    if marker not in template:
        raise SystemExit(f"template missing marker: {marker}")
    output = template.replace(marker, f"window.ATLAS = {payload};")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
