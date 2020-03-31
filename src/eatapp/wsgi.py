"""
WSGI config for eatapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

### this line is from setting up deploying on heroku
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eatapp.settings')

application = get_wsgi_application()

### this line is from setting up deploying on heroku
application = DjangoWhiteNoise(application)
