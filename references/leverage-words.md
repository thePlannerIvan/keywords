# Leverage Words

## The test

A leverage word is a compact handle for a domain model. It is useful only when it changes what the user can notice, decide, or ask the model to do.

For every candidate, answer:

1. What does the word name?
2. What problem or decision does it help with?
3. What can a person observe in a real artifact?
4. Which nearby word is most likely to be confused with it?
5. What is a good example, and what is a boundary example?
6. How does it change an AI instruction?
7. What evidence supports the definition, and what remains disputed?

## Promotion ladder

```text
candidate term
  -> sourced concept
    -> observable distinction
      -> command translation
        -> unseen-case transfer
          -> promoted leverage word
```

Do not promote a word because it is fashionable, difficult, or present in a source. Keep it as supporting vocabulary when it names something real but does not yet help the user make a decision.

## Good command translation

Prefer:

```text
Use [term] to achieve [decision/outcome], showing [observable cues], while avoiding [nearest boundary].
```

This is a teaching scaffold, not a rigid prompt template. The term must still be adapted to the user's medium, audience, and constraints.

## Failure patterns

- **Label without evidence:** the user can repeat the name but cannot recognize it.
- **Evidence without a name:** the user sees a pattern but cannot reuse it in an instruction.
- **Name without contrast:** neighboring concepts collapse into one vague style word.
- **Command without boundary:** the model applies the term everywhere, including cases where it conflicts with the goal.
- **Popularity as leverage:** a fashionable term is treated as useful even when it does not change a decision.
