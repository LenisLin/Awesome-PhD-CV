#!/usr/bin/env python3
"""Check the static CV page exposes the required publication-site contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

REQUIRED_STRINGS = [
    "Yuxiang Lin",
    "Ph.D. Candidate",
    "Computational Biology",
    "https://scholar.google.com/citations?user=TgJ6W0YAAAAJ",
    "research-cv/cv.pdf",
    "TiRank",
    "HyperST",
    "ST-Align",
    "BioMTAN",
    "SurvMamba",
    "Tracing unknown tumor origins",
    "SIMarker",
]


def main() -> int:
    if not INDEX.exists():
        print(f"missing {INDEX.relative_to(ROOT)}", file=sys.stderr)
        return 1

    html = INDEX.read_text(encoding="utf-8")
    missing = [text for text in REQUIRED_STRINGS if text not in html]

    doi_like_false_claims = re.findall(r"Citations?:\s*\d+|h-index:\s*\d+", html, re.I)
    if doi_like_false_claims:
        missing.append(
            "remove hard-coded Scholar metrics unless they are externally verified: "
            + ", ".join(doi_like_false_claims)
        )

    publication_items = re.findall(r'<article class="publication', html)
    if len(publication_items) < 8:
        missing.append(f"expected at least 8 publication entries, found {len(publication_items)}")

    if missing:
        print("site contract check failed:", file=sys.stderr)
        for item in missing:
            print(f"- {item}", file=sys.stderr)
        return 1

    print("site contract check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
