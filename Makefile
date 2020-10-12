.ONESHELL:
all: install

PYTHON_VENV = .venv_py
_BUILD_VENV := $(shell [ -d $(PYTHON_VENV) ] || \
					echo "Creating $(PYTHON_VENV)"; \
					python3 -m venv $(PYTHON_VENV);)

install: venv
	. $(PYTHON_VENV)/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt 

venv:
	@echo "🕵‍ Checking virtual enviroment..."
	@echo $(_BUILD_VENV)

clean:
	rm -rf "./$(PYTHON_VENV)"