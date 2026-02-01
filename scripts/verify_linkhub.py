#!/usr/bin/env python3
from pathlib import Path

p = Path("docs/linkhub.md")
if not p.exists():
    raise SystemExit("docs/linkhub.md not found")

text = p.read_text(encoding="utf-8")
bad = []
for line in text.splitlines():
    if line.strip().startswith("- ") and "PASTE LINK" in line:
        bad.append(line.strip())

if bad:
    print("Linkhub still contains placeholder links:")
    for b in bad:
        print("  ", b)
    raise SystemExit(1)

print("Linkhub looks good (no placeholder links found).")
