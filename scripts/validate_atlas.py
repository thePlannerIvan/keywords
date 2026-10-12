#!/usr/bin/env python3
"""Validate the atlas JSON consumed by the Keywords Viewer (relaxed & permissive)."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_atlas.py <atlas.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    errors: list[str] = []
    warnings: list[str] = []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: cannot parse JSON: {exc}")
        return 1

    if not isinstance(data, dict):
        print("ERROR: atlas root must be an object")
        return 1

    for key in ("title", "nodes"):
        if not data.get(key):
            errors.append(f"missing basic field: {key}")

    nodes = data.get("nodes", [])
    if not isinstance(nodes, list) or not nodes:
        errors.append("nodes must be a non-empty array")
        nodes = []

    ids: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"nodes[{index}] must be an object")
            continue
        node_id = node.get("id")
        if not node_id:
            errors.append(f"nodes[{index}] missing string id")
            continue
        if node_id in ids:
            errors.append(f"duplicate node id: {node_id}")
        ids.add(node_id)

        if not node.get("label"):
            warnings.append(f"{node_id} has no label (will fallback to id)")

    if errors:
        print("ERRORS:")
        for item in errors:
            print(f"- {item}")
        return 1

    if warnings:
        print("WARNINGS:")
        for item in warnings:
            print(f"- {item}")

    print(f"OK: {path} ({len(ids)} nodes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
