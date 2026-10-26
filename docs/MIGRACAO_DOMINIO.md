# Migração de domínio: davioliveira.tech → davioliveiraes.com

Checklist para quando a troca de domínio for executada de fato. Nada aqui
roda sozinho — é um guia manual, passo a passo, na ordem recomendada.

O código já está preparado: canonical, OG, sitemap, robots.txt e JSON-LD
derivam todos de `SITE_URL` (uma única variável de ambiente). Trocar de
domínio é majoritariamente configuração, não código.

## 1. DNS

- [ ] Registrar/confirmar a posse de `davioliveiraes.com` no provedor de DNS.
- [ ] Criar os registros A/AAAA de `davioliveiraes.com` (e `www`, se for usar)
      apontando para o IP da VPS atual.
- [ ] Manter os registros de `davioliveira.tech` ativos durante a transição
      (não remover ainda — o redirect do passo 4 precisa do domínio antigo
      respondendo).
- [ ] Aguardar a propagação do DNS antes de seguir (`dig davioliveiraes.com`).

## 2. Certificado SSL (Let's Encrypt / certbot)

- [ ] Na VPS, emitir certificado para o novo domínio:
      `certbot certonly --nginx -d davioliveiraes.com -d www.davioliveiraes.com`
- [ ] Não remover o certificado de `davioliveira.tech` ainda (precisa dele
      para o redirect 301 do passo 4 continuar servindo HTTPS).

## 3. Nginx (server block)

- [ ] Adicionar/ajustar o `server_name` para responder por
      `davioliveiraes.com` (e `www`), apontando para o mesmo `gunicorn` da
      aplicação atual.
- [ ] Testar a config (`nginx -t`) e recarregar (`systemctl reload nginx`).

## 4. Redirect 301: domínio antigo → novo

- [ ] Criar um `server {}` block separado para `davioliveira.tech` que só
      redireciona (301) para `davioliveiraes.com`, **preservando path e
      query string**:
      ```nginx
      server {
          listen 443 ssl;
          server_name davioliveira.tech www.davioliveira.tech;
          # certificado antigo continua aqui
          return 301 https://davioliveiraes.com$request_uri;
      }
      ```
- [ ] Testar alguns paths manualmente (`/curriculo/`, `/en/curriculo/`,
      `/sitemap.xml`) para confirmar que o redirect preserva o caminho.

## 5. Variáveis de ambiente na VPS

- [ ] No `.env` da aplicação (na VPS), atualizar:
      ```
      SITE_URL=https://davioliveiraes.com
      ALLOWED_HOSTS=davioliveiraes.com,www.davioliveiraes.com
      CSRF_TRUSTED_ORIGINS=https://davioliveiraes.com,https://www.davioliveiraes.com
      ```
- [ ] Reiniciar o serviço (`systemctl restart portfolio`, ou via
      `make deploy` / `deploy/update.sh` no próximo deploy normal).
- [ ] Conferir `/sitemap.xml`, `/robots.txt` e o `<head>` de `/curriculo/`
      (canonical, OG, JSON-LD) já mostrando `davioliveiraes.com`.

## 6. Conteúdo do banco

- [ ] O projeto "Portfólio Pessoal" tem um `live_url` apontando para
      `https://davioliveira.tech` (carregado por uma migration de dados —
      ver `apps/core/migrations/0004_seed_portfolio_content.py`). Esse valor
      é **conteúdo**, não é derivado de `SITE_URL` automaticamente. Criar uma
      nova migration de dados atualizando esse campo para
      `https://davioliveiraes.com`, ou editar via `/admin/`.

## 7. Google Search Console

- [ ] Adicionar `davioliveiraes.com` como nova propriedade (verificar posse).
- [ ] Usar a ferramenta "Mudança de endereço" (Change of Address), apontando
      de `davioliveira.tech` para `davioliveiraes.com` — isso acelera o
      Google re-indexar o novo domínio sem perder o histórico.
- [ ] Reenviar o `sitemap.xml` na propriedade nova.
- [ ] Manter a propriedade antiga por alguns meses só para acompanhar a
      migração (tráfego residual, erros de rastreamento).

## 8. Links externos

- [ ] LinkedIn (seção de contato/site).
- [ ] GitHub (bio do perfil e/ou do(s) repositório(s)).
- [ ] Instagram (link na bio).
- [ ] YouTube (descrição do canal).
- [ ] `README.md` do repositório (`Acesse: [davioliveira.tech](...)` →
      atualizar para o novo domínio).

## 9. Verificação final

- [ ] `davioliveira.tech` (com e sem `www`) redireciona 301 para
      `davioliveiraes.com`, preservando path/query, nos dois protocolos.
- [ ] `davioliveiraes.com` serve com certificado válido, sem avisos de
      mixed content.
- [ ] `/`, `/curriculo/`, `/en/` e `/en/curriculo/` respondem normalmente.
- [ ] `/sitemap.xml`, `/robots.txt` e o compartilhamento em redes sociais
      (testar com o debugger de OG do Facebook/LinkedIn) mostram o domínio
      novo.
