---
name: keywords
description: Build a problem-rooted keyword atlas for AI-assisted work in an unfamiliar domain. Use when the user needs to learn the vocabulary that changes AI instructions, asks for a concept map or domain keyword Wiki, or needs concrete examples before using a professional term. Repeat Wayfinder-style decision mapping and Research until the target question has enough evidence, observable examples, leverage words, and command translations. Produce a reusable local-first HTML atlas plus a grep-friendly Markdown Wiki; do not promise full professional mastery.
---

# Keywords

## Purpose

`keywords` solves a language problem before it becomes a prompting problem:

> When a person does not know the concepts of a field, they cannot describe the quality they want. The model fills the missing structure with defaults, so people get very different results from the same tool.

The goal is not to make the user memorize jargon or become a certified professional. The goal is to let the user quickly recognize the useful concepts in a field and invoke them in AI instructions.

This Skill has two equal outputs:

- **Human view:** a designed, local-first HTML atlas with a problem-rooted tree, concrete examples, comparisons, and command translations.
- **Model view:** a grep-friendly Markdown Wiki containing the same concepts, evidence, examples, boundaries, and instructions.

Markdown is the editable source. HTML is a reusable viewing tool, not a second source of truth.

## Core ideas

### Leverage words

A leverage word is not merely a popular or technical term. It is a word that compresses a stable bundle of domain constraints and changes the direction of an AI output.

A word earns leverage when a person can:

1. recognize it in a real example;
2. distinguish it from a nearby concept;
3. explain what decision it helps make;
4. put it into an instruction;
5. check whether the resulting work moved in the intended direction.

Never promote a term from a definition alone. Give it observable cues, a positive example, a boundary or counterexample, a neighboring distinction, and a command translation. A word people cannot recognize is only a label; a word they can recognize but cannot invoke is only a reference.

### Knowledge graph

The atlas is not an encyclopedia and not a random network of terms. It starts from the user's real question and expands only as far as that question requires:

```text
question
  -> decisions to make
    -> judgment dimensions
      -> concepts and schools
        -> types, contrasts, and boundaries
          -> observable examples
            -> command translations
```

The graph may be broad for "how do I do web design?" and narrow for "how do I make a video motion effect feel heavy?". Scope follows the question, not the size of the field.

### Observability and presentation

The purpose of observability is fast recognition: a person should be able to see, hear, compare, or otherwise understand what a concept means before being asked to use its name.

Choose the representation that exposes the relevant difference:

- hierarchy for general-to-specific structure;
- comparison for neighboring concepts and schools;
- real images for visual styles;
- playable local clips or frame strips for motion and video style;
- annotated diagrams for invisible structure;
- before/after command translations for instruction leverage.

An attractive HTML page that does not make the concept easier to recognize has failed. Do not decorate a glossary; make the evidence and the relation visible.

## Workflow

### 1. Define the question and destination

Turn the user's broad request into one working question. Separate:

- the work they want AI to help with;
- the decisions they currently cannot make;
- the vocabulary they need now;
- what is deliberately outside this atlas.

Do not start with "all of design" or "everything about video". Name the next useful judgment.

**Done when:** the question, target decisions, provisional scope, and transfer situation are explicit.

### 2. Map the fog

For a broad or branching topic, call `$wayfinder` to create or update a decision map, turn sharp unknowns into tickets, and keep unresolved fog separate from settled decisions. The map answers what must be decided about the research route; it is not the final concept graph. If the host does not allow nested invocation of the user-invoked Wayfinder Skill, follow its local Markdown tracker protocol directly and keep the same map/ticket shape.

Use the local Markdown tracker when the repository has no external tracker. Do not wait for a perfect map before the first useful research pass.

**Done when:** the research frontier is visible and the next question is concrete enough to investigate.

### 3. Research the field around the question

Call `$research` for source discovery, preservation, provenance, and failure records. Research enough to cover:

- foundational definitions and real usage;
- important types, schools, or competing explanations;
- concrete positive, contrast, boundary, and failure examples;
- media that makes the concept observable;
- unresolved disagreements and missing evidence.

Repeat the Wayfinder and Research loop when new evidence changes the map. Stop when the next research pass is no longer changing the decisions, concept branches, or examples needed for the user's question. Do not research the whole field for its own sake.

