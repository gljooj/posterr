#!/bin/sh

show() {
  echo "\n=========================================== $1 ==============================================="
}

. ./development.env

show "Testing and checking coverage for Python code"

COV_THRESHOLD=100;
export PYTHONPATH="$PWD/app"
coverage run -m pytest
coverage report -m

show "Checking lint"
flake8 app/
