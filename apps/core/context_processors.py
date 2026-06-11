import subprocess
from functools import lru_cache

from django.conf import settings


@lru_cache(maxsize=1)
def _last_commit_date():
    try:
        return (
            subprocess.check_output(
                ["git", "log", "-1", "--format=%cd", "--date=format:%d/%m/%Y"],
                cwd=settings.BASE_DIR,
                stderr=subprocess.DEVNULL,
                timeout=5,
            )
            .decode()
            .strip()
        )
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        return None


def site_meta(request):
    return {"last_update": _last_commit_date()}
