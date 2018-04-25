import os
import logging
import json

import requests

from stevesie.config import API_TOKEN, BASE_HOST


BASE_URL = BASE_HOST + '/api/v1/'

def get(url, params=None):
    logging.info('Fetching {} {}'.format(url, params or ''))
    print('Fetching {} {}'.format(url, params or ''))
    response = requests.get(url,
        verify=False, # TODO - remove! seemingly related to openSSL shipped in macOS
        headers={'Token': API_TOKEN},
        params=params)

    if response.status_code == requests.codes.unauthorized:
        raise Exception('Token unauthenticated. Please double check your STEVESIE__API_TOKEN environment variable and ensure the token was not revoked.')
    return response.json()
