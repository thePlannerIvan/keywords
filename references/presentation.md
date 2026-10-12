# Presentation

## Match the medium to the concept

Use the least elaborate representation that makes the intended difference obvious:

| Need | Preferred view |
|---|---|
| See the whole and current position | problem-rooted tree with detail panel |
| Compare neighboring terms | paired examples with the decisive difference marked |
| Understand image style | real local image, crop, caption, and source |
| Understand motion | local clip, frame strip, or scrub-able timeline |
| Understand invisible structure | annotated diagram or before/after overlay |
| Understand instruction leverage | plain sentence, professional command, observable effect |

## Viewer requirements

- The atlas renders as an interactive, zoomable, draggable mindmap tree powered by SVG/D3 layout.
- The UI follows DSH design tokens (`/*__DSH_TOKENS__*/` inlined from `planners-review-core`) and supports both dark and light modes.
- The template maintains a bare `{{REVIEW_BRIDGE}}` placeholder to run both in the DSH sidebar iframe and in standalone browsers.
- Clicking a node opens an inspection slide-over drawer:
  - Motion concepts render a live HTML/CSS sandbox with a replay controller;
  - Style/image concepts render high-fidelity galleries/images;
  - Diagrams render vector overlays;
  - Every concept features an actionable one-click Prompt box.
- The interface strictly follows DSH technical minimalism: no unnecessary engineering logs or audit dumps in the primary view.
- The page works with keyboard navigation and responsive layout.
- The page remains useful if a media file is missing.

The Viewer is a shared tool. Keep its layout robust and feed new atlas data into it.
