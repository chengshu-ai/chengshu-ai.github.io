# Project Evidence Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add three evidence-backed project detail pages and connect them to the existing research portfolio homepage.

**Architecture:** Jekyll renders three Markdown pages through one `_layouts/project.html` layout. Each page owns its narrative and semantic HTML while the shared layout provides navigation and shell; `_sass/_site.scss` supplies responsive editorial, diagram, metric, and evidence styles. Python source-contract tests lock routes, claims, evidence labels, and privacy boundaries before implementation.

**Tech Stack:** Jekyll, Liquid, Markdown/Kramdown, HTML5, SCSS, Python `unittest`, Playwright CLI for viewport verification.

## Global Constraints

- Preserve the existing homepage visual language and all current identity, CV, email, GitHub, experience, mobile, and accessibility behavior.
- Publish exactly three new routes: `/projects/agent-memory/`, `/projects/calling-agent/`, and `/projects/qwen3-reranker/`.
- Do not publish private repository links, filesystem paths, customer names, raw conversations, prompts, endpoints, IDs, keys, or internal configuration.
- Do not use `SOTA`, `state-of-the-art`, or unqualified performance-gain language.
- Agent Memory may report only the protocol-labelled LoCoMo 1,321/1,540 = 85.78% result and category breakdown; it must state that matched ablations and full EvoWalker LongMemEval evaluation remain incomplete.
- Calling Agent must not claim SFT, DPO, LoRA, GRPO, FSM implementation, conversion lift, accuracy, or latency improvement.
- Reranker must label 15,704/1,749 as current data assets and checkpoint-135 metrics as an archived evaluation on an earlier validation split.
- The fourth homepage project remains summary-only.
- Mobile layouts must have no horizontal overflow at 390px and 375px; visible links retain a minimum 44px tap height where applicable.

---

### Task 1: Detail-page content contract

**Files:**
- Create: `tests/test_project_pages.py`

