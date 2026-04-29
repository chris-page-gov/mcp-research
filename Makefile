PYTHON ?= uv run python
RUFF ?= uv run ruff
MYPY ?= uv run mypy

.PHONY: all build check check-links check-citations validate-wiki lint format typecheck clean

all: build

build:
	@./scripts/build.sh

check: check-citations check-links validate-wiki

check-links:
	@$(PYTHON) scripts/check_links.py

check-citations:
	@$(PYTHON) scripts/check_citations.py

validate-wiki:
	@$(PYTHON) scripts/validate_wiki_state.py

lint:
	@$(RUFF) check scripts

format:
	@$(RUFF) format scripts

typecheck:
	@$(MYPY) scripts

clean:
	@rm -rf dist
