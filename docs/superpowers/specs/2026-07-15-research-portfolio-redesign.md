# Shu Cheng Research Portfolio Redesign

Date: 2026-07-15
Status: Approved design direction

## 1. Objective

Redesign the existing GitHub Pages homepage as a restrained research portfolio for embodied-intelligence and Agent internships.

The page should answer three questions within the first viewport:

1. Who is Shu Cheng?
2. What research problem does he care about?
3. Which completed work supports that direction?

The core narrative is:

> I build memory and reasoning systems for agents, then connect them to grounded perception and embodied decision-making.

The homepage must present a credible transition from current Agent Memory, model post-training, retrieval, and multimodal work toward embodied intelligence. It must not imply that unfinished VLA or robotics projects are completed.

## 2. Chosen direction

Use a hybrid of:

- the restraint of a classic academic homepage;
- the narrative structure of a research portfolio.

The approved visual direction is the “Research Project Portfolio” mockup. It replaces the current sticky-profile-plus-document layout with a stronger research thesis and illustrated, evidence-oriented project entries.

### Visual thesis

A quiet editorial research page: white paper, charcoal text, one muted academic blue, serif display typography, restrained diagrams, generous spacing, and no generic card grid.

### Interaction thesis

- The navigation remains calm and sticky enough for orientation.
- Links use subtle underline and color transitions.
- Project diagrams may respond with a small hover shift; there are no scroll spectacles or decorative animations.
- `prefers-reduced-motion` disables nonessential transitions.

## 3. Information architecture

The single-page order is:

1. Navigation
2. Research hero
3. Selected Work
4. Research Questions
5. Experience and Current Focus
6. Footer

Education and contact information appear in the identity area instead of being repeated in multiple sections.

### Navigation

- Shu Cheng
- About
- Selected Work
- Research
- Experience
- CV

On mobile, navigation keeps only the identity, Work, and CV links visible. Secondary links may be omitted rather than forced into horizontal scrolling.

### Research hero

The hero contains:

- research-domain line: `Memory × Reasoning × Embodied AI`;
- primary statement: `Systems that help agents remember, reason, and act.`;
- one short supporting sentence connecting long-horizon memory and post-training to grounded perception and decision-making;
- portrait;
- name, degree, university, and Shanghai location;
- Email, GitHub, CV, and Selected Work links.

The portrait is supporting evidence of identity, not the dominant object. The research thesis must remain the strongest element.

### Selected Work

Show four projects in this order:

1. Dual-Time Agent Memory
2. State-Driven AI Calling Agent
3. Qwen3 Reranker Fine-tuning
4. Multimodal Structured Perception

Each project entry contains:

- sequence number;
- restrained project-specific diagram;
- domain label;
- title;
- one research or engineering question;
- two evidence-based contribution bullets;
- artifact links only when a real repository, report, demo, or technical note exists.

The four diagrams use one visual grammar—lines, nodes, states, ranked bars, and structured panes—rather than unrelated stock images. They communicate the kind of system without fabricating experimental evidence.

Dual-Time Agent Memory is the lead project. The other projects establish supporting capability in controllable Agent systems, model adaptation, and multimodal grounding.

### Research Questions

Use three questions to show the progression toward embodied intelligence:

- What should an agent retain after the current interaction ends?
- How can decisions remain grounded, adaptive, and inspectable?
- How should multimodal evidence become reusable experience?

These are positioning statements, not claims of completed results.

### Experience and Current Focus

Experience keeps only:

- Nuanwa Technology — AI Algorithm Engineering Intern;
- Uceng Intelligence — Python Systems R&D Intern.

Each role is compressed into one high-information contribution sentence and uses the same terminology as the relevant projects. The removed Fanhan internship must not reappear on the homepage.

The Current Focus paragraph explains the next research step toward agents that operate across long horizons and embodied settings. It must clearly distinguish current work from future direction.

### Workflow

Do not add a technology wall. Mention Codex, Claude Code, and Cursor once in the footer as research and engineering harnesses.

