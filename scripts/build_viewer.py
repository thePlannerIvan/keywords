#!/usr/bin/env python3
"""Build a Keywords Viewer while preserving the review-core host seam."""
from __future__ import annotations

import argparse
import json
import sys
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

    # The host, not this builder, injects the bridge. Keep the contract visible
    # in generated HTML so DSH and the local review host can use the same page.
    bridge_marker = "{{REVIEW_BRIDGE}}"
    occurrences = template.count(bridge_marker)
    if occurrences != 1 or not any(line.strip() == bridge_marker for line in template.splitlines()):
        raise SystemExit(
            "template must contain one bare {{REVIEW_BRIDGE}} marker on its own line"
        )

    # DSH can inject the bridge when it owns the host page. Standalone output
    # must not render the unresolved marker as visible text.
    template = template.replace(bridge_marker, "")

    # Inline DSH design tokens.
    #
    # The sheet resolves from the byte-identical mirror shipped in this repo
    # (assets/dsh-tokens.css), so a standalone clone builds pages without
    # planners-review-core installed. The canonical copy stays the source of
    # truth: when one is reachable too, drift between the two is reported.
    token_placeholder = "/*__DSH_TOKENS__*/"
    if token_placeholder in template:
        mirror = Path(__file__).resolve().parents[1] / "assets" / "dsh-tokens.css"
        # Canonical copies, in resolution order.
        canonical_paths = [
            # 1. Monorepo source tree (02-skills-library/06-agent-productivity/keywords/scripts/ -> parents[3] is 02-skills-library)
            Path(__file__).resolve().parents[3] / "00-system" / "planners-review-core" / "assets" / "dsh-tokens.css",
            # 2. Installed runtime skill sibling (e.g. ~/.claude/skills/keywords/scripts/ -> parents[2] is ~/.claude/skills)
            Path(__file__).resolve().parents[2] / "planners-review-core" / "assets" / "dsh-tokens.css",
            # 3. Known agent runtime roots
            Path.home() / ".claude" / "skills" / "planners-review-core" / "assets" / "dsh-tokens.css",
            Path.home() / ".codex" / "skills" / "planners-review-core" / "assets" / "dsh-tokens.css",
            Path.home() / ".gemini" / "config" / "skills" / "planners-review-core" / "assets" / "dsh-tokens.css",
            # 4. Workspace / CWD fallback
            Path("02-skills-library/00-system/planners-review-core/assets/dsh-tokens.css").resolve(),
        ]
        canonical = next((p for p in canonical_paths if p.is_file()), None)
        if mirror.is_file():
            sheet_path = mirror
            if canonical is not None and canonical.read_bytes() != mirror.read_bytes():
                print(
                    "warning: assets/dsh-tokens.css has drifted from "
                    f"{canonical} — re-sync the mirror from planners-review-core",
                    file=sys.stderr,
                )
        elif canonical is not None:
            sheet_path = canonical
        else:
            raise SystemExit(
                "Error: dsh-tokens.css not found. Expected the bundled mirror at "
                f"{mirror}, or a copy under planners-review-core in the skills "
                "library or agent runtimes."
            )
        print(f"tokens: {sheet_path}")
        sheet_text = sheet_path.read_text(encoding="utf-8")
        template = template.replace(
            token_placeholder,
            f"/*===DSH_TOKENS_BEGIN===*/\n{sheet_text.rstrip()}\n/*===DSH_TOKENS_END===*/",
        )

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
