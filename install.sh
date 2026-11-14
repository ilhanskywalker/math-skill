#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-$HOME/.agents/skills}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"

mkdir -p "$TARGET_DIR"

for skill in math-study-core math-problem-lab math-exam-engine; do
  if [ -d "$SKILLS_SRC/$skill" ]; then
    rm -rf "$TARGET_DIR/$skill"
    cp -R "$SKILLS_SRC/$skill" "$TARGET_DIR/$skill"
    echo "[OK] Installed $skill -> $TARGET_DIR/$skill"
  else
    echo "[ERROR] Missing skill directory: $SKILLS_SRC/$skill" >&2
    exit 1
  fi
done

echo "All 3 math skill packages installed successfully."
