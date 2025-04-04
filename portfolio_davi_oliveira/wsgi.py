"""
WSGI config for portfolio_davi_oliveira project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_davi_oliveira.settings")

application = get_wsgi_application()

from whitenoise import WhiteNoise
from django.conf import settings

application = WhiteNoise(application)
application.add_files(settings.MEDIA_ROOT, prefix="media/")
