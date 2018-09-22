import os
import configparser

CONFIG_FILE_ENV_KEY = 'STEVESIE_CONFIG_FILE'
DEFAULT_HOST = 'https://stevesie.com'

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.expanduser(os.getenv(CONFIG_FILE_ENV_KEY, '~/stevesie.cfg')))

API_TOKEN = CONFIG['core']['api_token']
BASE_HOST = CONFIG['core'].get('base_host', DEFAULT_HOST)

def worker_id_for(lookup_str):
    return CONFIG['workers'][lookup_str]
