#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "wm-mechanism-explorer" / "SKILL.md"
REQUIRED_REFS = [
    "references/question-ladder.md",
    "references/mechanism-map-template.md",
    "references/counterfactual-protocol.md",
    "references/output-contract.md",
    "tests/evals.md",
]


def main() -> int:
    text = SKILL.read_text(encoding="utf-8")
    problems: list[str] = []

    if not text.startswith("---\n"):
        problems.append("SKILL.md must start with YAML front matter")

    front = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    if not re.search(r"(?m)^name:\s*wm-mechanism-explorer\s*$", front):
        problems.append("front matter name must be wm-mechanism-explorer")
    if not re.search(r"(?m)^description:\s*.+$", front):
        problems.append("front matter must contain a description")

    for rel in REQUIRED_REFS:
        path = SKILL.parent / rel
        if not path.exists():
            problems.append(f"missing skill file: {path.relative_to(ROOT)}")

    if "F — Fact" not in text or "R — Fictional Rule" not in text:
        problems.append("skill must preserve F/I/H/R evidence separation")

    if "Stop before production" not in text:
        problems.append("skill must contain the pre-production stop gate")

    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1

    print("PASS skills/wm-mechanism-explorer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
