# Error Taxonomy

Root-cause classification codes for `mistake-log`. Always classify the **underlying cause** ("what check or understanding would have prevented this?"), not the surface symptom.

## Primary Categories

### 1. Conceptual and Knowledge Errors (Typically `gap`)

| Code | Name | Definition and Diagnostic Question |
|---|---|---|
| `CON` | Concept or Definition Misunderstanding | Misstating, misremembering, or misapplying a core definition, theorem, or structural property (e.g., confusing linear independence with spanning, or pointwise with uniform convergence). |
| `HYP` | Unverified or Dropped Hypothesis | Applying a theorem or operation without verifying its required conditions (e.g., Rank-Nullity without finite dimension, dividing by an expression that can vanish, assuming $\operatorname{char}(F) \ne 2$, or omitting compactness/continuity). |

### 2. Proof and Logical Reasoning Errors (`gap` or `slip`)

| Code | Name | Definition and Diagnostic Question |
|---|---|---|
| `PRF` | Proof Structure or Strategy Error | Flawed logical architecture: circular reasoning, proving the converse ($Q \Rightarrow P$ instead of $P \Rightarrow Q$), invalid induction step, or failing to prove both directions of an $\iff$ claim. |
| `QNT` | Quantifier or Scope Error | Reversing quantifier order ($\forall \exists$ vs. $\exists \forall$), letting $\delta$ depend on $x$ in uniform continuity, or treating a fixed existential witness as arbitrary. |
| `INC` | Incomplete Cases or Edge-Case Omission | Missing boundary or degenerate cases that invalidate generality (e.g., $x = 0$, empty set $\emptyset$, $n = 0$, zero divisors, non-diagonalizable matrices, or interval endpoints). |

### 3. Execution and Presentation Errors (Typically `slip`)

| Code | Name | Definition and Diagnostic Question |
|---|---|---|
| `CAL` | Algebraic or Arithmetic Calculation Error | Execution mistake in row reduction, determinant expansion, integration/differentiation, fraction simplification, or algebraic manipulation despite a valid method. |
| `SGN` | Sign or Indexing Error | Dropped minus sign, cofactor sign $(-1)^{i+j}$ mistake, inequality flip error when multiplying by a negative quantity, or off-by-one sequence/matrix indexing. |
| `NOT` | Notation or Type-Mismatch Error | Confusing distinct mathematical objects (scalar vs. vector, element vs. singleton set, function $f$ vs. value $f(x)$, matrix vs. linear operator) or ambiguous symbol reuse. |
| `COP` | Transcription or Problem-Reading Slip | Miscopying a coefficient/exponent from the prompt or intermediate line, or overlooking an explicit constraint stated in the problem. |

## Classification Rules

1. **One primary code per entry:** Pick the single code whose prevention rule directly stops the error at its root. Optionally add one secondary code (e.g., `HYP` primary, `INC` secondary).
2. **Gap vs. Slip distinction:**
   - **`gap`:** The student lacked the concept, theorem condition, or proof technique. Remedy: conceptual rebuild (`math-study-core`), formal review (`math-study-core`), or targeted drills (`math-problem-lab`).
   - **`slip`:** The student knew the concept and method but failed to run a routine check during execution. Remedy: an explicit pre-submission verification habit (`math-problem-lab` `math-solver` checks).
3. **Fallback:** If the evidence is insufficient to classify even after one clarifying question, set `Root cause: unclassified` and note what information is missing.
