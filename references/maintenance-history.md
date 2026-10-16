# Keywords Maintenance History

## 2026-10-12: Initial Skill

- Trigger: user defined a need for fast domain command vocabulary, observable examples, a problem-rooted concept tree, and a dual HTML/grep-friendly output.
- Added: core concepts, six-step workflow, Wayfinder/Research seams, local-first media rule, reusable Viewer contract, and mechanical validation.
- Deliberately excluded: full `domain-modeling` and `wiki-builder` workflows, professional certification claims, and automatic mutation of production Skills.
- Validation: frontmatter, file structure, Viewer build, atlas fixture validation, and a semantic Bento-style forward test.

## 2026-10-12: Viewer Mindmap & Polymorphic Modal Overhaul

- Trigger: user feedback that the initial Viewer was a rigid two-column form with heavy text and static figures, rather than a lightweight, intuitive mindmap with live animations.
- Changes:
  - Replaced the rigid two-column layout in `assets/keywords-viewer.html` with an interactive, zoomable, draggable SVG tree mindmap engine.
  - Aligned with `planners-review-core`: inlined DSH design tokens (`/*__DSH_TOKENS__*/`) and added a bare `{{REVIEW_BRIDGE}}` placeholder to support both standalone browsers and DSH sidebar plugins.
  - Introduced a polymorphic modal drawer: renders live HTML/CSS sandboxes for motion concepts (with replay controls), image galleries for styles, and one-click Prompt copying.
  - Collapsed academic citations and long-form boundaries into a bottom audit drawer.
  - Updated `build_viewer.py` to automatically inline `dsh-tokens.css` during the build step.
- Validation: re-validated `bento-atlas.json` and generated `01-projects/video-motion-keywords-atlas-2026-10/viewer.html`.

## 2026-10-12: Lean Refactoring & DSH Alignment (User Feedback Pass)

- Trigger: user feedback demanding a lean, practical "Leverage Words Atlas / Tool Inventory" without academic jargon, heavy validation barriers, or engineering clutter.
- Changes:
  - Rewrote `SKILL.md` to focus strictly on leverage word definitions, 4-step workflow, best-fit visual contract, and clear handoff format.
  - Relaxed `scripts/validate_atlas.py` from dogmatic schema checking to permissive warning-based validation.
  - Upgraded `assets/keywords-viewer.html` to an Inspector slide-over drawer, eliminated raw `{{REVIEW_BRIDGE}}` leak, removed all emojis/decorative gradients, and solved text truncation with dynamic node width.
  - Completely purged engineering audit logs/drawers from the viewer surface.
- Validation: verified `validate_atlas.py` against existing projects and test fixtures; verified standalone browser and DSH review bridge rendering.

## 2026-10-12: Theory Integration, Wayfinder/Research Seams & Adaptive Visualization

- Trigger: user feedback highlighting four structural enhancements:
  1. Deepen LLM understanding by incorporating foundational theory and motivations for leverage words (Wittgenstein, Simon chunking, LLM latent space steering vectors, domain micro-ontology).
  2. Formally embed `wayfinder` and `research` as core collaboration tools.
  3. Replace rigid visual presentation tables with illustrative examples judged adaptively by the model.
  4. Purge frontend UI implementation details from SKILL.md, treating the viewer pipeline as default tooling.
- Changes:
  - Re-anchored `SKILL.md` around the 4 interdisciplinary pillars and the prompt formula: Anchor + Slots.
  - Articulated the complementary roles of `/wayfinder` (navigating domain fog) and `/research` (grounding factual evidence).
  - Framed visualization around intuitive understanding with polymorphic examples (UI sandboxes, screenshots, vector graphs, token cards).
  - Pruned redundant DSH design token and drawer specs from the instructions.

## 2026-10-12: Reviewer Observation Path & Host Seam Repair

- Trigger: the pilot Atlas exposed that a concept could exist in the tree without giving a person a reliable path from seeing it to understanding and invoking it. The first Reviewer also left the review marker visible in standalone output and made node switching unnecessarily redraw the SVG tree.
- Changes:
  - Reordered the Inspector around the leverage test: live example, observable cues, why it matters, distinction, and copy-ready command.
  - Added independent replayable HTML/CSS demos for every motion and video-recipe keyword in the pilot vocabulary, with explicit fallback states for static or missing media.
  - Added role/position metadata, keyboard activation, focus states, reduced-motion behavior, mobile Inspector sizing, and local/DSH review status reporting.
  - Kept `{{REVIEW_BRIDGE}}` as the single bare review-core seam and made `build_viewer.py` reject malformed or duplicated markers; standalone bootstrap removes the untouched marker before first paint.
  - Updated node selection to change active state in place rather than rebuilding the entire mindmap during Inspector navigation.
- Validation: atlas validation, generated Viewer build, JavaScript parse check, browser regression across all 20 keyword nodes, keyboard activation, collapse behavior, and 390px viewport checks.

## 2026-10-12: Canvas Navigation & Tree Keyboard Control

- Trigger: dragging the mindmap selected page text, trackpad two-finger navigation felt like browser scrolling, and selecting a node did not provide a keyboard path through the tree.
- Changes:
  - Added `user-select: none`, pointer capture, and pointer events so canvas dragging pans without selecting labels.
  - Mapped non-pinched wheel deltas to horizontal/vertical canvas panning and `ctrlKey` pinch deltas to cursor-centered zooming.
  - Added tree-aware arrow navigation: left/right moves to parent/first child, up/down moves between same-level siblings; focus and Inspector follow the selected node.
  - Added accessible selected-state updates and branch/root Inspector states so keyboard navigation remains legible at every tree level.
