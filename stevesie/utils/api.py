import logging
import sys
import json

import requests

from stevesie.config import CONFIG, API_TOKEN, BASE_URL

BASE_URL_PATH = BASE_URL + '/api/v1/'

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def get(url, params=None):
    params_log = params or ''
    logging.info('Fetching %s %s', url, params_log)
    response = requests.get(
        url,
        headers={'Token': API_TOKEN},
        params=params)

    if response.status_code == 401:
        raise Exception('Access Denied - Check your token or the resource URL')
    return response.json()

def post(url, params=None, query=None):
    query_log = query or ''
    logging.info('Posting %s %s', url, query_log)
    response = requests.post(
        url,
        headers={'Token': API_TOKEN},
        json=params,
        params=query)

    if response.status_code == 401:
        raise Exception('Access Denied - Check your token or the resource URL')

    try:
        return response.json(), response.status_code
    except json.decoder.JSONDecodeError:
        return response.text, response.status_code

def delete(url):
    logging.info('Deleting %s', url)
    requests.delete(url, headers={'Token': API_TOKEN})
