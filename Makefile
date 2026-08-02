.PHONY: help deploy run test

help:
	@echo "make run      inicia o servidor de desenvolvimento (porta 8000)"
	@echo "make test     roda a suíte de testes"
	@echo "make deploy   publica o branch main na VPS"

run:
	venv/bin/python manage.py runserver

test:
	venv/bin/python -m pytest -q

# Configuração da VPS em deploy/deploy.conf (fora do git)
deploy:
	./deploy/update.sh
