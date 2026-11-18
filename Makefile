.DEFAULT_GOAL := fmt


.venv:
	python3 -m venv .venv
	./.venv/bin/pip install -e '.[dev]'

.PHONY: fmt
fmt: .venv
	./.venv/bin/ruff format .

.PHONY: run
run: .venv
	./.venv/bin/python -m cli_browser

.PHONY: clean
clean:
	rm -rf www.* .venv .ruff_cache
