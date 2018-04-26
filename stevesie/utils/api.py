import logging
import sys

import requests

from stevesie.config import API_TOKEN, BASE_HOST

BASE_URL = BASE_HOST + '/api/v1/'

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def get(url, params=None):
    params_log = params or ''
    logging.info('Fetching %s %s', url, params_log)
    response = requests.get(
        url,
        verify=False, # TODO - remove! seemingly related to openSSL shipped in macOS
        headers={'Token': API_TOKEN},
        params=params)

    if response.status_code == 401:
        raise Exception('Access Denied - Check your token or the resource URL')
    return response.json()
