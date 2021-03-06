# NOTICE

We don't use this repo. Instead of, we use [cookiecutter](https://github.com/cookiecutter/cookiecutter) and makefile in each repo layout.

# Tamplar

Tamplar is service generator. This project can to help you control your local development. We think, you should development
with isolated environment. Therefore we creates docker-compose for local debugging and testing. 

Please, don't use tamplar for deployment or other automatically processes. This util is used to only for simplyfy development.

Now, we use [this](https://github.com/U-Company/python-service-layout) python layout.

# Installing

    pip install tamplar
    
If you want to use local environments, you need a docker. Please install:

    sudo apt-get install docker.io
    
We don't use docker-compose as console util. We build docker-compose from source and we use docker API into python code.

# Usage

tamplar can work with:

- pip
- publishing package to pypi registry
- publishing docker to docker registry
- docker-compose for local development
    
# Console running

### Init

Go to empty directory and init your first project

    tamplar init
    
After that, you get [FastAPI](https://fastapi.tiangolo.com/) service with healthcheck methods. FastAPI is ASGI framework
instead of [Flask](https://flask.palletsprojects.com/).

If you want reinitialize, tamplar ask you about cleaning repo. If you work with JetBrains IDE, while initialization we
ignore `.idea` files.

### Deps

We use default excellent library for logging. This is [loguru](https://github.com/Delgan/loguru). Loguru is a very useful
wrapper over standart python [logger](https://docs.python.org/3.8/library/logging.html). After initilize you can install 
all dependencies:

    tamplar deps
    
This command uses `pip` and `requirements`.   

### Upload (Not implemented)

You can upload your package to concrete pypi registry and docker registry

    tamplar upload --docker=True --pypi=True --namespace=<your-namespace from .pypirc>
    
After that, it built your docker image, pypi registry and push to the registry with latest version from `info.py`. 
Registry is selected by namespace parameter.

### Validate (Not implemented)

This command checks struct of project by [python-service-layout](https://github.com/U-Company/python-service-layout).

    tamplar validate

### Run full

This command build and run docker with services with environment (dependencies of services)

    tamplar run --mode=full --build=no
    
We implement execute docker-compose by python library docker-compose internal API. After run, it run docker-compose file
or you get status code error 

### Run env

This command build and run docker WITHOUT services with environment (dependencies of services)

    tamplar run --mode=env --build=yes
    
We implement execute docker-compose by python library docker-compose internal API. After run, it run docker-compose file
or you get status code error
    
### Clean

Clean is command for cleaning your building files:

    tamplar clean
    
# Dependency

If you want to add new service as dependency, you need to go to the `deployment/docker-compose.*.yml`. After that, you 
need new service to your docker-compose files.

# Test

Tamplar have a lot of good tests. But we have not any integration tests, because it is very difficult emulate python's 
environment. Therefore we change integration tests to unit tests mixed integration tests (we creates and deletes files)
while tests:

    make test

If you want to execute test from IDE, you need to go `tests/__init__.py` and change `deep=2`. 
