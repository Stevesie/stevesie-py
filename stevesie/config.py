import os
import configparser

CONFIG_FILE_ENV_KEY = 'STEVESIE_CONFIG_FILE'

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.expanduser(os.getenv(CONFIG_FILE_ENV_KEY, '~/stevesie.cfg')))

API_TOKEN = CONFIG['core']['api_token']
BASE_HOST = CONFIG['core']['base_host']

def worker_id_for(lookup_str):
    return CONFIG['workers'][lookup_str]
