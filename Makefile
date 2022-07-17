-include development.env
export

lint_check:
	flake8 app/src

local/build/dependencies/install:
	$(PYTHON_BIN)/pip install -r requirements.txt

local/build/dependencies/lib/safety-check:
	$(PYTHON_BIN)/safety check -r requirements.txt

local/build/code-style:
	$(PYTHON_BIN)/flake8 src/

local/build: local/build/dependencies/install local/build/code-style local/build/dependencies/lib/safety-check

test: local/build
	 $(PYTHON_BIN)/pytest src -v -x --cov-fail-under=80

migrate:
    python src/test_migrate.py

PYTHON_BIN ?= .venv/bin
