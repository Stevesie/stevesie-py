import logging
import sys

import requests

from stevesie.config import CONFIG, API_TOKEN, BASE_HOST

BASE_URL = BASE_HOST + '/api/v1/'

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def get(url, params=None):
    params_log = params or ''
    logging.info('Fetching %s %s', url, params_log)
    response = requests.get(
        url,
        verify=CONFIG['core'].get('verify_ssl', True),
        headers={'Token': API_TOKEN},
        params=params)

    if response.status_code == 401:
        raise Exception('Access Denied - Check your token or the resource URL')
    return response.json()

def post(url, params=None):
    response = requests.post(
        url,
        verify=CONFIG['core'].get('verify_ssl', True),
        headers={'Token': API_TOKEN},
        json=params)

    if response.status_code == 401:
        raise Exception('Access Denied - Check your token or the resource URL')

    print(url)
    print(response.text)
    return response.json(), response.status_code
