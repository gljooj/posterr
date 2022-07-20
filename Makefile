-include development.env
export

lint_check:
	flake8

test:
	docker exec -it posterr_web_1 pytest

local/build/dependencies/install:
	$(PYTHON_BIN)/pip install -r requirements.txt


PYTHON_BIN ?= .venv/bin
