# Mistake Log Template

Portable Markdown format for `mistake-log`. Keep entries concise (at most 8 lines per entry) with stable sequential IDs (`E-001`, `E-002`, ...).

## Empty Log Starter

```markdown
---
course: <Course Code, e.g. MATH 213>
tags:
  - math
  - mistake-log
---

# Mistake Log

## Active & Practicing Entries

<!-- Paste new entries below -->

## Fixed Entries

<!-- Move entries here after 3 consecutive successful re-attempts -->
```

## Entry Schema

```markdown
### E-001 | <Topic>
- **Meta:** Date: YYYY-MM-DD | Root cause: `<CODE>` (`gap` / `slip`) | Severity: `minor` / `moderate` / `major` | Status: `open` | Recurrence: 1 | Next review: YYYY-MM-DD
- **What happened:** <Factual 1-2 line summary of the exact mistake.>
- **Correct idea:** <1-line mathematical correction.>
- **Rule for next time:** <1-sentence concrete check to run before moving on.>
- **Tags:** `#<topic-slug>` `#<code-lowercase>`
```

## Example Entries

```markdown
### E-001 | Linear Transformations & Rank-Nullity
- **Meta:** Date: 2026-11-10 | Root cause: `HYP` (`gap`) | Severity: `moderate` | Status: `open` | Recurrence: 1 | Next review: 2026-11-11
- **What happened:** Applied Rank-Nullity ($\dim V = \dim \ker T + \dim \operatorname{Im} T$) to the differentiation operator on $\mathcal{P}(\mathbb{R})$ to argue injectivity implies surjectivity.
- **Correct idea:** Rank-Nullity and the equivalence of injectivity/surjectivity for endomorphisms require $\dim V < \infty$.
- **Rule for next time:** Before applying Rank-Nullity or $\ker T = \{0\} \iff T \text{ onto}$, explicitly verify and state that the domain is finite-dimensional.
- **Tags:** `#linear-algebra` `#hyp`

### E-002 | Cofactor Determinant Expansion
- **Meta:** Date: 2026-11-12 | Root cause: `SGN` (`slip`) | Severity: `minor` | Status: `practicing` | Recurrence: 2 | Next review: 2026-11-15
- **What happened:** Omitted the $(-1)^{1+2}$ sign factor on the $(1,2)$ minor during cofactor expansion of a $3 \times 3$ matrix.
- **Correct idea:** Entry $(i,j)$ carries checkerboard sign $(-1)^{i+j}$, so $(1,2)$ has a minus sign.
- **Rule for next time:** Write the $+ / - / +$ checkerboard signs above the expansion row/column before computing any $2 \times 2$ minors.
- **Tags:** `#determinants` `#sgn`
```
