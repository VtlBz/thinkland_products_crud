import os

DEFAULT_TOKEN: str = 'DEFAULT_SECRET_KEY'
DEFAULT_HOSTS: str = '127.0.0.1 localhost [::1]'

SECRET_KEY = os.getenv('SECRET_KEY', DEFAULT_TOKEN)

DEBUG = os.getenv('DEBUG_STATE', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', DEFAULT_HOSTS).split()

INTERNAL_IPS = os.getenv('INTERNAL_ADDRESSES', '').split()

WSGI_APPLICATION = 'config.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