## 4. Content constraints

- English-first and factual.
- Problems and decisions precede framework names.
- No unsupported accuracy, latency, SOTA, publication, production-impact, or scale claims.
- No unfinished ManiSkill, LeRobot, OpenVLA, Isaac, or Memory-enhanced VLA work presented as completed.
- No `Code coming soon` links. A missing artifact link is omitted.
- No duplicated degree or school information.
- No “expected” after the education date.
- No Fanhan internship on the homepage.
- The bundled CV remains unchanged unless separately requested.

## 5. Component architecture

Keep the existing Jekyll/GitHub Pages architecture and introduce focused components:

- `_layouts/default.html`: page shell, navigation, and section order;
- `_includes/author-profile.html`: hero identity and contact links;
- `_includes/project-entry.html`: semantic project entry with diagram variant, question, contributions, and optional verified links;
- `_data/projects.yml`: content source for the four project entries;
- `_sass/_site.scss`: typography, hero, project layout, diagrams, mobile behavior, and accessibility states;
- `index.md`: concise introductory, research-question, experience, and focus content;
- `assets/images/profile/shu-cheng.png`: unchanged source portrait;
- `assets/files/Shu_Cheng_Resume.pdf`: unchanged CV.

Project content flows from `_data/projects.yml` into the project include, which renders semantic HTML. CSS selects an explicit diagram variant for each entry. No client-side framework or runtime data request is needed.

## 6. Responsive behavior

### Desktop

- Maximum content width around 1180–1240 px.
- Two-column hero with thesis dominant and portrait secondary.
- Project rows use number, diagram, and copy columns.
- Research questions appear in three columns.

### Mobile

- Tested at 390 px and 375 px.
- Identity uses a compact portrait plus metadata block.
- The research thesis appears within the first viewport.
- Project number, diagram, and copy stack without horizontal overflow.
- Research questions and lower sections become one column.
- Tap targets are at least 44 px where practical.

## 7. Accessibility and failure handling

- Semantic headings follow a single hierarchy.
- Portrait has meaningful alternative text.
- Decorative diagrams are hidden from assistive technology; their meaning is repeated in project copy.
- Keyboard focus is visible on every link.
- Body and link colors meet WCAG AA contrast.
- The page remains understandable without JavaScript.
- Missing optional project links render nothing rather than an empty placeholder.
- A missing project diagram falls back to the text entry without breaking layout.
- Long text and URLs wrap instead of causing horizontal scrolling.

## 8. Verification

Before publication:

1. Add contract tests for project data, content constraints, optional links, and the Fanhan exclusion.
2. Build or render the Jekyll site locally using a compatible runtime; if unavailable, document the limitation and rely on GitHub Pages build evidence.
3. Capture and inspect real 1440 px and 390 px browser screenshots.
4. Confirm all four project entries have distinct but coherent diagrams and readable copy.
5. Confirm the portrait, CV, email, GitHub, internal navigation, and optional artifact links resolve.
6. Scan source and rendered output for copied Hao Shi biography/assets and unsupported claims.
7. Run automated tests and `git diff --check`.
8. Push to `main`, wait for GitHub Pages status `built`, and verify the public URL returns HTTP 200.
9. Inspect the live homepage at desktop and mobile widths after deployment.

## 9. Out of scope

- Separate project-detail pages in this iteration.
- Publications, honors, blog, dark mode, bilingual toggle, analytics, or contact backend.
- New project metrics or claims that cannot be verified from source artifacts.
- Editing the résumé PDF.

## 10. Acceptance criteria

- The first viewport communicates identity, embodied-agent direction, and the memory/reasoning bridge.
- Selected Work is visually distinct from body prose and no longer renders as bare numbered text.
- Dual-Time Agent Memory reads as the lead research project.
- Nuanwa and Uceng are the only homepage experience entries.
- Desktop and mobile screenshots show no clipped text or horizontal overflow.
- Public GitHub Pages build succeeds and serves the redesigned page.
