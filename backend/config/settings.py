from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from split_settings.tools import include

dotenv_path = find_dotenv(filename='infra/.env')
load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).resolve().parent.parent

include(
    'components/base.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/auth_password_validators.py',
    'components/database.py',
    'components/internationalization.py',
    'components/templates.py',
    'components/url_settings.py',
    'components/rest_framework.py',
    'components/simple_jwt.py',
    'components/project_settings.py',
    'components/debug_settings.py',
)
