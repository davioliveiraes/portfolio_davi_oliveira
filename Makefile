.PHONY: help deploy run test cov lint previews

PYTHON := $(if $(wildcard venv/Scripts/python.exe),venv/Scripts/python.exe,venv/bin/python)

help:
	@echo "make run      inicia o servidor de desenvolvimento (porta 8000)"
	@echo "make test     roda a suíte de testes"
	@echo "make cov      roda os testes com relatório de cobertura"
	@echo "make lint     confere formatação (black + isort), como no CI"
	@echo "make previews regera as capas das coleções a partir do GitHub"
	@echo "make deploy   publica o branch main na VPS"

run:
	$(PYTHON) manage.py runserver

test:
	$(PYTHON) -m pytest -q

cov:
	$(PYTHON) -m pytest -q --cov --cov-report=term-missing

lint:
	$(PYTHON) -m black --check .
	$(PYTHON) -m isort --check-only .

# Rode depois de adicionar um projeto em python-projects ou data_science_projects
previews:
	$(PYTHON) scripts/collection_previews.py

# Configuração da VPS em deploy/deploy.conf (fora do git)
deploy:
	./deploy/update.sh
