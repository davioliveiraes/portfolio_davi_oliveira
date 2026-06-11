import io
import json
import urllib.error
from unittest.mock import patch

from django.core.cache import cache

import pytest

from apps.core.services import CACHE_KEY, get_github_repos

GITHUB_PAYLOAD = [
    {
        "name": "portfolio_davi_oliveira",
        "stargazers_count": 3,
        "language": "Python",
        "pushed_at": "2026-06-01T12:00:00Z",
    },
    {
        "name": "jwt_order_api",
        "stargazers_count": 1,
        "language": "Python",
        "pushed_at": "2026-05-02T10:00:00Z",
    },
]


def fake_response(payload):
    body = io.BytesIO(json.dumps(payload).encode())
    body.__enter__ = lambda *a: body
    body.__exit__ = lambda *a: None
    return body


class TestGetGithubRepos:
    def setup_method(self):
        cache.delete(CACHE_KEY)

    @patch("apps.core.services.urllib.request.urlopen")
    def test_returns_repos_indexed_by_name(self, mock_urlopen):
        mock_urlopen.return_value = fake_response(GITHUB_PAYLOAD)
        repos = get_github_repos()
        assert set(repos) == {"portfolio_davi_oliveira", "jwt_order_api"}
        assert repos["portfolio_davi_oliveira"]["stars"] == 3
        assert repos["portfolio_davi_oliveira"]["language"] == "Python"
        assert str(repos["portfolio_davi_oliveira"]["pushed_at"]) == "2026-06-01"

    @patch("apps.core.services.urllib.request.urlopen")
    def test_caches_result(self, mock_urlopen):
        mock_urlopen.return_value = fake_response(GITHUB_PAYLOAD)
        get_github_repos()
        get_github_repos()
        assert mock_urlopen.call_count == 1

    @patch("apps.core.services.urllib.request.urlopen")
    def test_returns_empty_dict_on_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("offline")
        assert get_github_repos() == {}

    @patch("apps.core.services.urllib.request.urlopen")
    def test_failure_is_cached_to_avoid_hammering(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("offline")
        get_github_repos()
        get_github_repos()
        assert mock_urlopen.call_count == 1
