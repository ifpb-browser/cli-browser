.DEFAULT_GOAL := fmt


.venv:
	python3 -m venv .venv
	pip install -e .

.PHONY: fmt
fmt: .venv
	./.venv/bin/ruff format .

.PHONY: run
run: 
	pip install -e .
	python -m cli_browser

.PHONY: clean
clean:
	rm -rf www.* .venv .ruff_cache
