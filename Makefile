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

APP=basic
run_app:
	@flask --app ${APP} run

debug_app:
	@flask --app ${APP} run --debug

issue_requests:
	@python issue_requests.py