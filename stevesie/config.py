import os
import configparser

CONFIG_FILE_ENV_KEY = 'STEVESIE_CONFIG_FILE'

config = configparser.ConfigParser()
config.read(os.path.expanduser(os.getenv(CONFIG_FILE_ENV_KEY, '~/stevesie.cfg')))

API_TOKEN = config['core']['api_token']
BASE_HOST = config['core']['base_host']

def worker_id_for(lookup_str):
    return config['workers'][lookup_str]
