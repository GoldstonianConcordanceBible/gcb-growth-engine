#!/usr/bin/env python3
import argparse

TEMPLATE = """---
title: "{title}"
---

# {title}

## Theme
{theme}

## Day 1
Passage:
Mirror:
Water:
Fire:

## Day 2
Passage:
Mirror:
Water:
Fire:

## Day 3
Passage:
Mirror:
Water:
Fire:

## Day 4
Passage:
Mirror:
Water:
Fire:

## Day 5
Passage:
Mirror:
Water:
Fire:

## Day 6
Passage:
Mirror:
Water:
Fire:

## Day 7
Passage:
Mirror:
Water:
Fire:
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--week-slug", required=True, help="e.g., 2026-wk-01")
    ap.add_argument("--theme", required=True, help="Theme/title")
    args = ap.parse_args()

    title = f"Weekly Plan — {args.week_slug}"
    theme = args.theme.strip()

    out_path = f"docs/reading-plans/{args.week_slug}.md"
    content = TEMPLATE.format(title=title, theme=theme)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    idx_path = "docs/reading-plans/index.md"
    with open(idx_path, "a", encoding="utf-8") as f:
        f.write(f"\n- [{title}](./{args.week_slug}.html)\n")

    print(f"Wrote: {out_path}")
    print(f"Updated: {idx_path}")

if __name__ == "__main__":
    main()
