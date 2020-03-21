PYTHONPATH=.
SCRIPTS=scripts/
TESTS=tests/

ifndef PYTHON
	PYTHON=python
endif
ifndef ENV_FILE
	ENV_FILE=.deploy/.envs/test.env
endif
ifndef PYTEST
	PYTEST=pytest
endif
ifndef PIP
	PIP=pip
endif
ifndef TEST_SUBFOLDER
	TEST_SUBFOLDER=./
endif

ENVS=PYTHONPATH=${PYTHONPATH} ENV_FILE=${ENV_FILE}

run:
	$(info app starting...)
	$(info $(ENVS))
	$(ENVS) $(PYTHON) app.py

local-run:
	$(info local app starting...)
	$(info $(ENVS))
	$(ENVS) ENV_FILE=.deploy/.envs/local.env $(PYTHON) app.py

deps:
	$(info dependencies installing...)
	$(info $(ENVS))
	$(PIP) install -r requirements
