#!/usr/bin/env python3
import re
from pathlib import Path

LINKHUB = Path("docs/linkhub.md")
PRESS = Path("docs/press-kit.md")

def extract_links(md: str):
    # basic: capture "- Label: URL"
    links = []
    for line in md.splitlines():
        line = line.strip()
        if line.startswith("- "):
            parts = line[2:].split(":", 1)
            if len(parts) == 2:
                label = parts[0].strip()
                url = parts[1].strip()
                if url and "PASTE" not in url:
                    links.append((label, url))
    return links

def main():
    if not LINKHUB.exists():
        raise SystemExit("docs/linkhub.md not found")

    linkhub = LINKHUB.read_text(encoding="utf-8")
    links = extract_links(linkhub)

    body = [
        "---",
        'title: "Press Kit"',
        "---",
        "",
        "# Press Kit",
        "",
        "## One-liner",
        "Goldstonian Concordance Bible helps believers walk in the Word with clarity through structured study resources and AI-ready indexing.",
        "",
        "## Short description",
        "This ecosystem combines canonical indexing, companion study resources, and public-facing tools to help people build consistent Scripture habits in a noisy digital age.",
        "",
        "## Links",
    ]

    if links:
        for label, url in links[:25]:
            body.append(f"- **{label}**: {url}")
    else:
        body.append("- (Add links in linkhub.md)")

    body += [
        "",
        "## Contact",
        "- Media contact: (add email or contact form link)",
        "",
        "## Brand assets",
        "See: `docs/assets/brand/README.md`",
        "",
    ]

    PRESS.write_text("\n".join(body), encoding="utf-8")
    print("Synced docs/press-kit.md from docs/linkhub.md")

if __name__ == "__main__":
    main()
