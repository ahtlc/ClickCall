from .base import *
import django_heroku

DEBUG = False
SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Django-heroku configuration
django_heroku.settings(locals())
