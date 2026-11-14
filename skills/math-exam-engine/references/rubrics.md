# Grading Rubrics

Standard 100-point grading rubrics for `math-grader`. If the user or instructor provides a specific rubric, use that rubric instead.

## Proof Problems

| Criterion | Weight | What it covers |
|---|---|---|
| Logic and structure | 40 | Logical flow, justified transitions, no skipped non-trivial steps, valid proof method |
| Concepts, definitions, hypotheses | 30 | Accurate use of definitions, every hypothesis verified, no conceptual gaps |
| Correct claims and conclusion | 20 | Intermediate claims are true; the argument actually proves the stated theorem |
| Notation and exposition | 10 | Symbols used accurately, distinct object types not confused, clear presentation |

## Computation Problems

| Criterion | Weight | What it covers |
|---|---|---|
| Method and steps | 30 | Valid solution strategy, intermediate steps shown and justified |
| Correct results | 40 | Intermediate and final values (applying error carried forward) |
| Concepts and definitions | 20 | Appropriate theorems and definitions applied, conditions checked |
| Notation and exposition | 10 | Clear, formal mathematical presentation |

## Mixed Problems

| Criterion | Weight |
|---|---|
| Logic, method, and steps | 35 |
| Concepts, definitions, hypotheses | 25 |
| Correct results and claims | 30 |
| Notation and exposition | 10 |

## Partial Credit Guidelines

- **Right idea, incomplete execution:** Award most of the method/logic credit; deduct from completeness/execution.
- **Right answer, no justification:** Award result credit; withhold most method and logic credit.
- **Wrong answer, correct method:** Award method and concept credit; deduct result credit once.
- **Unverified hypothesis** (e.g., applying Rank-Nullity without verifying finite dimensionality, or inverting a matrix without checking $\det A \ne 0$): Deduct from the concepts criterion, typically **3-8 points** depending on whether the conclusion still holds.
- **Circular reasoning or proving the converse:** Deduct heavily from logic and structure.
- **Notation-only issues:** Never deduct more than the 10-point notation weight.

## Error Carried Forward (ECF)

An early arithmetic or sign slip is penalized **once**, in the step where it occurs. Subsequent steps that are logically and computationally valid given that propagated value retain their method and follow-through credit. Result credit is deducted only for the affected final answer, unless the slip trivializes the problem or alters its mathematical nature.

## Severity Scale for Deductions

- **Minor (1-3 pts):** Isolated sign slip, minor notation slip, missing quantifier that is unambiguous from context.
- **Moderate (4-8 pts):** Unverified hypothesis, unjustified non-trivial step, flawed but repairable definition or computation.
- **Major (9+ pts):** Invalid logical structure, proving the converse/wrong claim, missing a primary case, fundamentally wrong method.
