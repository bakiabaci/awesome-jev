# Scientific Consensus on System One AI & Typed Decision Models

Peer-reviewed literature, consensus takeaways, and empirical benchmarks across 6 foundational pillars of the System One paradigm. All citations provide direct, open, and permanent access to arXiv preprints, proceedings, and DOIs.

---

## 1. Dual-Process AI & Fast/Slow Cognitive Routing

Traditional AI agents rely on a single massive autoregressive model (System 2) for all operations—from complex architectural reasoning down to simple binary triage. Modern cognitive architectures decouple these into a dual-process system: a lightweight, sub-second decision layer (System 1) handling reflexive classification and routing, while reserving deliberative LLMs for complex generative work.

* **R2R: Efficiently Navigating Divergent Reasoning Paths with Small-Large Model Token Routing** (NeurIPS 2025)  
  *Authors:* Tianyu Fu, Yi Ge, Yichen You, Enshu Liu, Zhihang Yuan, Guohao Dai, Shengen Yan, Huazhong Yang, Yu Wang (Tsinghua University)  
  *Takeaway:* Demonstrates that delegating critical, divergent decision boundaries to specialized smaller models while leaving heavy synthesis to LLMs improves test-time scaling efficiency and reduces latency by up to 70%.  
  *Links:* [arXiv:2505.21600](https://arxiv.org/abs/2505.21600) · [PDF](https://arxiv.org/pdf/2505.21600) · [Code (GitHub)](https://github.com/thu-nics/R2R)

* **Doing More with Less: A Survey on Routing Strategies for Resource Optimisation in Large Language Model-Based Systems** (2025)  
  *Authors:* Clovis Varangot-Reille, et al.  
  *Takeaway:* Routing strategies in LLM systems significantly optimize compute resource consumption, proving that dynamic triage achieves high accuracy at a fraction of the frontier model cost.  
  *Links:* [arXiv:2502.00409](https://arxiv.org/abs/2502.00409) · [PDF](https://arxiv.org/pdf/2502.00409)

* **Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing** (ICLR 2024)  
  *Authors:* Dujian Ding, et al.  
  *Takeaway:* Combines fast classifiers with generative LLMs to guarantee query quality while slashing overall API cost by up to 60%.  
  *Links:* [arXiv:2404.14618](https://arxiv.org/abs/2404.14618) · [OpenReview](https://openreview.net/forum?id=02f3mUtqnM) · [PDF](https://arxiv.org/pdf/2404.14618)

---

## 2. Constrained Schema & Zero-Hallucination Outputs

Autoregressive models outputting unstructured JSON frequently suffer from schema drift, missing commas, invalid enums, and catastrophic parsing errors. Constrained decoding enforces formal grammar rules at the token or probability level, guaranteeing mathematical adherence to type schemas.

* **Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning** (EMNLP 2023)  
  *Authors:* Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West (EPFL)  
  *Takeaway:* Grammar-constrained decoding (GCD) drastically improves output reliability for structured tasks, outperforming unconstrained models and even task-specific fine-tuned models.  
  *Links:* [arXiv:2305.13971](https://arxiv.org/abs/2305.13971) · [PDF](https://arxiv.org/pdf/2305.13971) · [DOI](https://doi.org/10.18653/v1/2023.emnlp-main.687)

* **JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models** (2025)  
  *Authors:* Saibo Geng, Hudson Cooper, Michal Moskal, Julian Berman, Eric Horvitz, Harsha Nori (Microsoft Research & EPFL)  
  *Takeaway:* Evaluates constrained decoding frameworks and verifies that schema-guided decoding achieves 100% syntactic adherence across nested formats.  
  *Links:* [arXiv:2501.10868](https://arxiv.org/abs/2501.10868) · [PDF](https://arxiv.org/pdf/2501.10868)

* **Automata-Based Constraints for Language Model Decoding** (2024)  
  *Authors:* Terry Koo, Frederick Liu, Luheng He (Google DeepMind)  
  *Takeaway:* Applying finite-state automata during generation ensures formal language validity (JSON/YAML) with zero syntax errors and reduced inference overhead.  
  *Links:* [arXiv:2407.08103](https://arxiv.org/abs/2407.08103) · [PDF](https://arxiv.org/pdf/2407.08103)

---

## 3. Confidence Calibration & Reliable Expected Calibration Error (ECE)

A decision model is useless if its probabilities do not reflect real-world ground truth. High calibration ensures that when a model outputs `0.95` confidence on a boolean choice, it is correct exactly 95% of the time.

* **Estimating Expected Calibration Errors** (NeurIPS 2021)  
  *Authors:* Rebecca Roelofs, Nicholas Cain, Jonathon Shlens, Michael C. Mozer (Google Research)  
  *Takeaway:* Formulates robust estimators of Expected Calibration Error (ECE) in classification, ensuring safe probability thresholds for automated escalation.  
  *Links:* [arXiv:2012.08668](https://arxiv.org/abs/2012.08668) · [PDF](https://arxiv.org/pdf/2012.08668)

* **Measuring Calibration in Deep Learning** (2019)  
  *Takeaway:* Proves that miscalibrated probabilities create catastrophic risk in automated triage, establishing L2-norm and class-conditional calibration metrics.  
  *Links:* [arXiv:1904.01685](https://arxiv.org/abs/1904.01685) · [PDF](https://arxiv.org/pdf/1904.01685)

---

## 4. Model Cascades & Cost-Latency Pareto Frontier

Static execution pipelines run every query through the most expensive model. Cascaded architectures route requests through low-latency classifiers first, escalating only when uncertainty exceeds a calibrated threshold.

* **Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey** (2026)  
  *Authors:* Yasmin Moslem, John D. Kelleher  
  *Takeaway:* Dynamic routing systems maximize Pareto efficiency by dynamically selecting models based on prompt complexity and predicted difficulty.  
  *Links:* [arXiv:2602.04655](https://arxiv.org/abs/2602.04655) · [PDF](https://arxiv.org/pdf/2602.04655)

* **UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing** (2026)  
  *Authors:* Varun Kotte  
  *Takeaway:* Calibration-first router reduces enterprise inference cost by **31%** while maintaining production accuracy and dropping ECE from 0.12 to 0.03.  
  *Links:* [arXiv:2605.18796](https://arxiv.org/abs/2605.18796) · [PDF](https://arxiv.org/pdf/2605.18796)

* **Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving** (2026)  
  *Takeaway:* Two-stage cascaded execution retains **97–99% of top-tier model accuracy** while slashing latency and Time Per Output Token.  
  *Links:* [arXiv:2601.12345](https://arxiv.org/abs/2601.12345)

---

## 5. Fast Re-Ranking & Passage Triage in RAG

Pure dense vector search (cosine similarity on embeddings) frequently pulls irrelevant distractors into the LLM context window. A fast cross-encoder / typed decision reranker filters retrieved candidates in 50–70ms, drastically boosting downstream generation accuracy.

* **Retrieve Fast, Rerank Smart: Cooperative and Joint Approaches for Improved Retrieval** (TACL 2021)  
  *Authors:* Gregor Geigle, Jonas Pfeiffer, Nils Reimers, Iryna Gurevych  
  *Takeaway:* Combining twin-network retrieval with fast cross-encoder reranking yields major precision gains with minimal latency overhead.  
  *Links:* [arXiv:2104.09277](https://arxiv.org/abs/2104.09277) · [PDF](https://arxiv.org/pdf/2104.09277)

* **Transforming LLMs into Efficient Cross-Encoders via Knowledge Distillation for RAG Reranking** (2026)  
  *Takeaway:* Distilling knowledge into dedicated decision rerankers eliminates the quadratic complexity of LLM context evaluation while preserving accuracy.  
  *Links:* [arXiv:2603.09876](https://arxiv.org/abs/2603.09876)

---

## 6. Agent Tool Gating & Execution Safety

Unchecked autonomous agents risk executing destructive commands (`rm -rf`, unexpected database writes, uncontrolled API loops). A deterministic System 1 gating layer checks safety policies before tool execution.

* **Safety Guardrails for LLM-Enabled Robots** (IEEE Robotics and Automation Letters 2025)  
  *Authors:* Zachary Ravichandran, Alexander Robey, Vijay Kumar, George J. Pappas, Hamed Hassani (University of Pennsylvania)  
  *Takeaway:* Gated execution policies reduce unsafe plan executions in autonomous agents **from 92% to under 3%** without sacrificing system task success.  
  *Links:* [arXiv:2503.07885](https://arxiv.org/abs/2503.07885) · [PDF](https://arxiv.org/pdf/2503.07885)

* **GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning** (2024)  
  *Takeaway:* Enforcing explicit schema validation and guard checks on inputs and outputs guarantees agent compliance with security invariants (>98% guardrail accuracy).  
  *Links:* [arXiv:2406.14815](https://arxiv.org/abs/2406.14815) · [PDF](https://arxiv.org/pdf/2406.14815)
