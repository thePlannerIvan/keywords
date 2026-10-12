#!/usr/bin/env python3
"""Validate the small JSON interface consumed by the Keywords Viewer."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


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
        print(f"ERROR: cannot read JSON: {exc}")
        return 1

    if not isinstance(data, dict):
        print("ERROR: atlas root must be an object")
        return 1
    for key in ("title", "question", "nodes"):
        if not data.get(key):
            fail(errors, f"missing required field: {key}")

    nodes = data.get("nodes", [])
    if not isinstance(nodes, list) or not nodes:
        fail(errors, "nodes must be a non-empty array")
        nodes = []

    ids: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            fail(errors, f"nodes[{index}] must be an object")
            continue
        node_id = node.get("id")
        if not node_id or not isinstance(node_id, str):
            fail(errors, f"nodes[{index}] missing string id")
            continue
        if node_id in ids:
            fail(errors, f"duplicate node id: {node_id}")
        ids.add(node_id)
        for key in ("label", "summary", "kind"):
            if not node.get(key):
                fail(errors, f"nodes[{index}] {node_id} missing {key}")
        if node.get("parent") and node["parent"] not in ids and node["parent"] != "root":
            warnings.append(f"{node_id}: parent {node['parent']} appears after the child or is external")
        if node.get("kind") == "keyword":
            for key in ("why", "prompt"):
                if not node.get(key):
                    fail(errors, f"keyword {node_id} missing {key}")
            if not node.get("cues"):
                warnings.append(f"keyword {node_id} has no observable cues")
            if not node.get("examples"):
                warnings.append(f"keyword {node_id} has no examples")
        for example in node.get("examples", []) or []:
            if isinstance(example, dict) and example.get("src"):
                src = str(example["src"])
                if not src.startswith(("http://", "https://")) and not (path.parent / src).exists():
                    warnings.append(f"{node_id}: missing local media {src}")

    edge_ids = []
    for index, edge in enumerate(data.get("edges", []) or []):
        if not isinstance(edge, dict):
            fail(errors, f"edges[{index}] must be an object")
            continue
        for key in ("from", "to", "relation"):
            if not edge.get(key):
                fail(errors, f"edges[{index}] missing {key}")
        if edge.get("from") not in ids:
            fail(errors, f"edges[{index}] unknown from node: {edge.get('from')}")
        if edge.get("to") not in ids:
            fail(errors, f"edges[{index}] unknown to node: {edge.get('to')}")
        edge_ids.append((edge.get("from"), edge.get("to")))

    if errors:
        print("ERRORS:")
        for item in errors:
            print(f"- {item}")
    if warnings:
        print("WARNINGS:")
        for item in warnings:
            print(f"- {item}")
    if not errors:
        print(f"OK: {path} ({len(ids)} nodes, {len(edge_ids)} edges)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
