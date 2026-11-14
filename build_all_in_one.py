#!/usr/bin/env python3
"""Bundle the 3 modular math skills and their references into a single prompt file."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
OUTPUT_FILE = DIST / "ALL_IN_ONE_PROMPT.md"

SKILLS = [
    "math-study-core",
    "math-problem-lab",
    "math-exam-engine",
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def build() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    sections = [
        "# University Mathematics Study Collaborator (All-in-One Bundle)\n",
        "Auto-generated from modular `skills/*` packages.\n",
    ]

    seen_refs: set[str] = set()

    for skill_name in SKILLS:
        skill_dir = ROOT / "skills" / skill_name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            raise FileNotFoundError(f"Missing {skill_md}")

        sections.append(f"\n---\n\n# Package: `{skill_name}`\n")
        sections.append(strip_frontmatter(skill_md.read_text(encoding="utf-8")))

        refs_dir = skill_dir / "references"
        if refs_dir.exists():
            for ref_file in sorted(refs_dir.glob("*.md")):
                if ref_file.name in seen_refs:
                    continue
                seen_refs.add(ref_file.name)
                sections.append(f"\n## Reference: `{ref_file.name}`\n")
                sections.append(ref_file.read_text(encoding="utf-8").strip())

    OUTPUT_FILE.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT_FILE} ({OUTPUT_FILE.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()
