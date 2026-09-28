# Self-Hosted & Open Weights — Running System One Without the Cloud API

While TypeSafe Jev operates as a managed cloud service, a vibrant ecosystem of **open-weight models and self-hosted runtimes** has emerged. Many of these projects implement the exact `/v1/systemone` wire protocol, allowing existing SDK clients to switch from cloud to local execution by altering a single base URL environment variable.

---

## 1. Wire-Compatible Drop-In Servers (`/v1/systemone`)

These runtimes implement TypeSafe's REST protocol. Point your application or agent to `http://localhost:8765/v1` to run decisions entirely offline.

| Repository | Stars | Base Architecture | Target Hardware | Notes |
| :--- | ---: | :--- | :--- | :--- |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 7,513 | Qwen3.5 / 3.8 (0.8B to 27B) | Laptop to Single GPU | Drop-in compatible with TypeSafe Python and TS SDKs. Includes training recipes for domain-specific fine-tuning on labeled internal datasets. |
| [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) | 752 | Laya, decider, NLI, GLiClass | Local daemon (Mac/Linux/Win) | "The Ollama for Decision Models." Seamless daemon serving multiple typed models with single-command downloads. |
| [feder-cr/jev](https://github.com/feder-cr/jev) | 1,066 | jevos (GGUF / llama.cpp) | **CPU Only (50–220ms)** | Runs fast boolean triage (`Noul`) on standard consumer CPUs without requiring a dedicated GPU. 8,192 token context. `uv run jev serve --device cpu`. |
| [razorback16/openjev](https://github.com/razorback16/openjev) | 479 | DiffusionGemma 26B-A4B | vLLM + NVIDIA GPU / Apple MLX | Reads directly from output probability logits rather than generating text tokens. Supports visual multimodal decision prompts. |
| [1Panel-dev/laya-server](https://github.com/1Panel-dev/laya-server) | 77 | Laya (Upstream) | Single Docker container | Production Docker image with built-in Web UI, API key management, and `/health/ready` endpoints. |
| [allebee/jevk5](https://github.com/allebee/jevk5) | 121 | JevK5 (4B / 9B) | Consumer GPU | Apache-2.0 open weights. Benchmarks report 0.775 accuracy on hard-tier decision evaluations. |

---

## 2. Reference Open-Weight Architectures

Foundational open weights trained specifically for non-autoregressive, schema-constrained decision making:

| Repository | Stars | Description | Performance Profile |
| :--- | ---: | :--- | :--- |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | **27,095** | The largest open project in the ecosystem. Non-autoregressive decision model supporting 100+ languages in a single forward pass. Trained with RLCD against strictly proper scoring rules. | **~33 ms latency**. Weights available at `convaiinnovations/laya` on Hugging Face. PyPI package: `laya`. |
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 6,520 | Optimized Apple Silicon MLX port of Laya weights. | **Median 13.4 ms latency**. Zero output token generation overhead; operates without PyTorch or Transformers dependencies. |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | 2,375 | 0.6B parameter ultra-compact replica. Computes full probability distributions with zero sequential token generation. | Microsecond inference; tested on real-time game agents (ViZDoom, Snake). |
| [wfzyx/von](https://github.com/wfzyx/von) | 737 | Non-autoregressive model for discrete, probabilistic, and ordinal classification. | **Sub-25 ms latency**. |
| [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) | 859 | Conversion framework (Nokia + Tencent) that converts arbitrary existing LLMs into calibrated decision models. | Ideal for converting custom fine-tuned weights into fast decision engines. |

---

## 3. How to Switch from Cloud to Local in Code

Because these servers adhere to the standard wire protocol, switching requires setting a single environment variable:

```bash
# In your terminal or .env:
export TYPESAFE_BASE_URL="http://127.0.0.1:8765/v1"
```

```python
import os
from typesafe import TypeSafeClient

# Points to your local Kev or Ollaya server automatically:
client = TypeSafeClient(
    base_url=os.getenv("TYPESAFE_BASE_URL", "http://127.0.0.1:8765/v1")
)

decision = client.decide.noul(
    question="Is this request authorized?",
    state={"role": "admin", "action": "delete"}
)
print(decision.value)
```
