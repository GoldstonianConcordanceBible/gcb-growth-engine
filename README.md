# GCB Growth Engine

This repository is the **distribution + conversion layer** for the Goldstonian Concordance Bible (GCB).
It is designed to help people **walk in the Word of God with clarity** in a noisy digital space while
building sustainable support for hosting, translation, tooling, and outreach.

This repo is intentionally separate from the canon repos so that:
- the canon repos stay stable, scholarly, and citable
- the growth engine can iterate fast (landing pages, link hub, lead magnets, weekly plans, offers)
- links can change without touching the core project spine

## What this repo does
- GitHub Pages site (docs/) with:
  - Start Here onboarding
  - Link Hub (bio links)
  - Weekly reading plans
  - Free “lead magnets” (downloads / guides)
  - Offers (support tiers, church pack, training)
  - Moltbook templates
  - Metrics page (simple KPI discipline)
  - UTM tracking guidance (clean attribution)

- Automation:
  - Deploy GitHub Pages on push
  - Generate weekly plan pages (workflow_dispatch)
  - Create release notes pages on GitHub releases
  - Sync press kit automatically from repo metadata (optional)
  - Verify Link Hub links (basic hygiene)

## What this repo does NOT do
- No paywall for Scripture.
- No manipulative fundraising.
- No “engagement bait” theology.

## Connect to the main org
Primary org: https://github.com/GoldstonianConcordanceBible

Suggested “source of truth” repos to link here:
- canonical index repo (routing + metadata)
- each volume repo (book content / companion resources)
- gcb-impact repo (mission + funding + agent skills)

## Setup (10 minutes)
1) Create repo: `gcb-growth-engine` under your GitHub org.
2) Paste these files with the same paths.
3) Repo Settings → Pages:
   - Source: **GitHub Actions**
4) Edit `docs/_config.yml`:
   - set `url` + `baseurl`
5) Edit `docs/linkhub.md` with your real links.
6) Run: Actions → “Generate Weekly Reading Plan”

## The principle
Be loud about the Gospel, quiet about ourselves, excellent in craft.
