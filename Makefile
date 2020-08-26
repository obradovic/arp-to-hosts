.PHONY: .

SHELL := /bin/bash

TIMER := TIMEFORMAT="That took %1R seconds" && time  # bash built-in, requires bash to be the SHELL above
ifdef NO_TIMER
    TIMER :=
endif


all: black typecheck lint test
	@echo ""
	@echo "ALL GOOD!"
	@echo ""

black:
	@black *.py

lint:
	@pylint_runner -v --rcfile .pylintrc .

typecheck:
	@mypy *.py


coverage: coverage-run coverage-report

coverage-run:
	@coverage run --source=. -m pytest -c setup.cfg --durations=5 --disable-warnings .

coverage-report:
	@echo
	@echo
	@coverage report -m

test:
	@py.test --cov-report term-missing --cov=. .

run:
	@./arp_to_hosts

clean:
	@rm -rf .coverage .mypy_cache .pytest_cache __pycache__ build dist *.egg-info

#
# Below this, things are only useful for wheel management
#
wheel: wheel-build wheel-install

# Builds the wheel
wheel-build:
	@python3 setup.py bdist_wheel

# Installs the wheel
wheel-install:
	@python3 -m pip install --force dist/*.whl

# Uploads to pypi
wheel-push:
	@python3 -m twine upload dist/*.whl

# Initializes the environment - only need to run once
init:
	@python3 -m virtualenv .env
	@python3 -m pip install --upgrade pip setuptools wheel tqdm twine
	@python3 -m pip install -r requirements.txt

