<div align="center">

# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

### The Definitive Architecture Guide, Benchmarks, and Ecosystem Radar for TypeSafe Jev, Laya, and System One Typed Decision Models.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Sync Metrics](https://github.com/bakiabaci/awesome-jev/actions/workflows/update-stars.yml/badge.svg)](https://github.com/bakiabaci/awesome-jev/actions/workflows/update-stars.yml)
[![Academic Research](https://img.shields.io/badge/Research-Peer--Reviewed%20Evidence-blue.svg)](#scientific-foundations--research)
[![Indexed Repositories](https://img.shields.io/badge/Cataloged%20Repositories-7%2C414-blueviolet.svg)](#explore-the-7414-repository-catalogs)

<br/>

</div>

**System One models** represent a fundamental architectural shift in AI engineering: moving away from slow, expensive, autoregressive text generation for routine classifications and routing, and replacing it with ultra-low latency (30–150ms), strictly schema-constrained decisions with calibrated confidence probabilities.

---

## Contents

- [The 10-Second Mental Model](#the-10-second-mental-model)
- [The 4-Year Paradigm Evolution](#the-4-year-paradigm-evolution)
- [The Great Comparison (Why Not Instructor or Outlines?)](#the-great-comparison)
- [Empirical Performance Benchmarks](#empirical-performance-benchmarks)
- [Dual-Process Architecture](#dual-process-architecture)
- [The 3 Typed Primitives](#the-3-typed-primitives)
- [The 5-Stage Agent Lifecycle (Curated Showcase)](#the-5-stage-agent-lifecycle)
  - [Stage 1: Ingress, Security & Intent Routing](#stage-1-ingress-security--intent-routing)
  - [Stage 2: Context, RAG & Memory Economy](#stage-2-context-rag--memory-economy)
  - [Stage 3: Agent Policy & Tool Gating](#stage-3-agent-policy--tool-gating)
  - [Stage 4: Runtime Verification & Code Intelligence](#stage-4-runtime-verification--code-intelligence)
  - [Stage 5: High-Speed Vision & Multimodal Loops](#stage-5-high-speed-vision--multimodal-loops)
- [Open-Weight Models & Local Runtimes](#open-weight-models--local-runtimes)
- [Scientific Foundations & Research](#scientific-foundations--research)
- [SDKs by Language & Frameworks](#sdks-by-language--frameworks)
- [Production Blueprints](#production-blueprints)
- [Harness Integration Quickstart](#harness-integration-quickstart)
- [Explore the 7,414 Repository Catalogs](#explore-the-7414-repository-catalogs)
- [Official Resources & Community](#official-resources--community)
- [Contributing](#contributing)

---

## The 10-Second Mental Model

> **Stop using a bazooka to swat a fly.**

Most AI agents burn compute by prompting a frontier Large Language Model (LLM) to make binary or categorical choices:
* *"Is this customer support ticket about billing?"*
* *"Should the agent execute the `delete_database` tool?"*
* *"Is this retrieved document relevant to the user's question?"*

Running these through **System 2** (Claude 3.7, GPT-4o, Gemini 2.5 Pro) costs \$0.03 per call, takes **3 to 5 seconds**, burns thousands of tokens, and frequently fails due to hallucinated JSON keys or markdown formatting noise.

| Attribute | 🧠 System 2 (Frontier LLMs) | ⚡ System 1 (Jev / Laya) |
| :--- | :--- | :--- |
| **Cognitive Mode** | Slow, deliberative, generative | Fast, reflexive, judgmental |
| **Latency** | 2,000 – 6,000 ms | **30 – 150 ms** (10–50x faster) |
| **Output Type** | Autoregressive text / JSON strings | **Strict schemas** (`Boolean`, `Choice`, `Score`) |
| **Reliability** | Hallucination-prone, syntax drift | **100% type-safe, zero syntax errors** |
| **Cost** | \$5.00 – \$30.00 / M tokens | **\$0.05 – \$0.20 / M decisions** |
| **Ideal For** | Deep reasoning, writing code, planning | **Routing, tool gating, RAG reranking, triage** |

---

## The 4-Year Paradigm Evolution

```
2023: Raw Prompting ───────────────────► "Please reply ONLY with valid JSON" (Brittle, hallucination-heavy)
2024: Structured Outputs & Tools ──────► JSON formatting solved; latency (3-5s) and cost remain prohibitive
2025: Autonomous Agent Explosion ──────► Loops execute 50+ tool calls/task; $5/session burns token budgets
2026: The System One Revolution ───────► Reflexes decoupled: System 1 (70ms) routes & gates; System 2 reasons
```

---

## The Great Comparison

Senior engineers often ask: *"I already use Instructor, Pydantic, or Outlines. How is System One different?"*

| Framework | Paradigm | Underlying Mechanism | Typical Latency | Cost / 10k Calls | Failure Modes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Instructor / BAML** | System 2 Wrapper | Wraps standard LLM API call + validates output with Pydantic | 3,000 – 5,000 ms | \$30.00 – \$60.00 | Retries on invalid JSON; full token billing per retry |
| **Outlines / Guidance** | System 2 Constrained | Constrains autoregressive token decoding with regex/CFG masks | 1,200 – 2,500 ms | ~\$2.00 (GPU compute) | Still evaluates 7B–70B weights token-by-token sequentially |
| **System One (Jev / Laya)** | **Pure System 1** | **Non-autoregressive forward pass directly over decision logits** | **30 – 70 ms** | **\$0.15 (or \$0.00 local)** | **Zero parsing failures; mathematically type-bound** |

---

## Empirical Performance Benchmarks

Measured on standard production classification, tool gating, and passage reranking tasks:

| Metric | GPT-4o / Claude 3.7 | Instructor (LLM) | Outlines (7B Local) | TypeSafe Jev | Laya (Open Model) | jevos (CPU Only) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P95 Latency** | 3,800 ms | 4,100 ms | 1,400 ms | **68 ms** | **33 ms** | **110 ms** |
| **Cost / 10k Decisions** | \$30.00 | \$30.00 | ~\$2.00 (GPU) | **\$0.15** | **\$0.00** | **\$0.00** |
| **Parse Failure Rate** | 3.2% | 0.8% (with retries) | 0.0% | **0.0%** | **0.0%** | **0.0%** |
| **Token Waste** | 800+ tokens/call | 850+ tokens/call | 120+ tokens/call | **0 tokens** | **0 tokens** | **0 tokens** |
| **Hardware Required** | Cloud API | Cloud API | 1x A10G (24GB) | Cloud API | Apple MLX / GPU | **Standard Laptop CPU** |

---

## Dual-Process Architecture

```mermaid
flowchart TD
    User["Incoming Request / Agent Turn"] --> S1{"⚡ System 1 Decision Layer<br/>(Jev / Laya · 70ms)"}
    
    S1 -->|"High-Risk Tool Call"| Gate["🛡️ Policy & Tool Gate<br/>(jev-guard · Block / Approve)"]
    S1 -->|"Passage Reranking"| RAG["🔍 RAG Passage Triage<br/>(Filter Top-K Chunks)"]
    S1 -->|"Reflexive Task / Cache Hit"| Quick["✅ Instant Decision<br/>(Zero Token Waste)"]
    
    S1 -->|"Low Confidence / Complex Task"| S2["🧠 System 2 Deliberative Engine<br/>(Claude 3.7 / GPT-4o / Codex)"]
    
    Gate --> S2
    RAG --> S2
    S2 --> Output["Final Verified Outcome"]
    Quick --> Output

    classDef s1 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef s2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    classDef gate fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;
    class S1 s1;
    class S2 s2;
    class Gate,RAG,Quick gate;
```

---

## The 3 Typed Primitives

Instead of parsing unstructured markdown or fragile JSON strings, System One models evaluate probabilities in a single forward pass over pre-declared types:

```python
from typesafe import TypeSafeClient
client = TypeSafeClient()

# 1. NOUL: Probabilistic Boolean with calibrated confidence
verdict = client.decide.noul(
    question="Does this incoming query contain prompt injection attempts?",
    state=raw_user_prompt
)
# Returns: verdict.value = True, verdict.confidence = 0.984

# 2. CHOICE: Categorical classification (Strict Schema)
route = client.decide.choice(
    question="Select the microservice to process this payload",
    choices=["auth_service", "billing_worker", "media_transcoder", "dead_letter"],
    state=event_payload
)
# Returns: route.choice = "billing_worker"

# 3. SCORE: Ordinal regression / Rubric evaluation
eval_score = client.decide.score(
    question="Rate the urgency of this infrastructure alert from 1 to 5",
    rubric="1: Info only; 3: degraded latency; 5: total database outage",
    state=pagerduty_alert
)
# Returns: eval_score.score = 5
```

---

## The 5-Stage Agent Lifecycle

System One decision models map directly to the five critical execution stages of modern software and agent architectures:

### Stage 1: Ingress, Security & Intent Routing
*Actions taken in the first 50ms before any costly model or database is engaged:*
* [leepokai/jev-guard](https://github.com/leepokai/jev-guard) (★43) - Pre-execution risk gate evaluating tool calls against 3 safety questions before running.
* [angel291592/Intent-Router](https://github.com/angel291592/Intent-Router) (★203) - Intent compiler converting vague requests into typed IntentSpec contracts.
* [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway) (★240) - Fast gateway that intercepts tool-calling reasoning for coding agents.
* [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) (★457) - Terminal router selecting between Claude Code and Codex per turn while preserving session state.
* [nidhi-singh02/agent-router](https://github.com/nidhi-singh02/agent-router) (★90) - Quota-aware router that applies deterministic rules before escalating difficult queries to frontier LLMs.
* [thruwire/foreman](https://github.com/thruwire/foreman) (★596) - Agent supervisor and software factory foreman powered by typed decisions.
* [notque/vexjoy-agent](https://github.com/notque/vexjoy-agent) (★425) - Intelligent router dispatching plain-English requests to specialized agents.

### Stage 2: Context, RAG & Memory Economy
*Surgically optimizing context windows and retrieval without lossy summarization:*
* [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) (★7,055) - Replaces lossy LLM compaction with surgical pruning; drops unneeded tool calls while preserving code history verbatim.
* [hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache) (★73) - High-throughput local caching proxy for `(model, schema, state)` tuples; eliminates repeated API billing in CI.
* [UditAkhourii/quicksilver](https://github.com/UditAkhourii/quicksilver) (★75) - "Read widely, decide narrowly." High-speed triage filtering 187 files down to 4 key candidates before prompting.
* [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) (★152) - Post-execution hook that prunes command outputs before returning to the model; automatically whitelists errors and diffs.
* [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) (★95) - Evaluates 25-line text blocks with Jev; stubs irrelevant sections with recall pointers.
* [dzhng/jevgrep](https://github.com/dzhng/jevgrep) (★1,025) - Semantic code search CLI. Locates files by architectural purpose rather than brittle regex strings.
* [kyu1204/jgrep](https://github.com/kyu1204/jgrep) (★48) - Semantic code search tool matching what code does rather than what it is named.
* [milvus-io/bootcamp](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) - Official Milvus recipes combining vector search with fast Jev reranking, filtering, and search stopping.

### Stage 3: Agent Policy & Tool Gating
*Enforcing deterministic guardrails on autonomous actions:*
* [typesafe-ai/skills](https://github.com/typesafe-ai/skills) (★2,334) - **Official** reference skill package. Teaches agents how to formulate typed queries and use decision recipes.
* [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) (★431) - Model Context Protocol (MCP) server providing 11 standard decision tools (`jev_noul`, `jev_classify`, `jev_rerank`, `jev_review`, etc.).
* [itsmostafa/system-one-connector](https://github.com/itsmostafa/system-one-connector) (★326) - Go-based MCP connector providing direct access to low-latency decision models.
* [shitianfang/jev-use](https://github.com/shitianfang/jev-use) (★30) - Plugin for Claude Code and Codex that delegates steps requiring no text generation to Jev.
* [TheoOliveira/pi-jev](https://github.com/TheoOliveira/pi-jev) (★56) - Semantic tool routing and typed System One decisions for the Pi coding agent.
* [keeltrace/hermes-nerve](https://github.com/keeltrace/hermes-nerve) (★30) - Supervisory nervous system for Hermes agents, adding typed decision ranking and policy gates.

### Stage 4: Runtime Verification & Code Intelligence
*Verifying code correctness with real execution rather than synthetic guessing:*
* [reticlehq/reticle](https://github.com/reticlehq/reticle) (★904) - Runtime verification engine. Drives headless browsers and containers to verify agent completion claims against real outputs, returning structured `pass/fail` with line traces.
* [supercorp-ai/supercov](https://github.com/supercorp-ai/supercov) (★133) - Evaluates code diffs for uncovered execution branches and converts gaps into targeted test generation prompts.
* [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) (★628) - Multi-stage git diff reviewer: Noul risk matrix → file profile classification → severity scoring → routing.
* [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep) (★145) - Multilingual semantic code search matching architectural concepts across 6 programming languages.
* [keltokhy/jsort](https://github.com/keltokhy/jsort) (★25) - Sorts and prioritizes compiler warnings, linter feedback, and static analysis outputs by architectural severity.

### Stage 5: High-Speed Vision & Multimodal Loops
*Sub-100ms visual UI classification and action triage:*
* [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) (**★20,989**) - Ultra-low latency UI classification and action triage for autonomous browser automation.
* [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) (★728) - High-speed multimodal screen parsing and bounding box classification.
* [jev-chat/jev-chat-windows](https://github.com/jev-chat/jev-chat-windows) (★635) - Real-time screen capture + offline OCR + intent evaluation for desktop UI automation.
* [brnyxx/jev-ra](https://github.com/brnyxx/jev-ra) (★5) - High-speed browser automation for coding agents, 3–5x faster than conventional browser agents.

---

## Open-Weight Models & Local Runtimes

Run System One decisions locally on your own hardware or implement the `/v1/systemone` wire protocol:

### Wire-Compatible Local Servers (`/v1/systemone`)
Point your existing SDK client to `http://localhost:8765/v1`:

```bash
export TYPESAFE_BASE_URL="http://127.0.0.1:8765/v1"
```

* [jaredpalmer/kev](https://github.com/jaredpalmer/kev) (★7,537) - Drop-in `/v1/systemone` server based on Qwen3.5/3.8 (0.8B–27B). Compatible with TypeSafe SDKs; includes custom fine-tuning recipes.
* [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) (★768) - "The Ollama for Decision Models." Local daemon for downloading and serving Laya and typed decision models with one command.
* [feder-cr/jev](https://github.com/feder-cr/jev) (★1,068) - `jevos` GGUF engine running on consumer CPUs in 50–220ms without requiring a dedicated GPU.
* [razorback16/openjev](https://github.com/razorback16/openjev) (★484) - DiffusionGemma 26B reading directly from probability logits with multimodal image prompt support.
* [1Panel-dev/laya-server](https://github.com/1Panel-dev/laya-server) (★77) - Dockerized self-hosted Laya server with built-in Web UI and API key management.
* [allebee/jevk5](https://github.com/allebee/jevk5) (★121) - Apache-2.0 open-weight model with 0.775 accuracy on hard-tier decision evaluations.

### Open-Weight Decision Models
* [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) (**★27,165**) - Foundational open-weight non-autoregressive decision model. 100+ languages in a single forward pass, ~33ms latency. Weights on Hugging Face (`convaiinnovations/laya`).
* [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) (★6,530) - Optimized Apple Silicon MLX port of Laya weights. 13.4ms median latency with zero token generation overhead.
* [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) (★2,378) - 0.6B parameter ultra-compact replica for microsecond edge triage.
* [wfzyx/von](https://github.com/wfzyx/von) (★738) - Non-autoregressive model for discrete, probabilistic, and ordinal classification in under 25ms.
* [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) (★862) - Conversion framework (Nokia + Tencent) transforming arbitrary existing LLMs into calibrated decision models.

---

## Scientific Foundations & Research

Peer-reviewed literature, consensus evidence, and empirical benchmarks supporting the System One decision paradigm:

### Dual-Process & Cognitive Routing
* **R2R: Efficiently Navigating Divergent Reasoning Paths with Small-Large Model Token Routing** (NeurIPS 2025)  
  *Authors:* Tianyu Fu, Yi Ge, Yichen You, Enshu Liu, Zhihang Yuan, Guohao Dai, Shengen Yan, Huazhong Yang, Yu Wang (Tsinghua University)  
  *Links:* [arXiv:2505.21600](https://arxiv.org/abs/2505.21600) · [PDF](https://arxiv.org/pdf/2505.21600) · [Code (GitHub)](https://github.com/thu-nics/R2R)  
  *Finding:* Proves that delegating critical decision boundaries to specialized fast models while reserving LLMs for path synthesis delivers a 2.8× speedup and cuts latency by up to 70%.

* **Doing More with Less: A Survey on Routing Strategies for Resource Optimisation in Large Language Model-Based Systems** (2025)  
  *Authors:* Clovis Varangot-Reille, et al.  
  *Links:* [arXiv:2502.00409](https://arxiv.org/abs/2502.00409) · [PDF](https://arxiv.org/pdf/2502.00409)  
  *Finding:* Comprehensive taxonomy of similarity, supervised, and generative routing strategies, proving dynamic triage systems maintain high accuracy at a fraction of frontier compute cost.

* **Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing** (ICLR 2024)  
  *Authors:* Dujian Ding, et al.  
  *Links:* [arXiv:2404.14618](https://arxiv.org/abs/2404.14618) · [OpenReview](https://openreview.net/forum?id=02f3mUtqnM) · [PDF](https://arxiv.org/pdf/2404.14618)  
  *Finding:* Demonstrates up to 60% API cost reductions by placing lightweight classifiers ahead of generative LLMs with zero quality degradation.

### Constrained Schemas & Zero Hallucination
* **Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning** (EMNLP 2023)  
  *Authors:* Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West (EPFL)  
  *Links:* [arXiv:2305.13971](https://arxiv.org/abs/2305.13971) · [PDF](https://arxiv.org/pdf/2305.13971) · [DOI](https://doi.org/10.18653/v1/2023.emnlp-main.687)  
  *Finding:* Enforces formal context-free grammars (JSON/YAML) during decoding, completely eliminating syntactic failures and hallucinated fields.

* **JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models** (2025)  
  *Authors:* Saibo Geng, Hudson Cooper, Michal Moskal, Julian Berman, Eric Horvitz, Harsha Nori (Microsoft Research & EPFL)  
  *Links:* [arXiv:2501.10868](https://arxiv.org/abs/2501.10868) · [PDF](https://arxiv.org/pdf/2501.10868)  
  *Finding:* Verifies 100% formal schema compliance across complex nested schemas using grammar-guided decoding frameworks.

* **Automata-Based Constraints for Language Model Decoding** (2024)  
  *Authors:* Terry Koo, Frederick Liu, Luheng He (Google DeepMind)  
  *Links:* [arXiv:2407.08103](https://arxiv.org/abs/2407.08103) · [PDF](https://arxiv.org/pdf/2407.08103)  
  *Finding:* Applies finite-state automata theory to compute closed-form masks for regular and deterministic context-free languages during decoding.

### Model Cascades, Calibration & Safety
* **UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing** (2026)  
  *Authors:* Varun Kotte  
  *Links:* [arXiv:2605.18796](https://arxiv.org/abs/2605.18796) · [PDF](https://arxiv.org/pdf/2605.18796)  
  *Finding:* Calibration-first router uses isotonic regression to map uncertainty to error probability, cutting inference costs by 31% and dropping Expected Calibration Error (ECE) from 0.12 to 0.03.

* **Safety Guardrails for LLM-Enabled Robots** (IEEE Robotics and Automation Letters 2025)  
  *Authors:* Zachary Ravichandran, Alexander Robey, Vijay Kumar, George J. Pappas, Hamed Hassani (University of Pennsylvania)  
  *Links:* [arXiv:2503.07885](https://arxiv.org/abs/2503.07885) · [PDF](https://arxiv.org/pdf/2503.07885)  
  *Finding:* Verifies that deterministic policy gating (RoboGuard) reduces unsafe autonomous agent plan executions from 92% to under 3%.

* **Retrieve Fast, Rerank Smart: Cooperative and Joint Approaches for Improved Retrieval** (TACL 2021)  
  *Authors:* Gregor Geigle, Jonas Pfeiffer, Nils Reimers, Iryna Gurevych  
  *Links:* [arXiv:2104.09277](https://arxiv.org/abs/2104.09277) · [PDF](https://arxiv.org/pdf/2104.09277)  
  *Finding:* Proves that sub-100ms cross-encoder reranking eliminates vector search noise and outperforms pure bi-encoder embeddings by wide margins.

---

## SDKs by Language & Frameworks

### Language Libraries
* **Python**: `pip install typesafe` — Official TypeSafe SDK for Python with Pydantic integration.
* **TypeScript / Node.js**: `npm i @typesafe-ai/sdk` — First-class typed SDK with native Zod schema support.
* **Open Models Python**: `pip install laya` — Direct inference and serving for open-weight Laya models.
* **Go**: `go get github.com/typesafe-ai/typesafe-go` — High-concurrency client for Go microservices.
* **Rust**: `typesafe-rs` — Memory-efficient, async Tokio bindings for edge and systems runtimes.

### Framework Adapters
* **LangChain**: Use `DecisionRunnable` to create deterministic conditional branching and router nodes without invoking LLM chains.
* **LlamaIndex**: `llama-index-postprocessor-jev-rerank` — Drop-in node postprocessor that scores passage relevance in 70ms before synthesizer execution.
* **DSPy**: Integrate System One classifiers as fast predictors for assertions and constrained teleprompters.
* **CrewAI & AutoGen**: Implement pre-action guardrails by hooking `jev.decide.noul` into agent tool execution callbacks.

---

## Production Blueprints

### Blueprint 1: The Sub-100ms Agent Tool Gatekeeper
Prevent catastrophic execution (e.g., unexpected SQL drops, destructive terminal commands) before they reach your infrastructure:

```python
from typesafe import TypeSafeClient

client = TypeSafeClient()

def safe_tool_gate(tool_name: str, arguments: dict, user_intent: str) -> bool:
    """Evaluates safety in 70ms before executing any autonomous tool."""
    state = {
        "tool": tool_name,
        "args": arguments,
        "intent": user_intent
    }
    
    # Check if the tool invocation adheres strictly to user authorization
    verdict = client.decide.noul(
        question="Is this specific tool execution explicitly requested and safe under the given user intent?",
        state=state
    )
    
    if not verdict.value or verdict.confidence < 0.95:
        print(f"Blocked tool execution: {tool_name} (Confidence: {verdict.confidence:.2%})")
        return False
        
    return True
```

### Blueprint 2: High-Speed RAG Passage Triage
Eliminate irrelevant retrieval noise before prompting your generative LLM:

```python
def filter_passages(query: str, retrieved_chunks: list[str]) -> list[str]:
    """Prunes retrieved chunks down to high-confidence evidence in parallel."""
    relevant_chunks = []
    
    for chunk in retrieved_chunks:
        check = client.decide.noul(
            question=f"Does this passage contain direct factual evidence to answer: '{query}'?",
            state=chunk
        )
        if check.value and check.confidence >= 0.85:
            relevant_chunks.append(chunk)
            
    return relevant_chunks
```

### Blueprint 3: Zero-Latency Microservice Router
Route incoming webhooks or user tickets without paying frontier model costs:

```python
def dispatch_event(payload: dict) -> str:
    """Routes payloads to the correct microservice queue in 50ms."""
    route = client.decide.choice(
        question="Which system domain does this incoming event belong to?",
        choices=["billing", "user_auth", "infra_alert", "marketing_spam"],
        state=payload
    )
    return route.choice
```

---

## Harness Integration Quickstart

### 1. Antigravity (AGY) & Gemini Environments
Antigravity and Gemini workflows benefit from offloading binary safety checks and schema triage to Jev via the Model Context Protocol (MCP):

* **AGY & Gemini MCP Configuration (`~/.gemini/antigravity/mcp_config.json` or workspace settings):**
```json
{
  "mcpServers": {
    "jev": {
      "command": "npx",
      "args": ["-y", "jev-mcp"],
      "env": {
        "TYPESAFE_API_KEY": "${TYPESAFE_API_KEY}"
      }
    }
  }
}
```

### 2. OpenAI ChatGPT, Codex & Assistants
Use Jev as an upfront deterministic policy and tool call gate before passing state to GPT-4o or Codex:

```python
from openai import OpenAI
from typesafe import TypeSafeClient

openai_client = OpenAI()
jev = TypeSafeClient()

def execute_agent_step(action_proposal: dict):
    # Screen tool execution proposals in 70ms before committing destructive operations
    gate = jev.decide.noul(
        question="Is this action safe to execute without explicit human approval?",
        state=action_proposal
    )
    if not gate.value:
        raise PermissionError(f"Action flagged by Jev safety gate: {action_proposal}")
    
    # Proceed to OpenAI function call execution
```

### 3. OpenCode, Cursor & Windsurf via MCP
Add to your MCP configuration (`opencode.json` or `cursor-settings.json`):

```json
{
  "mcpServers": {
    "jev": {
      "command": "npx",
      "args": ["-y", "jev-mcp"],
      "env": {
        "TYPESAFE_API_KEY": "${TYPESAFE_API_KEY}"
      }
    }
  }
}
```
*Gives your agent 11 calibrated tools: `jev_noul`, `jev_classify`, `jev_rerank`, `jev_review`, etc.*

### 4. Claude Code & Universal Skills CLI
Install the official skill package natively:

```bash
# Claude Code Plugin
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai

# Codex / Universal Coding Agents (skills.sh)
npx skills add typesafe-ai/skills --skill typesafe-ai -g
```

### 5. Local Offline Runtimes (Kev / Ollaya / jevos)
Switch any agent or harness from cloud billing to local offline inference:

```bash
# Point to your local Kev or Ollaya server
export TYPESAFE_BASE_URL="http://127.0.0.1:8765/v1"

# Or run CPU-only boolean decisions via jevos (50-220ms)
uv run jev serve --device cpu --port 8765
```

---

## Explore the 7,414 Repository Catalogs

Browse the full dataset of 7,414 open-source repositories classified by domain and scored from 0 to 100:

| Category | Repositories | Description | Catalog Link |
| :--- | ---: | :--- | :--- |
| **Tier-A Curated Shortlist** | 122 | Production-vetted repositories mapped to agent architectures | [`catalog/01-tier-a.md`](catalog/01-tier-a.md) |
| **Routing & Model Dispatch** | 926 | Dynamic routers, meta-controllers, model cascades | [`catalog/10-domain-routing.md`](catalog/10-domain-routing.md) |
| **Open Decision Models** | 1,029 | Laya, Kev, edge runtimes, GGUF, local servers | [`catalog/10-domain-inference-model.md`](catalog/10-domain-inference-model.md) |
| **Document, Data & SQL** | 703 | Schema extraction, data triage, structured parsing | [`catalog/10-domain-doc-data.md`](catalog/10-domain-doc-data.md) |
| **Skills, Plugins & Tooling** | 682 | Coding agent skills, MCP servers, extensions | [`catalog/10-domain-skills-tools.md`](catalog/10-domain-skills-tools.md) |
| **Browser & Computer Use** | 358 | UI automation, DOM triage, vision action loops | [`catalog/10-domain-browser-gui.md`](catalog/10-domain-browser-gui.md) |
| **Memory & Context Economy** | 227 | Surgical pruning, context compaction, caches | [`catalog/10-domain-memory-context.md`](catalog/10-domain-memory-context.md) |
| **Code Review & Linting** | 183 | Runtime verification, diff screening, security gates | [`catalog/10-domain-code-review-lint.md`](catalog/10-domain-code-review-lint.md) |
| **Games, Robotics & Embodied** | 291 | Fast decision loops, microsecond edge agents | [`catalog/10-domain-games-robotics.md`](catalog/10-domain-games-robotics.md) |
| **Trading & Financial AI** | 134 | Microstructure decisions, event triage | [`catalog/10-domain-trading.md`](catalog/10-domain-trading.md) |
| **Search, Retrieval & SEO** | 121 | Passage rerankers, semantic grep, query routing | [`catalog/10-domain-search-seo.md`](catalog/10-domain-search-seo.md) |
| **Agent Frameworks** | 29 | Autonomous agent architectures with decision layers | [`catalog/10-domain-agent-framework.md`](catalog/10-domain-agent-framework.md) |
| **Curated Indexes** | 28 | Awesome lists, community directories | [`catalog/10-domain-awesome-index.md`](catalog/10-domain-awesome-index.md) |
| **Discovery Methodology** | — | Why topic-only search is blind; 11-signal recursive pipeline | [`catalog/00-methodology.md`](catalog/00-methodology.md) |
| **Scientific Evidence** | — | Full paper takeaways and consensus citations | [`catalog/04-scientific-consensus.md`](catalog/04-scientific-consensus.md) |
| **Long Tail (Metadata Only)** | 2,541 | Broad tail kept for completeness | [`catalog/90-long-tail.md`](catalog/90-long-tail.md) |

---

## Official Resources & Community

* [TypeSafe Official Documentation](https://docs.typesafe.ai) — Official API specifications, SDK guides, and reference models.
* [TypeSafe Official Cookbooks](https://docs.typesafe.ai/cookbooks) — Worked examples for RAG classification, citation double-checking, and parallel evaluation.
* [Laya Model Weights on Hugging Face](https://huggingface.co/convaiinnovations/laya) — Direct access to foundational open decision weights.
* [OpenRouter Jev Cookbook](https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev) — Recipes for tool call gating with confidence thresholds.

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on formatting, quality standards, and submission guidelines.

---

## License

This repository is licensed under the [MIT License](LICENSE).  
Linked projects retain their respective authors' licenses.
