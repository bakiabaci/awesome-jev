# Contributing to Awesome Jev

Thank you for helping maintain and expand the definitive index of **Jev, Laya, and System One typed decision models** for AI agents.

---

## 🎯 Inclusion Criteria

To maintain signal quality across the ecosystem, all submissions are evaluated against four criteria:

1. **Concrete Typed Decision Loop**: The project must implement or integrate with typed decision primitives (`Choice`, `Noul`, `Score`), sub-100ms routing, or wire compatibility with `/v1/systemone`. Generic LLM wrappers without decision routing do not qualify.
2. **Runnable & Documented**: Projects must feature clear documentation, installation instructions, and verifiable, reproducible code or weights.
3. **Open Source**: The project must use an OSI-approved open source license (or open model weights agreement like Apache-2.0, MIT, Llama, Gemma).
4. **Zero Hype / Objective Phrasing**: Descriptions must be factual and technically precise. Avoid marketing adjectives ("revolutionary", "blazing-fast", "game-changing"). Quantify latency or architectural role where possible.

---

## 🏗️ 5-Stage Lifecycle Classification

When proposing a repository, classify it into the most accurate stage:

| Stage / Category | Purpose & Focus | Typical Primitives |
| :--- | :--- | :--- |
| **Stage 1: Ingress & Fast Routing** | First 50ms pre-flight triage, safety gates, intent compilation | `Choice`, binary predicates |
| **Stage 2: Context & Memory Economy** | Surgical context compaction, caching, file filtering without lossy summarization | `Noul`, relevance scoring |
| **Stage 3: Policy & Tool Gating** | Enforcing runtime guardrails before executing dangerous tools | `Noul`, MCP tools, risk gating |
| **Stage 4: Runtime QA & Verification** | Headless browser execution, code coverage analysis, compiler warning triage | `Score`, test generation |
| **Stage 5: High-Speed Vision Loops** | Sub-100ms UI classification, bounding box triage, screen parsing | Vision embeddings, `Choice` |
| **Open Weights & Local Runtimes** | Non-autoregressive models, Apple MLX, GGUF runtimes, `/v1/systemone` daemons | Direct logit inference |
| **SDKs & Frameworks** | Language bindings (Python, TS, Go, Rust), agent framework adapters | Standard client libraries |

---

## 📝 Entry Format Standard

### In `README.md` (Stage Highlights)
```markdown
* [owner/repo](https://github.com/owner/repo) (★stars) - Short, objective description of what it does and which problem it solves.
```

*Note: You do not need to worry about keeping star numbers updated manually. Our automated GitHub Action bot updates all repository star counts weekly via the GitHub GraphQL API.*

---

## 🚀 How to Submit

### Option 1: GitHub Issue Form (Recommended for quick suggestions)
If you just want to suggest a repository without editing files yourself:
1. Go to **[Issues → New Issue](https://github.com/bakiabaci/awesome-jev/issues/new/choose)**.
2. Select **Suggest a Repository**.
3. Fill in the repository URL, lifecycle stage, and short description.

### Option 2: Pull Request (Direct Contribution)
1. Fork the repository.
2. Add your project under the appropriate section in `README.md` or `catalog/`.
3. Ensure all text is 100% English.
4. Submit a Pull Request. GitHub will automatically populate our standard PR checklist.

---

## 🔄 Automated Metrics & Maintenance

* Repository star counts and archived statuses are synchronized on schedule via `.github/workflows/update-stars.yml`.
* Dead links and 404s are flagged automatically.
* To run the synchronizer locally:
  ```bash
  python .github/scripts/sync_stars.py
  ```