**Done when:** every important branch has a source or an explicit evidence gap, and the atlas can teach recognition rather than only recite definitions.

### 4. Extract and test leverage words

For each candidate term, record:

- plain-language meaning;
- the decision it helps make;
- observable cues;
- nearby concepts it is often confused with;
- positive example and boundary example;
- an instruction that uses the term precisely;
- source and uncertainty.

Promote a candidate only after it survives a small transfer check on an unseen example. If a term cannot change a decision or instruction, leave it as supporting vocabulary rather than a headline keyword.

**Done when:** the important terms are usable handles, not a list of names.

### 5. Compile the atlas

Write the editable Markdown Wiki first. Organize it around the question-rooted tree, then generate the reusable HTML Viewer from the atlas data. Keep local media beside the atlas whenever possible; retain source links and state clearly when an asset could not be saved or verified.

The first viewport must show the question, the whole tree, and the user's current position. Selecting a node must reveal its meaning, why it matters, observable evidence, distinctions, and command translation without losing the map.

**Done when:** a first-time reader can locate the relevant branch, understand at least one concept from its example, and find its instruction form; the same information is grep-able in Markdown.

### 6. Calibrate and package

Ask the user to apply the atlas once to a new case or write a command for a real task. Correct the concept boundary, not just the wording. Then package the atlas for continued use and hand production back to the relevant execution Skill.

Do not call the user an expert because they can repeat definitions. Completion means the user can recognize and invoke the vocabulary needed for the current question, with remaining limits visible.

**Done when:** one transfer has occurred, the evidence and media are traceable, the HTML and Markdown agree, and the next unresolved branch is explicit.

## Seams and tools

| Seam | Upstream gives | `keywords` consumes or returns |
|---|---|---|
| Wayfinder -> research route | destination, decisions, open tickets, dependencies | a concrete research question and an updated frontier |
| Research -> atlas | sources, preserved materials, provenance, failures, derived media | concept evidence, examples, uncertainty, and local asset paths |
| Atlas source -> Viewer | question-rooted Markdown/data and local media | one generated HTML page; no hand-edited semantic content |
| Atlas -> execution Skill | tested terms, distinctions, examples, command translations | a compact context pointer or Wiki path; production remains elsewhere |

Use `scripts/build_viewer.py` to inject atlas JSON into the reusable Viewer. Use `scripts/validate_atlas.py` before opening or publishing the page. The scripts check mechanical integrity; they cannot prove that a term is genuinely useful or that a visual example teaches the intended distinction.

## Output shape

Each completed atlas should contain, at minimum:

```text
<atlas>/
├── index.md              # question-rooted map and retrieval entry point
├── concepts/             # one Markdown page per important concept/keyword
├── sources.md             # provenance, uncertainty, and failures
├── media/                # local-first images, clips, frame strips, diagrams
├── atlas.json             # generated Viewer input, not the authoring truth
└── viewer.html            # generated from the reusable shell
```

The exact folder can vary, but the two views must remain aligned: a term visible in HTML must be findable by name in Markdown, and a promoted leverage word must have an observable example or an explicit missing-media note.

## Boundaries

- Do not build a complete professional curriculum.
- Do not turn a word list into a knowledge graph by adding arbitrary links.
- Do not treat a polished viewer as evidence that the concepts are correct.
- Do not use a term only because it sounds sophisticated.
- Do not replace original sources with model summaries.
- Do not silently make a disputed interpretation look like consensus.
- Do not mutate a production Skill from one unverified candidate term.

## Validation

Run the mechanical checks:

```bash
python3 scripts/validate_atlas.py <atlas.json>
python3 scripts/build_viewer.py <atlas.json> --output <viewer.html>
```

Then perform the semantic checks:

- Can a first-time reader explain what a selected concept looks or sounds like?
- Can they distinguish it from its nearest neighbor?
- Can they use it in a real instruction?
- Does the page show the relation that matters, rather than only the label?
- Do local media, source links, and uncertainty states remain honest?
- Does a new case expose a missing branch or a false distinction?

## Run-time improvement

Keep one-off discoveries in the atlas. Add a candidate to `GOTCHAS.md` only when the same failure is observed again or causes costly rework. Promote an accepted change into the relevant section of this Skill or its references, remove the superseded rule, and record the change in `references/maintenance-history.md`.
