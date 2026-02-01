# gcb-growth-engine
This repository is the **distribution + conversion layer** for the Goldstonian Concordance Bible (GCB). It is designed to help people **walk in the Word of God** in a noisy digital space while building sustainable support for hosting, translation, tooling, and outreach.

# GCB Growth Engine

This repository is the **distribution + conversion layer** for the Goldstonian Concordance Bible (GCB).
It is designed to help people **walk in the Word of God** in a noisy digital space while building
sustainable support for hosting, translation, tooling, and outreach.

This repo is intentionally separate from the theological canon repos so that:
- the canon repos stay clean, scholarly, and stable
- the growth engine can move fast (landing pages, lead magnets, weekly plans, social templates)
- links can be updated without touching core data

## What this repo does
- GitHub Pages site (docs/) with:
  - “Start here” onboarding
  - link hub (for bios, socials, Moltbook, Rumble, YouTube)
  - lead magnets (free downloads / reading plans)
  - offers (support tiers, church packs, training)
  - press kit + FAQ
- Automation:
  - publish GitHub Pages on every push
  - generate weekly reading plan pages from a template
  - optional release notes workflow

## What this repo does NOT do
- It does not host the Scripture text behind a paywall.
- It does not replace your canonical repositories.
- It does not ask people to “pay for the Bible.”

## Connect to the main org
Primary org: https://github.com/GoldstonianConcordanceBible

Suggested “source of truth” repos to link here:
- canonical index repo (your routing + metadata)
- each volume repo (book content / companion indexes)
- gcb-impact repo (mission + conduct + funding + agent skills)

## Setup in 5 minutes
1) Create repo: `gcb-growth-engine` under your org.
2) Copy/paste the files in this repository structure.
3) Go to GitHub repo Settings → Pages:
   - Source: **GitHub Actions**
4) Edit `docs/_config.yml`:
   - set `url` and `title`
5) Edit `docs/linkhub.md`:
   - add your real links (Amazon, Substack, Rumble, YouTube)

## The principle
We aim to be loud about the Gospel, quiet about ourselves, and excellent in craft.

> “The power is in the Word of God.” Tools simply help people reach it.

