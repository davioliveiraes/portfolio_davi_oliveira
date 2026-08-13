.PHONY: help deploy run test

PYTHON := $(if $(wildcard venv/Scripts/python.exe),venv/Scripts/python.exe,venv/bin/python)

help:
	@echo "make run      inicia o servidor de desenvolvimento (porta 8000)"
	@echo "make test     roda a suíte de testes"
	@echo "make deploy   publica o branch main na VPS"

run:
	$(PYTHON) manage.py runserver

test:
	$(PYTHON) -m pytest -q

# Configuração da VPS em deploy/deploy.conf (fora do git)
deploy:
	./deploy/update.sh
