# Compact Research Hero Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the homepage's oversized editorial hero with a compact, responsive research-profile hero that foregrounds Shu Cheng's name, research direction, and portrait without overflow.

**Architecture:** Keep the existing Jekyll page and SCSS architecture. Replace only the hero markup in `index.md` and `_includes/author-profile.html`, then scope the new responsive composition to existing `.hero*` selectors in `_sass/_site.scss`. Add a dedicated source-contract test so unrelated pending project tests remain untouched.

**Tech Stack:** Jekyll, Liquid, SCSS, Python `unittest`, GitHub Pages, Playwright browser verification.

## Global Constraints

- Preserve the existing white, dark-ink, and blue-accent palette.
- Use the exact hero labels `MEMORY · AGENTS · EMBODIED AI`, `Shu Cheng`, and `舒橙`.
- Do not claim completed embodied-AI or robot-learning work.
- Do not modify Selected Work, research questions, experience, project detail pages, or project data.
- Support 1440px, 1024px, 390px, and 375px without horizontal overflow.
- Respect `prefers-reduced-motion: reduce` and retain 44px link targets.

---

### Task 1: Lock the compact hero content contract

**Files:**
- Create: `tests/test_compact_hero.py`
- Modify: `index.md`
- Modify: `_includes/author-profile.html`

**Interfaces:**
- Consumes: existing `site.author.avatar`, `site.author.name`, `site.author.email`, `site.author.github`, and `site.author.cv` values.
- Produces: `.hero-copy`, `.hero-name`, `.hero-topics`, `.hero-statement`, `.hero-links`, `.hero-identity`, and `.hero-portrait` hooks for SCSS.

- [ ] **Step 1: Write the failing source-contract test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CompactHeroContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.md").read_text(encoding="utf-8")
        cls.profile = (ROOT / "_includes/author-profile.html").read_text(encoding="utf-8")
        cls.scss = (ROOT / "_sass/_site.scss").read_text(encoding="utf-8")

    def test_compact_research_hierarchy(self):
        for text in (
            "MEMORY · AGENTS · EMBODIED AI",
            "Shu Cheng",
            "舒橙",
            "Agent memory · model post-training · multimodal systems",
        ):
            self.assertIn(text, self.index)
        self.assertNotIn("Systems that help agents", self.index)
        self.assertNotIn("site.author.title", self.profile)
        self.assertNotIn("site.author.affiliation", self.profile)
        self.assertNotIn("site.author.location", self.profile)

    def test_required_layout_and_accessibility_hooks(self):
        for selector in (
            ".hero-name",
            ".hero-name-local",
            ".hero-topics",
            ".hero-statement",
            ".hero-portrait",
        ):
            self.assertIn(selector, self.scss)
        self.assertIn("prefers-reduced-motion: reduce", self.scss)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python3 -m unittest tests/test_compact_hero.py -v`

Expected: FAIL because the new hierarchy and selectors do not exist.

- [ ] **Step 3: Replace the hero copy and simplify the portrait include**

Use this hero hierarchy in `index.md`:

```html
<p class="eyebrow">MEMORY · AGENTS · EMBODIED AI</p>
<h1 class="hero-name">Shu Cheng <span class="hero-name-local">舒橙</span></h1>
<p class="hero-topics">Agent memory · model post-training · multimodal systems</p>
<p class="hero-statement">I build memory and reasoning systems for long-horizon agents, with the goal of connecting reliable learning systems to embodied intelligence.</p>
```

Keep the four existing links. Reduce `_includes/author-profile.html` to the existing accessible portrait image inside `.hero-identity`, removing `.hero-meta`.

- [ ] **Step 4: Run the focused test and confirm only style hooks remain RED**

Run: `python3 -m unittest tests/test_compact_hero.py -v`

Expected: content assertions PASS and style-hook assertions FAIL.

### Task 2: Implement the responsive composition

**Files:**
- Modify: `_sass/_site.scss`
- Test: `tests/test_compact_hero.py`

**Interfaces:**
- Consumes: the hero hooks created by Task 1.
- Produces: a bounded two-column desktop hero and a single-column mobile hero with reduced-motion-safe entrance animation.

- [ ] **Step 1: Replace the current hero styling**

Implement these exact layout boundaries:

```scss
.hero {
  grid-template-columns: minmax(0, 1fr) minmax(240px, 320px);
  gap: clamp(2.5rem, 6vw, 6rem);
  min-height: min(680px, calc(100svh - 72px));
  padding-block: clamp(3rem, 7vh, 5.5rem);
}

.hero-name {
  max-width: 760px;
  font-family: inherit;
  font-size: clamp(3.6rem, 7vw, 6.6rem);
  font-weight: 720;
  letter-spacing: -0.065em;
  line-height: 0.92;
}

.hero-name-local {
  color: var(--accent);
  font-size: 0.34em;
  font-weight: 650;
  letter-spacing: 0;
  white-space: nowrap;
}

.hero-topics {
  margin-top: 1.35rem;
  color: var(--accent);
  font-size: clamp(0.88rem, 1.4vw, 1.05rem);
  font-weight: 650;
  letter-spacing: 0.02em;
}

.hero-statement {
  max-width: 720px;
  margin-top: 2rem;
  color: var(--ink);
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(1.18rem, 2vw, 1.55rem);
  line-height: 1.55;
}

.hero-identity {
  width: 100%;
  max-width: 320px;
}

.hero-portrait {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  box-shadow: 0 22px 50px rgba(20, 35, 50, 0.12);
}
```

At `max-width: 760px`, set the grid to one column, cap the portrait at 190px, lower the name size to `clamp(3rem, 16vw, 4.4rem)`, and keep the portrait after the link row. Add a short `hero-enter` animation to the copy and portrait; disable it in the existing reduced-motion media query.

- [ ] **Step 2: Run the focused test and full source suite**

Run: `python3 -m unittest tests/test_compact_hero.py tests/test_redesign_source.py -v`

Expected: PASS.

- [ ] **Step 3: Build the Jekyll site and run all contracts**

Run: `bundle exec jekyll build --trace && python3 -m unittest discover -s tests -v`

Expected: build succeeds and the full suite passes. If unrelated pre-existing RED tests fail, record them separately and confirm the new compact-hero test remains green.

- [ ] **Step 4: Validate real browser layouts**

Serve `_site` locally, then use Playwright at 1440×1000, 1024×900, 390×844, and 375×812. At every viewport, assert `document.documentElement.scrollWidth === window.innerWidth`, capture a screenshot, and check the browser console for errors.

Expected: no clipping, no horizontal overflow, name and portrait fully visible, links wrap cleanly, and the hero fits comfortably in the first desktop viewport.

- [ ] **Step 5: Commit and publish the verified hero**

```bash
git add index.md _includes/author-profile.html _sass/_site.scss tests/test_compact_hero.py
git commit -m "style: simplify research profile hero"
git push origin main
```

Expected: GitHub Pages publishes the new hero without staging the unrelated pending project tests or local screenshot artifacts.