**Interfaces:**
- Consumes: planned routes and exact evidence language from the design spec.
- Produces: a source-level contract that later tasks must satisfy.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_project_pages.py` with tests that require the three page files, `layout: project`, homepage links, the shared section labels, Agent Memory protocol and limitation text, Calling Agent fast/fallback modules and forbidden training claims, and Reranker current/archived version labels.

- [ ] **Step 2: Run the tests and verify RED**

Run: `python3 -m unittest tests.test_project_pages -v`

Expected: FAIL because the three project pages and project layout do not exist.

- [ ] **Step 3: Commit the failing contract**

```bash
git add tests/test_project_pages.py
git commit -m "test: define project evidence page contract"
```

### Task 2: Shared editorial project-page foundation

**Files:**
- Create: `_layouts/project.html`
- Modify: `_sass/_site.scss`

**Interfaces:**
- Consumes: page front matter fields `title`, `kicker`, `question`, `answer`, and `description`.
- Produces: `.project-page`, `.project-hero`, `.project-facts`, `.project-narrative`, `.system-diagram`, `.evidence-grid`, `.project-boundary`, and `.project-next` components used by all three pages.

- [ ] **Step 1: Add a source assertion for the layout shell and responsive selectors**

Extend `tests/test_project_pages.py` to assert the layout renders the kicker, question, answer, Back to selected work link, and content slot, and that `_sass/_site.scss` declares all shared component selectors plus mobile rules.

- [ ] **Step 2: Run the focused tests and verify RED**

Run: `python3 -m unittest tests.test_project_pages -v`

Expected: FAIL on the missing layout and selectors.

- [ ] **Step 3: Implement the shared layout and styles**

Build a compact project masthead followed by a full-width content slot. Add responsive editorial grids, evidence cards, labelled CSS diagrams, metric treatments, breadcrumb/tap-target styles, and reduced-motion behavior using the existing design tokens.

- [ ] **Step 4: Run focused and regression tests**

Run: `python3 -m unittest tests.test_project_pages tests.test_redesign_source tests.test_project_data -v`

Expected: project-page layout tests pass; page-content tests remain failing until Tasks 3-5; existing regressions pass.

- [ ] **Step 5: Commit the foundation**

```bash
git add _layouts/project.html _sass/_site.scss tests/test_project_pages.py
git commit -m "feat: add project evidence page foundation"
```

### Task 3: EvoWalker Agent Memory flagship page

**Files:**
- Create: `projects/agent-memory.md`

**Interfaces:**
- Consumes: shared `project` layout and its semantic component classes.
- Produces: the public `/projects/agent-memory/` case study.

- [ ] **Step 1: Run the Agent Memory contract and verify RED**

Run: `python3 -m unittest tests.test_project_pages.ProjectPageContract.test_agent_memory_evidence -v`

Expected: FAIL because `projects/agent-memory.md` does not exist.

- [ ] **Step 2: Implement the page**

Write the research question, one-sentence method, three-stage architecture diagram, method narrative, protocol-labelled LoCoMo evidence cards, category breakdown, embodied-AI bridge, and explicit incomplete-ablation / LongMemEval boundary. Do not include private links or alternative legacy result versions.

- [ ] **Step 3: Run the focused test and verify GREEN**

Run: `python3 -m unittest tests.test_project_pages.ProjectPageContract.test_agent_memory_evidence -v`

Expected: PASS.

- [ ] **Step 4: Commit**

```bash
git add projects/agent-memory.md
git commit -m "feat: add agent memory research case study"
```

### Task 4: Strategy-Driven AI Calling Agent page

**Files:**
- Create: `projects/calling-agent.md`

**Interfaces:**
- Consumes: shared `project` layout and diagram/evidence classes.
- Produces: the public `/projects/calling-agent/` case study.

- [ ] **Step 1: Run the Calling Agent contract and verify RED**

Run: `python3 -m unittest tests.test_project_pages.ProjectPageContract.test_calling_agent_evidence -v`

Expected: FAIL because `projects/calling-agent.md` does not exist.

- [ ] **Step 2: Implement the page**

Write the Memory → cached prediction → fast-path/fallback architecture, modular responsibilities, offline replay evidence, system-design tradeoff, and public boundary. Use no training, FSM, compliance-guarantee, conversion, accuracy, or latency-gain claims.

- [ ] **Step 3: Run the focused test and verify GREEN**

Run: `python3 -m unittest tests.test_project_pages.ProjectPageContract.test_calling_agent_evidence -v`

Expected: PASS.

- [ ] **Step 4: Commit**

```bash
git add projects/calling-agent.md
git commit -m "feat: add calling agent systems case study"
```

### Task 5: Qwen3 Reranker training page

**Files:**
- Create: `projects/qwen3-reranker.md`

**Interfaces:**
- Consumes: shared `project` layout and diagram/evidence classes.
- Produces: the public `/projects/qwen3-reranker/` case study.

- [ ] **Step 1: Run the Reranker contract and verify RED**

Run: `python3 -m unittest tests.test_project_pages.ProjectPageContract.test_reranker_evidence -v`

Expected: FAIL because `projects/qwen3-reranker.md` does not exist.

- [ ] **Step 2: Implement the page**

Write the query-document relevance task, Qwen3-Reranker-0.6B + LoRA SFT method, pointwise yes/no supervision, 1:3 positive-negative construction, current 15,704/1,749 data assets, and separately labelled checkpoint-135 archived evaluation of 85.39% accuracy and 93.12% negative recall on an earlier split.

- [ ] **Step 3: Run the focused test and verify GREEN**

Run: `python3 -m unittest tests.test_project_pages.ProjectPageContract.test_reranker_evidence -v`

Expected: PASS.

- [ ] **Step 4: Commit**

```bash
git add projects/qwen3-reranker.md
git commit -m "feat: add reranker training case study"
```

### Task 6: Homepage integration and end-to-end verification

**Files:**
- Modify: `_data/projects.yml`
- Modify: `_includes/project-entry.html`
- Modify: `tests/test_project_data.py`
- Modify: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: three published project routes.
- Produces: homepage `Read project →` links for projects 01-03 while project 04 stays unlinked.

- [ ] **Step 1: Add failing homepage-link tests**

Require exactly three `url:` fields in project data, a Liquid `relative_url` project link in the component, and the three rendered routes in the site contract.

- [ ] **Step 2: Run tests and verify RED**

Run: `python3 -m unittest tests.test_project_data tests.test_redesign_source -v`

Expected: FAIL because the project URLs are not wired.

- [ ] **Step 3: Wire the three routes**

Add the URLs to projects 01-03 and render one `Read project →` link only when `project.url` exists.

- [ ] **Step 4: Run the full source suite**

Run: `python3 -m unittest discover -s tests -v`

Expected: all source tests PASS; rendered-only tests may explicitly SKIP when `_site` is absent.

- [ ] **Step 5: Build or validate rendered output**

Use the available GitHub Pages build as the authoritative Jekyll build if local Ruby remains incompatible. After push, download each live page and run rendered-site assertions and link checks against all four routes.

- [ ] **Step 6: Validate desktop and mobile layouts**

Use Playwright at 1440px, 390px, and 375px. Confirm `scrollWidth === innerWidth`, project diagrams remain legible, and visible navigation/project links meet the 44px tap-target rule.

- [ ] **Step 7: Commit integration and verification fixes**

```bash
git add _data/projects.yml _includes/project-entry.html tests/test_project_data.py tests/test_site_contract.py _sass/_site.scss
git commit -m "feat: connect evidence pages to portfolio"
```

- [ ] **Step 8: Independent review and publish**

Request a reviewer to compare the full diff against the design spec and evidence boundaries. Fix every Critical or Important finding, rerun the full verification suite, push `main`, confirm GitHub Pages status is `built`, and verify all live routes return HTTP 200.
