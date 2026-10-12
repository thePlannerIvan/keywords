# Keywords Architecture

## Purpose and panorama

`keywords` turns a real AI-assisted domain question into a small, evidence-backed vocabulary system. It maps the question, gathers sources and observable examples, promotes useful terms into leverage words, writes a Markdown Wiki, and feeds a reusable HTML Viewer.

## Modules

| Module | Unique owner | Interface | Does not do |
|---|---|---|---|
| Question scope | `SKILL.md` | user problem -> target decisions and boundaries | does not define the whole field |
| Wayfinder seam | `SKILL.md` plus local tracker | open design fog -> concrete research questions | does not store source evidence |
| Research seam | Research Skill | research question -> sources, provenance, failures, media | does not decide the final keyword taxonomy |
| Leverage test | `references/leverage-words.md` | candidate term -> observable, contrastive, command-ready term | does not promote by popularity |
| Atlas source | generated domain Markdown | question -> tree, concepts, examples, commands | does not hide content only in HTML |
| Viewer tool | `assets/keywords-viewer.html` + scripts | atlas data -> local HTML page | does not author semantic content |
| Validation | `scripts/validate_atlas.py` | atlas data -> mechanical errors/warnings | does not prove teaching quality |

## Seams

- Wayfinder hands over the next sharp question; Research hands back source material and provenance.
- Research hands over evidence and media; the leverage test turns them into terms and contrasts.
- Markdown remains the authoring truth; `atlas.json` is generated input for the Viewer.
- The Viewer returns a human-readable interface; the Markdown Wiki remains the model-readable interface.
- A production Skill may consume a compact Wiki pointer, but `keywords` does not take over production.

## Two truths that must stay separate

1. **Research pack vs atlas:** the research pack records what was found and how it can be checked; the atlas organizes only the concepts needed for the question.
2. **Markdown vs HTML:** Markdown/data is editable source; HTML is generated presentation. Never hand-edit the semantic content in the generated page.

## Retirement rule

If a new file, field, or script has no consumer in the research seam, atlas source, Viewer, or validator, remove it. Do not import the full architecture of `wiki-builder` or `domain-modeling` merely because it exists.
