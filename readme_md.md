# math-skill

A modular, token-efficient suite of university-level mathematics agent skills covering concept learning, rigorous proof coaching, verified problem solving, Obsidian synthesis, rubric-based grading, mistake tracking, and exam strategy.

## Architecture

| Module | Included Skills | Primary Purpose | Shared References |
| :--- | :--- | :--- | :--- |
| **`math-study-core`** | `lecture-guide`, `intuition-builder`, `obsidian-notes` | Formal lecture walkthroughs, intuition-first concept rebuilds, and Obsidian Markdown note synthesis. | `notation.md`, `pedagogy.md` |
| **`math-problem-lab`** | `problem-solver`, `proof-coach`, `counterexample-lab` | Verified step-by-step solutions, non-spoiler Socratic proof coaching, and minimal counterexample generation. | `verification.md`, `coaching-rules.md` |
| **`math-exam-engine`** | `exam-strategy`, `quiz-maker`, `math-grader`, `mistake-log` | Syllabus-based exam strategy, mock practice quizzes, 100-pt rubric grading, and spaced mistake logs. | `template.md`, `verification.md` |

## Core Guarantees

* **Automatic Language & Terminology Matching:** Matches the user's input language automatically. When writing in Turkish, technical mathematical terms are preserved in English or introduced in parentheses (e.g., *bölüm uzayı (quotient space)*). Obsidian notes default to formal English.
* **Zero Unchecked Claims:** Every computation, counterexample, or reference solution is verified via code execution or an independent second method before output.
* **Strict Hypothesis & Cutoff Discipline:** Never drops hidden conditions (finite dimensionality, $\mathrm{char}(F) \neq 2$, compactness) or uses techniques beyond the stated topic cutoff.
* **Cross-Package State Carry-Over:** Seamlessly inherits active theorems, proof attempts, deductions, and notation when transitioning across modes in the same session.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ilhanskywalker/math-skill.git
cd math-skill
```

### 2. Install modular skills (Recommended)

Run the installation script to install the modular skill packages into your agent environment:

```bash
chmod +x install.sh
./install.sh
```

### 3. Build single-file bundle (Optional)

If your LLM client or agent framework prefers a single consolidated prompt file rather than modular directories:

```bash
python3 build_all_in_one.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.