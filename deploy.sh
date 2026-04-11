#!/bin/bash
set -e

PROJECT_DIR="/home/davi/portfolio_davi_oliveira"
VENV_DIR="$PROJECT_DIR/venv"

echo "==> Atualizando código..."
cd "$PROJECT_DIR"
git pull origin main

echo "==> Ativando virtualenv..."
source "$VENV_DIR/bin/activate"

echo "==> Instalando dependências..."
pip install -r requirements.txt --quiet

echo "==> Aplicando migrações..."
python manage.py migrate --noinput

echo "==> Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "==> Reiniciando serviços..."
sudo systemctl restart portfolio
sudo systemctl restart nginx

echo "==> Deploy concluído com sucesso!"
