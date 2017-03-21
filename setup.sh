#!/bin/sh

DIR=`dirname $0`
PYTHON_VERSION=`cat ${DIR}/python-version`
PYTHON_ENV=`cat ${DIR}/.python-version`
pyenv install ${PYTHON_VERSION} -s
pyenv virtualenv ${PYTHON_VERSION} ${PYTHON_ENV} -s

pip install -r ${DIR}/requirements.txt
