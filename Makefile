.DEFAULT_GOAL := fmt

.PHONY: fmt
fmt:
	uvx ruff format .

.PHONY: clean
clean:
	rm -f www.*
