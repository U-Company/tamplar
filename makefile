PYTHONPATH=.
TESTS=tests/

ifndef PYTHON
	PYTHON=python
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
ifndef VAULT_ENV
	VAULT_ENV=.deploy/.envs/local.env
endif

ENVS=PYTHONPATH=${PYTHONPATH} VAULT_FILE=${VAULT_ENV}

run:
	$(info $(ENVS))
	$(info ${STORAGE_ENV_FILE})
	$(ENVS) $(PYTHON) app.py

test:
	$(info $(ENVS))
	$(info ${TESTS}${TEST_SUBFOLDER})
	$(ENVS) $(PYTEST) -v -l --disable-warnings ${TESTS}${TEST_SUBFOLDER}

deps:
	$(info $(ENVS))
	$(PIP) install -r requirements
