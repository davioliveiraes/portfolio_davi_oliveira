"""Integração com a API pública do GitHub.

Busca os repositórios do usuário e expõe métricas (estrelas, linguagem,
último push) para enriquecer os cards de projetos. O resultado fica no
cache do Django para não estourar o rate limit (60 req/h sem token) nem
adicionar latência por request.
"""

import json
import logging
import urllib.error
import urllib.request
from datetime import datetime

from django.core.cache import cache

logger = logging.getLogger(__name__)

GITHUB_USER = "davioliveiraes"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&sort=pushed"
CACHE_KEY = "github_repos"
CACHE_TTL = 60 * 60 * 6  # 6 horas
FAILURE_TTL = 60 * 10  # falhou? espera 10 min antes de tentar de novo


def get_github_repos():
    """Retorna {nome_do_repo: {stars, language, pushed_at}} ou {} em falha."""
    repos = cache.get(CACHE_KEY)
    if repos is not None:
        return repos

    try:
        request = urllib.request.Request(
            API_URL,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "davioliveira.tech-portfolio",
            },
        )
        with urllib.request.urlopen(request, timeout=5) as response:
            data = json.load(response)
        repos = {
            repo["name"]: {
                "stars": repo["stargazers_count"],
                "language": repo["language"],
                "pushed_at": datetime.strptime(
                    repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ"
                ).date(),
            }
            for repo in data
        }
        cache.set(CACHE_KEY, repos, CACHE_TTL)
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError):
        logger.exception("Falha ao consultar a API do GitHub")
        repos = {}
        cache.set(CACHE_KEY, repos, FAILURE_TTL)

    return repos
