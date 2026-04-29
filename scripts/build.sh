#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

mkdir -p dist

PAPER_MD="dist/mcp-research-paper.md"
PAPER_TEX="dist/mcp-research-paper.tex"
PAPER_PDF="dist/mcp-research-paper.pdf"

{
  echo "---"
  echo "title: Model Context Protocol as an Integration Backbone for Enterprise and Government AI"
  echo "author: MCP Research Team"
  echo "date: 2026-04-29"
  echo "bibliography: ../latex/references.bib"
  echo "---"
  echo
  for file in paper/*.md; do
    echo
    echo "<!-- source: ${file} -->"
    echo
    cat "$file"
    echo
  done
} > "$PAPER_MD"

echo "Built combined Markdown: $PAPER_MD"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Pandoc not found; skipping TeX/PDF generation."
  echo "Install pandoc and a XeLaTeX distribution, then rerun ./scripts/build.sh."
  exit 0
fi

pandoc "$PAPER_MD" \
  --from markdown+pipe_tables+table_captions \
  --standalone \
  --citeproc \
  --bibliography latex/references.bib \
  --metadata link-citations=true \
  -o "$PAPER_TEX"

echo "Built LaTeX: $PAPER_TEX"

if command -v xelatex >/dev/null 2>&1; then
  pandoc "$PAPER_MD" \
    --from markdown+pipe_tables+table_captions \
    --pdf-engine=xelatex \
    --citeproc \
    --bibliography latex/references.bib \
    --metadata link-citations=true \
    -o "$PAPER_PDF"
  echo "Built PDF: $PAPER_PDF"
else
  echo "XeLaTeX not found; skipping PDF generation."
fi
