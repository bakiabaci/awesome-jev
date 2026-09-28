# Jev Ecosystem Index — Methodology, Coverage and Known Limits

Generated: 2026-09-28 09:05 UTC  
Source of truth: `data/index.json` (machine-readable), `data/04-scored.jsonl` (full detail including README text).

## How This Was Built

1. **Discovery** — GitHub Search API queried across 11 signals (`topic:jev`, `topic:typesafe`,
   `topic:system-one`, `topic:laya`, `topic:typed-decisions`, `topic:decision-model`,
   `jev in:name`, `typesafe-ai in:name,description`, `"TypeSafe" in:description`,
   `"system one" in:description jev`, `jevlang OR jev.ai in:name,description`).
   The GitHub Search API caps single queries at 1,000 results; every over-cap query was
   recursively split across year → month → day windows until no window exceeded 900 hits.
   **11,901 unique repositories** were discovered and de-duplicated.
2. **Pre-filter** — A Jev-specific vocabulary score (not a generic "type safe" substring match)
   combined with a traction rule. Anything carrying a `jev`/`typesafe` topic, a Jev-shaped name,
   or >= 20 stars was retained. The remainder was routed to `data/99-rejected.jsonl` **with explicit reasons recorded**.
3. **Enrichment** — GraphQL batch queries (20 repositories per query): stars, forks, open issues/PRs,
   license, topics, language breakdown, disk usage, default branch, last commit timestamp,
   latest release, and the first 12,000 characters of `README.md`.
   **4,873 repositories enriched.**
4. **Classification** — Component type, harness compatibility, install method, cost model,
   and functional domain were extracted using weighted regex heuristics over description, topics, and README.
   **No model calls were made in this pipeline.**
5. **Scoring** — Decision score weights community traction (0-35), Jev evidence (0-25),
   agent stack fit (0-20), activity (0-12), and documentation evidence quality (0-8),
   penalizing archived and unmaintained zero-star repos. Tier A additionally requires
   >= 30 stars or >= 10 forks, ensuring zero-star repos never reach Tier A on keyword frequency alone.

## Why Topic-Only Indexing Fails

`browser-use/jev-ultrafast` is the **2nd largest Jev project by stars (20,962)** and carries
**zero GitHub topics** — it is completely invisible to `topic:jev`. Its description is simply `i. am. speed.`.
It can only be reached via name-shape matching. This single fact demonstrates why classical topic-only
awesome lists miss critical projects, and why an 11-signal union pipeline is essential.

## Ecosystem Overview

- **4,873** enriched repositories, **302,054** total stars.
- **4,553** of them were created in September 2026 alone. The ecosystem emerged within days:
  1,634 `topic:jev` repos appeared between 2026-09-15 and 2026-09-24.
- Tiers: Tier A=122, Tier B=3274, Tier C=1477.
- Median stars per repo: 1.

| Functional Domain | Repositories |
| :--- | ---: |
| Open Decision Models & Inference (System One / Laya / Open Weights) | 1,338 |
| Routing, Model Dispatch & Agent Registries | 926 |
| Document, Data & SQL Triage | 472 |
| Skills, Plugins & General Tooling | 444 |
| Unclassified | 409 |
| Games, Robotics & Embodied AI | 357 |
| Browser, Desktop & Computer Use | 321 |
| Memory, Compaction & Context Window Economy | 234 |
| Code Review, Linting & Security Gates | 140 |
| Trading, Finance & Market Microstructure | 107 |
| Search, Retrieval & SEO | 86 |
| Agent Frameworks & Orchestration | 22 |
| Ecosystem Indexes & Curated Lists | 17 |

| Harness Mentioned in README | Repositories |
| :--- | ---: |


## Known Limits & Transparent Disclosures

1. **Truncation in Search Windows**: Three `jev in:name` day-pair windows (2026-09-18..23) reached the 1,000-result API cap where recursion stopped at depth 5. These windows are covered independently by `topic:jev` buckets; no known major Jev project is missing, but raw pool candidate counts are conservative by ~1,500 hits.
2. **Topic Cap**: `field:topic` is capped at 40 topics per repo in the GraphQL fragment.
3. **README Truncation**: README text is truncated at 12,000 characters (median README length is ~7,100 characters).
4. **Regex Heuristics**: `component`, `domain`, and `cost_model` are deterministic regex classifications, not manually certified facts. They serve as navigation aids.
5. **Awesome-List Repositories**: Awesome-list repos are indexed as projects, but their linked entries were not recursively scraped to prevent circular inclusion.
6. **Archived Repositories**: Explicitly archived repositories are excluded from enrichment.

## File Manifest

| Path | Description |
| :--- | :--- |
| `data/index.json` | Complete machine-readable index (enriched + long tail) |
| `data/statistics.json` | Statistical distributions and aggregations |
| `data/consensus_research.json` | 30 peer-reviewed papers fetched via Consensus API |
| `data/04-scored.jsonl` | Enriched records with extracted README text and scores |
| `data/00-raw-discovery.jsonl` | Every discovered repo with query provenance |
| `data/99-rejected.jsonl` | Rejected candidates with recorded justification |
| `data/02-longtail.jsonl` | Metadata-only tail records |
| `catalog/01-tier-a.md` | Curated shortlist for production agent stacks |
| `catalog/02-harness-integration.md` | Recipes for Claude Code, OpenCode, Codex, Cursor & MCP |
| `catalog/03-open-models.md` | Self-hosted, local weights, and wire-compatible servers |
| `catalog/04-scientific-consensus.md` | Academic foundation & empirical evidence |
| `scripts/harvest.py` | Resumable discovery and GraphQL enrichment |
| `scripts/prefilter.py` | Evidence scoring and tier routing |
| `scripts/classify.py` | Deterministic classification and scoring |
| `scripts/report.py` | Catalog and index generator |
