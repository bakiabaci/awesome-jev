# Tier A — Curated Production Shortlist

Verified against actual repository source code and pinned READMEs. These 20 repositories represent the highest-signal, production-ready tools across the Jev and System One ecosystem.

---

## 1. Core Integration & Official Tooling

| Repository | Stars | Description | Target Stack |
| :--- | ---: | :--- | :--- |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | 2,564 | **Official** TypeSafe skills and plugin repository. Teaches coding agents how to invoke Jev correctly, retrieve up-to-date cookbooks, and structure typed decisions. | Universal (`npx skills add typesafe-ai/skills --skill typesafe-ai`), Claude Code, OpenCode, Codex. |
| [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) | 490 | Exposes Jev as **11 standard Model Context Protocol (MCP) tools**: `jev_verify`, `jev_screen`, `jev_noul`, `jev_find`, `jev_rerank`, `jev_classify`, `jev_decide`, `jev_review`, and `jev_extract`. | Any MCP client: OpenCode, Claude Desktop, Cursor, Zed. |
| [UditAkhourii/quicksilver](https://github.com/UditAkhourii/quicksilver) | 98 | "Read widely, decide narrowly." Delegates heavy triage to Jev before LLM ingestion. Benchmarks claim 187 files filtered down to 4 files, reducing token usage from 26k to 2.4k. | Claude Code, OpenCode CLI. |

---

## 2. Context Economy & Token Optimization

Long agent sessions explode in cost and latency due to repetitive tool call outputs and verbose logs. These tools prune context deterministically without summarization artifacts.

| Repository | Stars | Description | Value Proposition |
| :--- | ---: | :--- | :--- |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 7,362 | Replaces lossy LLM compaction summaries with deterministic Jev decisions. **Never writes summaries**; surgically drops obsolete tool results while preserving verbatim history. | Zero loss of exact code context; Claude Code plugin. |
| [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) | 159 | Post-execution hook that prunes command output before returning to the model. Automatically whitelists errors, JSON, and git diffs. | Keeps raw tool output below token thresholds without polluting reasoning. |
| [hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache) | 75 | High-throughput local cache for Jev decisions based on `(model, schema, state)` tuples. Redacts PII before hashing. Deterministic replay for CI. | Eliminates repeated API billing for identical unit evaluations. |
| [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) | 101 | Splits file reads and grep outputs into ~25-line chunks, querying Jev for relevance probability. Unneeded blocks are stubbed with recall tokens. | Provides fallback to `system-one-adapter` (Haiku) if Jev API is unreachable. |

---

## 3. Code Intelligence & Runtime Verification

| Repository | Stars | Description | Value Proposition |
| :--- | ---: | :--- | :--- |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | 2185 | Semantic code search tool. Node 22+, `@dzhng/jevgrep`. Locates exact code blocks via intent queries rather than exact regex patterns. | Solves the "needle in a haystack" file search bottleneck in large repositories. |
| [reticlehq/reticle](https://github.com/reticlehq/reticle) | 1154 | "Agent says done — but is it actually working?" Drives real headless browser and Docker runtimes to verify agent outcomes, returning structured `pass / fail / unknown` with exact line traces. | Verifies runtime truth rather than theoretical code diffs. *(Note: FSL-46d6a0 source-available license)*. |
| [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) | 664 | Multi-stage git diff reviewer: Noul risk matrix → file profile classification → severity scoring → routing. | Automated code review with calibrated confidence. |
| [supercorp-ai/supercov](https://github.com/supercorp-ai/supercov) | 144 | Analyzes code diffs with Jev for security and coverage risks, runs project test suites, and converts uncovered branches into actionable prompts. | Pinpoints untested edge cases automatically. |
| [leepokai/jev-guard](https://github.com/leepokai/jev-guard) | 56 | Pre-execution safety gate. Evaluates tool calls against 3 typed questions (`risk_level`, `explicitly_requested`, `untrusted_input`). | Prevents dangerous execution loops in autonomous agents. |

---

## 4. High-Performance Vision & UI Automation

| Repository | Stars | Description | Value Proposition |
| :--- | ---: | :--- | :--- |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | **20,962** | The second largest project in the ecosystem. Sub-100ms visual UI classification and action triage for autonomous browser agents. | Blazing fast browser automation without waiting for heavy multimodal LLM decoding. |
| [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) | 741 | High-speed multimodal screen parsing and bounding box classification. | High-frequency screen analysis at minimal compute overhead. |

---

## 5. Dynamic Routing & Multi-Model Orchestration

| Repository | Stars | Description | Value Proposition |
| :--- | ---: | :--- | :--- |
| [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) | 528 | CLI router (`npm i -g jev-router`) that selects optimal models per turn while preserving native terminal interfaces and session state. | Seamless dynamic routing between Claude Code and Codex. |
| [nidhi-singh02/agent-router](https://github.com/nidhi-singh02/agent-router) | 100 | Quota-aware router that applies deterministic rules before escalating difficult queries to frontier LLMs. | Maximizes throughput on rate-limited subscription accounts. |

---

## 6. Evaluation, Benchmarks & Calibration

| Repository | Stars | Description | Value Proposition |
| :--- | ---: | :--- | :--- |
| [Jevals.com / jevals-data](https://github.com/Jevals/jevals-data) | 1 | Independent benchmark comparing hosted Jev and six frontier LLMs on identical Noul, Choice, and Score evaluations. | Empirical truth on decision accuracy across PubMedQA, Banking77, and HelpSteer2. |
| [chunxiaoxx/jev-trust](https://github.com/chunxiaoxx/nautilus-compass/tree/main/sdks/jev-trust) | 876 | Middleware logging every typed decision, calculating in-domain calibration (Brier score, ECE), and signing evidence with ed25519. | Cryptographically verifiable AI decision logs. |
| [abhixhek/jevcal](https://github.com/abhixhek/jevcal) | 10 | Fits and drift-checks confidence thresholds against labeled ground truth data. | Detects calibration drift in production classification pipelines. |
