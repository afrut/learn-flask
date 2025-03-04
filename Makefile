# Install make
# Install pyenv and pyenv-virtualenv

PYTHON_VERSION=3.13.2
PYENV_VIRTUALENV_NAME=learn-flask

all: \
	create_virtualenv

create_virtualenv:
	@pyenv install ${PYTHON_VERSION} --skip-existing && \
	pyenv virtualenv ${PYTHON_VERSION} ${PYENV_VIRTUALENV_NAME} --force && \
	pyenv local ${PYENV_VIRTUALENV_NAME}

install_python_requirements:
	@pip install -r requirements.txt

# make run_app APP=basic_graphql
APP=basic
run_app:
	@flask --app ${APP} run

# make debug_app APP=basic_graphql
debug_app:
	@flask --app ${APP} run --debug

test_basic:
	@python test_basic.py

test_basic_graphql:
	@python test_basic_graphql.py