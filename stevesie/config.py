import os
import configparser

CONFIG_FILE_ENV_KEY = 'STEVESIE_CONFIG_FILE'
DEFAULT_BASE_URL = 'https://stevesie.com'

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.expanduser(os.getenv(CONFIG_FILE_ENV_KEY, '~/stevesie.cfg')))

api_token = None
base_url = None

if CONFIG.has_section('core'):
    api_token = CONFIG.get('core', 'api_token')
    base_url = CONFIG.get('core', 'base_url')

API_TOKEN = os.getenv('STEVESIE_API_TOKEN') or api_token
BASE_URL = os.getenv('STEVESIE_BASE_URL') or base_url or DEFAULT_BASE_URL
