#!/bin/sh

show() {
  echo "\n=========================================== $1 ==============================================="
}

. ./development.env

show "Testing and checking coverage for Python code"

COV_THRESHOLD=100;
export PYTHONPATH="$PWD/app"
docker exec -it posterr_web pytest
coverage report -m --omit="*test*"

show "Checking lint"
flake8 app/
