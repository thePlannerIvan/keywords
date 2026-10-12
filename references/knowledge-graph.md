# Knowledge Graph

## Root it in a question

The root is the user's current question, not the entire discipline. The first layer below it contains decisions the user must make. Later layers name the concepts that improve those decisions.

```text
question -> decision -> dimension -> concept -> contrast -> example -> command
```

Use a tree when the main relationship is general-to-specific. Add typed edges only when they explain something a tree cannot:

- includes;
- depends on;
- contrasts with;
- responds to;
- is an example of;
- is evidenced by.

Every edge must answer a reader's question. Decorative connections make a graph look intelligent while reducing its teaching value.

## Node roles

- **Decision:** what the user must choose or judge.
- **Dimension:** the variable that changes that decision.
- **Concept:** a named professional idea.
- **Keyword:** a concept strong enough to change an instruction.
- **Example:** an observable artifact, excerpt, image, clip, or diagram.
- **Source:** where the meaning or example can be checked.

The HTML can combine these roles visually, but the Markdown should name them so a model can retrieve them precisely.

## Scale

Stop expanding a branch when new terms no longer change the target decision, command, or observable distinction. A narrow atlas is better than a complete-looking field map that the user cannot navigate.
