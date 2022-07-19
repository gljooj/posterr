-include development.env
export

lint_check:
	flake8

local/build/dependencies/install:
	$(PYTHON_BIN)/pip install -r requirements.txt

local/build/dependencies/lib/safety-check:
	$(PYTHON_BIN)/safety check -r requirements.txt

local/build: local/build/dependencies/install local/build/code-style local/build/dependencies/lib/safety-check

test: local/build
	 $(PYTHON_BIN)/pytest

PYTHON_BIN ?= .venv/bin
