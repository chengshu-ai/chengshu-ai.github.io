# Compact Research Hero Design

## Objective

Replace the current oversized editorial hero with a compact research-profile hero inspired by the clarity of Ran Cheng's homepage, while retaining Shu Cheng's existing light palette and evidence-first positioning.

## Visual thesis

A calm research profile cover: the name is the strongest signal, the research direction is readable in seconds, and the portrait acts as a single identity anchor rather than a separate information column.

## Content hierarchy

1. Research domain label: `MEMORY · AGENTS · EMBODIED AI`
2. Name: `Shu Cheng` with `舒橙` as a quieter bilingual identifier
3. Compact topic line: `Agent memory · model post-training · multimodal systems`
4. One research statement connecting current evidence to the embodied-AI direction
5. Four low-noise links: selected work, email, GitHub, CV
6. Portrait with no detached degree, university, or location block

The education and location facts remain available elsewhere on the site and in the CV; they do not compete with the hero's research narrative.

## Layout

- Desktop: a bounded two-column composition, approximately 2:1 text-to-image, vertically centered within the first viewport below the masthead.
- The text column uses a clear maximum width so the statement does not become a long paragraph.
- The portrait is a single 4:5 image with restrained rounding and a subtle border/shadow.
- The hero uses less vertical padding than the current implementation and removes the offset block shadow.
- Mobile: copy first, portrait second; the name remains within two lines and the action links wrap without overflow.

## Typography and color

- Keep the existing white background, dark ink, and one blue accent.
- Use the site's sans-serif face for the name and labels; reserve serif only for the short research statement.
- Use no decorative gradients, pills, stat cards, or additional colors.

## Interaction thesis

- A short, reduced-motion-safe entrance for the label, name, statement, and portrait.
- Underline movement on the hero links to clarify interactivity.
- No scroll effects or continuous animation; the page should feel like an academic profile, not a product campaign.

## Responsive and accessibility requirements

- No horizontal overflow at 1440px, 1024px, 390px, or 375px widths.
- All links retain at least a 44px touch target.
- The portrait keeps descriptive alt text.
- Entrance animation is disabled under `prefers-reduced-motion: reduce`.
- Text contrast continues to meet WCAG AA on the white background.

## Scope boundary

Only the homepage hero structure and its styles change. Selected Work, research questions, experience, project detail pages, data files, and the unrelated pending project tests remain untouched.
