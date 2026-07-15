# Project Evidence Pages Design

## Objective

Turn the first three homepage project summaries into evidence-backed case studies that make the work discussable in an embodied-AI or Agent interview without exposing private code or overstating results.

## Information architecture

- Keep the homepage concise and preserve its existing visual hierarchy.
- Add a `Read project →` link to the first three project entries.
- Publish three standalone pages under `/projects/`:
  - `/projects/agent-memory/`
  - `/projects/calling-agent/`
  - `/projects/qwen3-reranker/`
- Reuse one editorial project-page layout so the pages feel like a coherent research portfolio.

Each page follows the same narrative:

1. Research or engineering question.
2. One-sentence answer.
3. System or method diagram.
4. What was built.
5. Evidence and evaluation protocol.
6. Honest limitations or next experiment.

## Page 1: EvoWalker Agent Memory

Position this as the flagship research project and the clearest bridge to embodied intelligence.

- Problem: long-horizon agents must remember prior events while tracking how facts change.
- Method: natural-language fact nodes, intra-session / cross-session / update relations, valid intervals, query-conditioned random walk, and multi-granularity raw-evidence recovery.
- Verified result: 1,321 / 1,540 correct on LoCoMo non-adversarial categories under the LoCoMo official LLM-as-a-Judge protocol, 85.78% overall.
- Category results may be shown with protocol labels: multi-hop 75.89%, temporal 80.69%, open-domain 71.88%, single-hop 92.63%.
- Boundary: do not claim component causality because matched ablations are incomplete; do not present the existing raw-only LongMemEval score as an EvoWalker result.
- Embodied-AI bridge: persistent state, temporal consistency, and traceable evidence are reusable capabilities for agents operating across long task horizons.

## Page 2: Strategy-Driven AI Calling Agent

Position this as a production Agent-systems case study, not a model-training project.

- Problem: open-ended generation must be turned into an inspectable, recoverable business workflow.
- System: Memory writes the conversation state; cached predictions are reranked into a fast path; misses fall back to Router → Generator; optional Verifier reviews and rewrites; the response updates Memory and triggers the next prediction.
- Evidence: describe the implemented modules and the offline replay harness, but publish no internal code, customer data, endpoints, prompts, or credentials.
- Boundary: do not claim SFT, DPO, LoRA, GRPO, FSM implementation, conversion lift, accuracy, or latency improvement for this repository.
- Interview hook: explain the engineering decision between predictable control and model flexibility.

## Page 3: Qwen3 Reranker Fine-tuning

Position this as the model-training case study.

- Problem: general semantic similarity does not reliably capture domain-specific clause relevance.
- Method: Qwen3-Reranker-0.6B with LoRA SFT and pointwise yes/no relevance supervision; one positive and three negatives per sample.
- Current data assets: 15,704 training samples and 1,749 validation samples.
- Archived evaluation: checkpoint-135 reached 85.39% accuracy and 93.12% negative recall on an earlier validation split; label it explicitly as an archived experiment, not the current-data result.
- Boundary: do not describe the model as a full-corpus retriever and do not merge checkpoint-135 metrics with the current dataset version.
- Interview hook: show how hard-negative design and error analysis matter more than merely naming a fine-tuning framework.

## Visual direction

- Preserve the white paper, dark ink, muted blue, serif-heading language of the homepage.
- Use a narrow reading column for prose and a wider evidence band for diagrams and metrics.
- Diagrams are HTML/CSS, not screenshots, so they stay responsive and accessible.
- Metrics appear as protocol-labelled evidence cards, never as promotional hero claims.
- Mobile width must remain free of horizontal overflow at 390px and 375px.

## Content and privacy constraints

- Do not publish private repository links or source paths.
- Do not include customer names, raw conversations, product scripts, API endpoints, IDs, keys, or internal prompts.
- Do not use `SOTA`, `state-of-the-art`, or unqualified gain language.
- Every number must include its dataset/split/protocol context on the same page.
- The fourth homepage project remains a summary only because its public evidence is not yet strong enough for a case study.

## Acceptance criteria

- All three routes exist and are linked from the homepage.
- Each page contains the shared narrative sections and a distinct diagram.
- The Agent Memory page contains the verified LoCoMo protocol and limitations.
- The Calling Agent page contains no training or business-performance claims.
- The Reranker page separates current data assets from the archived checkpoint result.
- Existing homepage identity, CV, email, GitHub link, experience boundary, and accessibility behavior remain intact.
- Source tests, rendered-site tests, link checks, and 1440px / 390px viewport checks pass.