- Validation: JavaScript parse, atlas validation, browser keyboard navigation for child/sibling/parent movement, standalone marker check, and responsive Viewer regression.

## 2026-10-12: Complete Data Contract, Mandatory Discovery Gates & Adaptive Base Viewport

- Trigger: user feedback identifying 3 key gaps:
  1. Missing explicit field-by-field schema specification for `atlas.json` data handoff;
  2. Need for mandatory enforcement of `/wayfinder` and `/research` as non-negotiable prerequisite steps;
  3. Visual stage in the viewer: resolved debate between rigid fixed sizing vs unconstrained adaptiveness by establishing the "360px Base Viewport + Ratio-driven Adaptiveness" contract.
- Changes:
  - Documented complete `atlas.json` schema in `SKILL.md` (root, branches, nodes, kind enumeration, cues, distinctions, prompt, examples, sources).
  - Enforced `/wayfinder` and `/research` as mandatory gates in both workflow principles and step sequences.
  - Formally upgraded the visual presentation contract in `SKILL.md` and `presentation.md`: anchored to a 360px base width micro-viewport, with aspect ratio adaptation (16:9 for motion/comparison, 1:1 for architecture/grids, 9:16 for mobile/flows) and height naturally expanding up to ~380px max height.
- Validation: validated test fixtures, updated viewer template CSS, and synced all runtimes via `publish_skills.py`.

## 2026-10-12: Cross-Level Vertical Keyboard Navigation

- Trigger: user feedback that `ArrowDown` should continue through any node visibly below the current selection, instead of stopping at same-level siblings.
- Changes:
  - Kept left/right as hierarchy navigation: parent and first child.
  - Changed up/down to choose the nearest node above or below on the rendered canvas, allowing movement across branches and depth levels.
  - Preserved focus, active-node styling, highlighted links, and Inspector synchronization.
- Validation: rebuilt the pilot Viewer and re-ran atlas validation plus browser keyboard navigation checks.

## 2026-10-12: Dynamic Column Mindmap Layout, Flexbox Anti-Crush & Multi-Path DSH Token Resolution

- Trigger: user report showing mindmap label collision/overlap across levels, Inspector stage bottom-clipping on SVG cards, and unstyled appearance due to missing DSH tokens.
- Changes:
  - Replaced hardcoded column X positions in `keywords-viewer.html` (`layoutTree`) with a 2-pass dynamic layout: recursively measures max label width per depth level and computes non-overlapping column offsets with a fixed 54px breathing gap.
  - Added `.stage-section { flex-shrink: 0; }` preventing Flexbox column containers from collapsing `overflow: hidden` stage elements down to 94px in constrained viewports.
  - Upgraded `resetView()` to auto-fit using content bounding box and automatically invoked it on `DOMContentLoaded`.
  - Expanded `build_viewer.py` DSH token candidate search paths to cover monorepo source tree, installed runtime sibling directories (`~/.claude/skills`, `~/.codex/skills`, `~/.gemini/config/skills`), and workspace root; upgraded missing token behavior to throw an explicit error rather than silently degrading to unstyled text.
- Validation: Playwright headless browser rendering tests confirming 100% complete micro-cards, zero node collision, smooth S-curve bezier connections, and authentic DSH design tokens inlined.

## 2026-10-12: Same-Depth Vertical Navigation Across Branches & Hierarchical Horizontal Traversal

- Trigger: user feedback that spatial vertical navigation was chaotic; requested that Up/Down strictly move across nodes at the exact same depth level (allowing cross-branch jumps), while Left/Right strictly traverses hierarchy levels.
- Changes:
  - Replaced arbitrary spatial Y navigation with `getNodesAtDepth(node.depth)`, collecting all nodes at the same tree depth across the atlas and sorting by vertical Y order.
  - Up/Down keys strictly cycle within this same-depth list, smoothly leaping across branches without shifting depth.
  - Left key ascends to parent node (`depth - 1`); Right key descends to the vertically closest child node (`depth + 1`).
  - Implemented `ensureNodeVisible(target)` auto-panning so nodes remain comfortably in view during keyboard traversal.
  - Added global window keydown listener so arrow navigation works immediately without requiring manual focus on a node pill.
- Validation: validated JS syntax with Node, rebuilt viewers for `ppt-layout` and `video-motion`, and verified multi-runtime sync.

## 2026-10-16: Open-Source Packaging & Self-Contained Token Mirror

- Trigger: the public repo had no LICENSE/NOTICE/TRADEMARK/COMMERCIAL, and a standalone clone could not build a viewer at all — `build_viewer.py` hard-errored when `planners-review-core/assets/dsh-tokens.css` was unreachable (267 `var(--dsw-*)` references in the template make a token-less page visibly broken, so silent degradation was not an option).
- Changes:
  - Added `LICENSE` (AGPL-3.0), `NOTICE`, `TRADEMARK.md`, `COMMERCIAL.md`, `.gitignore`, `THIRD_PARTY_NOTICES.md`, a provenance block in `SKILL.md`, and README sections for install/attribution.
  - Vendored a byte-identical mirror of the token sheet at `assets/dsh-tokens.css` (+ `assets/dsh-tokens.LICENSE.txt`, MIT, DeepSeek), deliberately making this Skill the one documented exception to review-core's "no second copy" rule.
  - `build_viewer.py` now prefers the mirror, falls back to the canonical copies, prints which sheet it used, and warns on stderr when mirror and canonical have drifted apart. Missing-token error text and `references/presentation.md` updated to match.
- Validation: standalone simulation (`HOME` outside the runtimes, skill copied to `/tmp`) builds successfully and inlines the mirror; drift warning verified with a mutated mirror; monorepo build resolves the mirror; fixture validation unchanged.

