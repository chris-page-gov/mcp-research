PYTHON ?= uv run python
RUFF ?= uv run ruff
MYPY ?= uv run mypy

REPORT_DATE ?= $(shell date -u +%F)

.PHONY: all build check check-links check-citations validate-wiki codex-summary lint format typecheck clean clean-metadata

all: build

build:
	@./scripts/build.sh

check: clean-metadata check-citations check-links validate-wiki

clean-metadata:
	@find . -name .DS_Store -delete

check-links:
	@$(PYTHON) scripts/check_links.py

check-citations:
	@$(PYTHON) scripts/check_citations.py

validate-wiki:
	@$(PYTHON) scripts/validate_wiki_state.py

codex-summary:
	@$(PYTHON) scripts/codex_project_summary.py \
		--repo-filter mcp-research \
		--summary-title "Codex MCP-Research Summary" \
		--output reports/mcp_research_codex_project_summary_$(REPORT_DATE).md \
		--json-output reports/mcp_research_codex_project_summary_$(REPORT_DATE).json \
		--summary-svg-output reports/mcp_research_codex_project_summary_$(REPORT_DATE).svg \
		--summary-pdf-output reports/mcp_research_codex_project_summary_$(REPORT_DATE).pdf \
		--summary-png-output reports/mcp_research_codex_project_summary_$(REPORT_DATE).png

lint:
	@$(RUFF) check scripts

format:
	@$(RUFF) format scripts

typecheck:
	@$(MYPY) scripts

clean:
	@rm -rf dist
