import os

BASE_DIR = globals().get('BASE_DIR')

ROOT_URLCONF = 'config.urls'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
