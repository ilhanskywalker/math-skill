# Verification Recipes

Mandatory checks before presenting any final answer in `math-solver` (and across all modes under Rigor Rule 3). If a code execution tool is available, run exact symbolic/rational verification; otherwise perform at least two independent checks by hand.

## Linear Algebra

- **Linear systems ($Ax = b$):** Substitute candidate $x$ back into $Ax$ and verify every equation equals $b$. For parametric general solutions, verify both a particular solution ($Ax_p = b$) and that all basis vectors of the homogeneous solution satisfy $Ax_h = 0$.
- **Rank and nullity:** Check $\operatorname{rank}(A) + \operatorname{nullity}(A) = n$ (column count) and verify linear independence and counts of basis vectors for $\operatorname{null}(A)$ and $\operatorname{col}(A)$.
- **Eigenvalues and eigenvectors:**
  - Verify $\sum_{i=1}^n \lambda_i = \operatorname{tr}(A)$ (with algebraic multiplicity) and $\prod_{i=1}^n \lambda_i = \det(A)$.
  - For each eigenvector $v_i$, compute $Av_i$ directly and verify $Av_i = \lambda_i v_i$ with $v_i \neq 0$.
- **Diagonalization ($A = PDP^{-1}$):** Check $AP = PD$ directly (avoids inverting $P$ first) and verify $\det(P) \neq 0$.
- **Orthonormal bases / QR / Orthogonal matrices:** Verify $q_i^T q_j = \delta_{ij}$ (or $\langle q_i, q_j \rangle = \delta_{ij}$) for all pairs, and check $Q^T Q = I$.
- **Determinants:** Cross-check row-reduction determinant (tracking row swaps and scalar multiples) against cofactor expansion along a sparse row or column.

## Calculus and Real Analysis

- **Antiderivatives and indefinite integrals:** Differentiate candidate $F(x)$ and simplify to confirm $F'(x) = f(x)$ on the target domain.
- **Definite integrals:** Check sign, rough magnitude bounds ($m(b-a) \le \int_a^b f(x)\,dx \le M(b-a)$), symmetry on $[-a, a]$, and special parameter values.
- **Limits and asymptotics:** Test behavior along distinct paths (in $\mathbb{R}^n$) or sequences $x_k \to x_0$; cross-check L'Hôpital's rule against Taylor expansion.
- **Series and sequences:** Check $n$-th term divergence ($a_n \to 0$) first; test endpoints $x = c \pm R$ separately for power series; check partial sums $S_1, S_2, S_3$ against closed-form formulas.
- **Uniform vs. pointwise convergence:** Compute $\sup_{x \in E} |f_n(x) - f(x)|$ explicitly and test whether it tends to $0$ as $n \to \infty$.

## Abstract Algebra and Number Theory

- **Subgroups, ideals, and subrings:** Verify non-emptiness ($e \in H$ or $0 \in I$), operation closure, and absorption ($ra, ar \in I$) for ideals.
- **Homomorphisms and isomorphisms:** Verify $\phi(ab) = \phi(a)\phi(b)$ (and $\phi(1) = 1$ for unital rings), compute $\ker\phi$ and $\operatorname{Im}\phi$, and check $|G/\ker\phi| = |\operatorname{Im}\phi|$ via the First Isomorphism Theorem.
- **Quotient structures and well-definedness:** Whenever a map is defined on cosets $[a]$ or equivalence classes, verify $a \sim a' \implies f([a]) = f([a'])$ explicitly.
- **Congruences and Diophantine equations:** Substitute solutions back modulo $m$ and verify coprimality conditions ($\gcd(a, m) = 1$).

## Differential Equations and Probability

- **ODEs and IVPs:** Substitute $y(t)$ and its derivatives directly into the ODE and verify every initial/boundary condition.
- **Probability distributions and expectations:** Check non-negativity, normalization ($\sum p_i = 1$ or $\int_{-\infty}^\infty f(x)\,dx = 1$), and bounds ($0 \le P(A) \le 1$, $\operatorname{Var}(X) \ge 0$).

## Proof Self-Audit Checklist

1. **Hypothesis accounting:** Identify the exact step where each hypothesis is used. Unused hypotheses signal a flaw or overly strong premise.
2. **Quantifier order:** Verify $\forall \varepsilon > 0\,\exists \delta > 0$ dependencies (ensure $\delta$ does not depend on later-quantified variables such as $x$).
3. **Edge-case stress test:** Test the argument on minimal or degenerate objects: $\emptyset$, zero vector/matrix, $n = 0$ or $n = 1$, $\operatorname{char}(F) = 2$, non-abelian groups, and infinite-dimensional spaces.
