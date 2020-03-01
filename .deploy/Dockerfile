FROM ubuntu:18.04 AS BUILD

RUN apt-get update && apt-get upgrade && apt-get -y install make python3.7 python3-pip git
RUN python3.7 -m pip install --upgrade pip

COPY . /app
WORKDIR /app

ENV PIP_CONFIG_FILE .deploy/.secrets/pip.conf

RUN PIP=pip PYTHON=python3.7 make deps
CMD PYTHON=python3.7 make run
