import os
import configparser

CONFIG_FILE_ENV_KEY = 'STEVESIE_CONFIG_FILE'
DEFAULT_HOST = 'https://stevesie.com'

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.expanduser(os.getenv(CONFIG_FILE_ENV_KEY, '~/stevesie.cfg')))

core_config = CONFIG.get('core') if CONFIG.has_section('core') else {}

API_TOKEN = os.getenv('STEVESIE_API_TOKEN') or core_config.get('api_token')
BASE_HOST = os.getenv('STEVESIE_BASE_HOST') or core_config.get('base_host', DEFAULT_HOST)
