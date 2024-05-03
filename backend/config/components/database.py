import os

DEFAULT_DB_SCHEMAS: str = os.getenv('DB_SCHEMAS', 'public')

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
#         'NAME': os.getenv('POSTGRES_DB', 'postgres'),
#         'USER': os.getenv('POSTGRES_USER'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', 5432),
#         'OPTIONS': {
#             'options': f'-c search_path={DEFAULT_DB_SCHEMAS}',
#         },
#         'CONN_MAX_AGE': 300,
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}