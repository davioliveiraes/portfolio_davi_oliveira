#!/bin/bash
#
# deploy/update.sh — Deploy de ATUALIZAÇÃO do portfólio em produção.
#
# Roda da SUA máquina local. Verifica o repositório local, garante que o
# código está no GitHub e conecta na VPS via SSH para aplicar a atualização
# (git pull -> migrate -> collectstatic -> restart) com healthcheck do serviço.
#
# Pré-requisito: autenticação por chave SSH já configurada (ssh-copy-id),
# para conectar sem digitar senha.
#
# Uso:
#   VPS_IP=1.2.3.4 ./deploy/update.sh
#
# Variáveis de ambiente (com defaults):
#   VPS_IP        (obrigatória — aborta se ausente)
#   VPS_USER      (default: root)
#   PROJECT_DIR   (default: /home/portfolio_davi_oliveira)
#   BRANCH        (default: main)
#   SERVICE_NAME  (default: portfolio)

set -e

# --- Configuração via variáveis de ambiente ---
VPS_USER="${VPS_USER:-root}"
PROJECT_DIR="${PROJECT_DIR:-/home/portfolio_davi_oliveira}"
BRANCH="${BRANCH:-main}"
SERVICE_NAME="${SERVICE_NAME:-portfolio}"
SITE_URL="https://davioliveira.tech"

if [ -z "${VPS_IP:-}" ]; then
    echo "❌ VPS_IP não definida."
    echo "   Uso: VPS_IP=<ip-do-servidor> ./deploy/update.sh"
    exit 1
fi

# --- Vai para a raiz do repositório (funciona de qualquer diretório) ---
cd "$(dirname "$0")/.."

echo "==> Verificando o repositório local..."

# 1) Não pode haver alterações não commitadas (o servidor faz git pull)
if [ -n "$(git status --porcelain)" ]; then
    echo "❌ Há alterações não commitadas. Faça commit (ou stash) antes do deploy."
    git status --short
    exit 1
fi

# 2) Precisa estar no branch que será deployado
CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
    echo "❌ Você está no branch '$CURRENT_BRANCH', mas o deploy é do '$BRANCH'."
    echo "   Troque de branch ou rode com BRANCH=$CURRENT_BRANCH ./deploy/update.sh"
    exit 1
fi

# 3) Garante que os commits locais estão no GitHub (o servidor puxa de lá)
git fetch --quiet origin "$BRANCH"
if [ -n "$(git rev-list "origin/$BRANCH..HEAD")" ]; then
    echo "==> Commits locais ainda não enviados. Fazendo push para origin/$BRANCH..."
    git push origin "$BRANCH"
else
    echo "==> Branch já sincronizado com o GitHub."
fi

echo ""
echo "==> Conectando em $VPS_USER@$VPS_IP e atualizando produção..."
echo ""

# Bloco remoto: as variáveis são injetadas como env na frente do `bash -s`,
# por isso o heredoc pode ficar com aspas ('ENDSSH') sem expansão local.
ssh "$VPS_USER@$VPS_IP" \
    "PROJECT_DIR='$PROJECT_DIR' BRANCH='$BRANCH' SERVICE_NAME='$SERVICE_NAME' bash -s" << 'ENDSSH'
set -e

# root não precisa de sudo; usuário comum precisa
if [ "$(id -u)" -eq 0 ]; then SUDO=""; else SUDO="sudo"; fi

echo "==> [remoto] Entrando em $PROJECT_DIR"
cd "$PROJECT_DIR"

echo "==> [remoto] Atualizando código (git pull origin $BRANCH)"
git pull origin "$BRANCH"

echo "==> [remoto] Ativando virtualenv"
source venv/bin/activate

echo "==> [remoto] Aplicando migrações"
python manage.py migrate --noinput

echo "==> [remoto] Coletando arquivos estáticos"
python manage.py collectstatic --noinput

echo "==> [remoto] Reiniciando o serviço $SERVICE_NAME"
set +e   # daqui em diante, diagnosticar em vez de abortar em silêncio
$SUDO systemctl restart "$SERVICE_NAME"
sleep 2

if systemctl is-active --quiet "$SERVICE_NAME"; then
    echo "==> [remoto] ✅ Serviço $SERVICE_NAME está ATIVO."
else
    echo "==> [remoto] ❌ Serviço $SERVICE_NAME NÃO subiu. Últimas linhas do log:"
    journalctl -u "$SERVICE_NAME" -n 30 --no-pager
    exit 1
fi
ENDSSH

echo ""
echo "✅ Deploy concluído com sucesso!"
echo "🌐 $SITE_URL"
