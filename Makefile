.DEFAULT_GOAL := fmt

.PHONY: fmt
fmt:
	uvx ruff format .
