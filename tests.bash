#!/bin/bash

set -x
TEST_PATH=${TEST_PATH:-./src}
export PYTHONPATH=./src
coverage run -m --source=./src pytest -vv $TEST_PATH && coverage report -m --fail-under=90
