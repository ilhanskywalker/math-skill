# Classic Counterexamples by Area

Candidate checks for `counterexample-lab`. Always verify every premise of the user's statement; an object below is only a valid counterexample if it satisfies all premises while violating the conclusion.

## Linear Algebra

- **Characteristic $p$:** $\mathbb{Z}/2\mathbb{Z}$ or $\mathbb{Z}/p\mathbb{Z}$ breaks $2x = 0 \Rightarrow x = 0$, $x \ne -x$, $(a+b)^p \ne a^p + b^p$, and "symmetric and skew-symmetric matrices intersect only in $0$".
- **Matrices ($2 \times 2$):**
  - Zero divisors: $AB = 0$ with $A, B \ne 0$, e.g. $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
  - Nilpotent matrices: $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ satisfies $N^2 = 0$, $N \ne 0$, $\operatorname{tr}(N) = 0$.
  - Non-commuting pairs: $AB \ne BA$.
  - Non-diagonalizable matrix: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over any field.
  - No real eigenvalues: $90^\circ$ rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{R}$.
- **Subspaces:** Union of two coordinate axes in $\mathbb{R}^2$ (not closed under addition); three distinct lines through $0$ in $\mathbb{R}^2$ (pairwise intersect in $\{0\}$, sum is not direct).
- **Infinite dimensions:** Shift operators on $F^{\mathbb{N}}$ or $\mathcal{P}(\mathbb{R})$; differentiation $D$ on $\mathcal{P}(\mathbb{R})$ (surjective, not injective); right shift (injective, not surjective). Breaks "$\ker T = \{0\} \iff T$ is surjective".

## Real Analysis

- **Continuity vs. differentiability:** $|x|$ at $x = 0$; Weierstrass function (continuous everywhere, nowhere differentiable).
- **Integrability:** Dirichlet function $\mathbf{1}_{\mathbb{Q}}$ (nowhere continuous; not Riemann integrable on $[0, 1]$).
- **Open / unbounded intervals:** $(0, 1)$ has no maximum and is not compact; $f(x) = 1/x$ on $(0, 1)$ is continuous but unbounded and not uniformly continuous.
- **Pointwise vs. uniform convergence:** $f_n(x) = x^n$ on $[0, 1]$ (pointwise limit discontinuous at $1$); $f_n(x) = x/n$ on $\mathbb{R}$ (uniform on bounded sets only).
- **Exchanging limits and integrals:** $f_n = n \cdot \mathbf{1}_{(0, 1/n)}$ on $[0, 1]$ ($f_n \to 0$ pointwise, yet $\int_0^1 f_n = 1$ for all $n$).
- **Series:** Harmonic series $\sum 1/n$ ($a_n \to 0$ yet diverges); alternating harmonic series $\sum (-1)^{n-1}/n$ (converges conditionally, not absolutely).
- **Positive derivative without local monotonicity:** $f(x) = x + 2x^2 \sin(1/x)$ for $x \ne 0$, $f(0) = 0$ has $f'(0) = 1 > 0$ but is not monotone on any neighborhood of $0$.

## Abstract Algebra

- **Smallest non-abelian group:** $S_3$ (order 6). Non-normal subgroup: $\langle (1\,2) \rangle \subset S_3$.
- **Same order, non-isomorphic:** $\mathbb{Z}/4\mathbb{Z}$ vs. $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ (Klein four-group).
- **Converse of Lagrange's theorem fails:** $A_4$ has order 12 and no subgroup of order 6.
- **Rings:** $\mathbb{Z}/6\mathbb{Z}$ has zero divisors; $\mathbb{Z}/4\mathbb{Z}$ has nilpotents; $2\mathbb{Z}$ is a commutative ring without $1$; $\mathbb{Z}$ is an integral domain that is not a field.
- **Integral domain without unique factorization:** $\mathbb{Z}[\sqrt{-5}]$, where $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$.
- **Fields:** $x^2 + 1$ is irreducible over $\mathbb{R}$ but reducible over $\mathbb{C}$ and over $\mathbb{F}_5$.

## Topology and Metric Spaces

- **Open vs. closed:** $[0, 1)$ is neither open nor closed in $\mathbb{R}$; $\mathbb{Q}$ is neither open nor closed in $\mathbb{R}$.
- **Compactness:** Closed and bounded does not imply compact in infinite-dimensional or non-Euclidean metric spaces (e.g., closed unit ball in $\ell^2$; $\mathbb{R}$ with the discrete metric $d(x, y) = \min(1, |x - y|)$).
- **Connectedness:** $\mathbb{Q}$ is totally disconnected; $\mathbb{R} \setminus \{0\}$ is disconnected.
- **Topologies:** Cofinite topology on an infinite set is compact but not Hausdorff; indiscrete topology on a 2-point set is not $T_0$.
- **Continuity vs. homeomorphism:** A bijective continuous map need not have a continuous inverse, e.g., $f : [0, 2\pi) \to S^1$, $f(t) = e^{it}$.

## Probability and Statistics

- **Independence:** Pairwise independence does not imply mutual independence (two independent fair bits $X, Y$ and $Z = X \oplus Y$).
- **Uncorrelated vs. independent:** $X \sim \mathcal{N}(0, 1)$ and $Y = X^2$ satisfy $\operatorname{Cov}(X, Y) = 0$ but are dependent.
- **Non-existent expectation:** Standard Cauchy distribution has no finite mean.
- **Conditioning pitfalls:** Two-children and Monty Hall problems depend critically on the observation/sampling protocol.

## Discrete Math and Number Theory

- **Euler's prime-generating polynomial:** $n^2 + n + 41$ is prime for $n = 0, \dots, 39$, but at $n = 40$ equals $41^2$.
- **Even prime edge case:** $2$ is the only even prime; statements assuming "odd prime" fail at $p = 2$.
- **Divisibility:** $a \mid bc$ does not imply $a \mid b$ or $a \mid c$ when $a$ is composite (e.g., $6 \mid 2 \cdot 3$).
- **Graphs:** A graph with all even degrees need not be Eulerian if disconnected; bipartite $\iff$ no odd cycle (holds for disconnected graphs too).

## Ordinary Differential Equations

- **Non-uniqueness:** $y' = \sqrt{|y|}$, $y(0) = 0$ has infinitely many solutions ($y \equiv 0$ and $y(t) = t^2/4$ for $t \ge 0$).
- **Finite-time blow-up:** $y' = y^2$, $y(0) = 1$ has smooth right-hand side everywhere yet blows up at $t = 1$ ($y(t) = \frac{1}{1-t}$).
