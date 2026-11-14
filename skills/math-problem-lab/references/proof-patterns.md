# Standard Proof Patterns

Reference list of opening strategies and proof shapes for `proof-coach` Tier 2 hints. Name the method and structural setup without revealing the punchline.

## General

- **Direct proof:** Assume hypotheses, unpack definitions, and chain implications to the conclusion.
- **Contrapositive:** To prove $P \Rightarrow Q$, prove $\neg Q \Rightarrow \neg P$. Effective when $\neg Q$ provides a concrete object.
- **Contradiction:** Assume the negation of the claim and derive a contradiction. Effective for irrationality, uniqueness, and non-existence.
- **Induction (weak, strong, structural):** Identify $P(n)$, base case, and which earlier cases the inductive step needs.
- **Existence by construction:** Construct the object explicitly, then verify every required property.
- **Uniqueness:** Assume two objects satisfy the property and prove they are equal.
- **Cases / exhaustion:** Split into mutually exhaustive cases.
- **Pigeonhole / counting:** Compare object and box counts, or double-count a finite set.
- **Equivalence ($\iff$):** Prove both directions separately, or form a cycle $(a) \Rightarrow (b) \Rightarrow (c) \Rightarrow (a)$.

## Sets and Maps

- **Double inclusion:** $A = B$: prove $A \subseteq B$ and $B \subseteq A$ via arbitrary elements.
- **Injective / surjective / bijective:** Injective: $f(x) = f(y) \Rightarrow x = y$ (or $\ker f = \{0\}$). Surjective: for arbitrary $y$ in the codomain, produce $x$ in the domain with $f(x) = y$. Bijective: prove both or construct a two-sided inverse.
- **Well-definedness:** For maps on equivalence classes or cosets, prove independence of representative.

## Linear Algebra

- **Subspace test:** Verify non-emptiness ($0 \in W$) and closure under addition and scalar multiplication.
- **Direct sum:** Show $V = W_1 + W_2$ and $W_1 \cap W_2 = \{0\}$.
- **Linear independence:** Assume $\sum c_i v_i = 0$ and force all $c_i = 0$.
- **Basis extension / dimension counting:** Extend a linearly independent set to a basis, then compare dimensions; use Rank-Nullity on finite-dimensional domains.
- **Kernel/image arguments:** Characterize injectivity by $\ker T = \{0\}$ and surjectivity by $\operatorname{Im} T = W$.

## Analysis

- **$\varepsilon$-$\delta$ / $\varepsilon$-$N$:** Fix $\varepsilon > 0$ arbitrary first, then choose $\delta$ or $N$ (scratch work backwards, write forwards).
- **Sequences and subsequences:** Use Bolzano-Weierstrass for sequential compactness; use the Cauchy criterion when the limit is unknown.
- **Triangle inequality trick:** Insert and subtract an intermediate term: $|a - c| \le |a - b| + |b - c|$.
- **Compactness / completeness:** Use finite subcovers, sequential compactness, Extreme Value Theorem, or monotone-bounded convergence.

## Abstract Algebra

- **Subgroup test:** Verify non-emptiness and closure under $ab^{-1}$.
- **Homomorphism arguments:** Verify operation preservation, find the kernel, and apply the First Isomorphism Theorem.
- **Order and Lagrange:** Use divisibility of element and subgroup orders.
- **Quotients:** Verify normality (groups) or ideal absorption (rings) before forming the quotient, then check well-definedness.

## Probability

- **Conditioning:** Partition the sample space and apply the law of total probability.
- **Indicator variables and linearity of expectation:** Decompose counts into indicators to bypass independence.
- **Complement counting:** Compute $1 - P(A^c)$ when the complement has simpler structure.
