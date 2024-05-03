from config.components.base import DEBUG
from config.components.installed_apps import INSTALLED_APPS
from config.components.middleware import MIDDLEWARE

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'formatters': {
            'default': {
                'format': ('%(asctime)s %(levelname)s: %(message)s '
                           '[in %(pathname)s:%(lineno)d]'),
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'filters': ['require_debug_true'],
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }
