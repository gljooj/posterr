-include development.env
export

setup:
    pip install -r app/requirements.txt

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

test:
	docker exec -it posterr_web_1 pytest

lint_check:
	flake8


local/build/dependencies/install:
	$(PYTHON_BIN)/pip install -r requirements.txt


PYTHON_BIN ?= .venv/bin
