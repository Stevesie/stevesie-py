import os
import logging
import json

import requests


#BASE_URL = 'https://stevesie.com/api/v1/'
BASE_URL = 'http://localhost:9000/api/v1/'
TOKEN_ENV_KEY = 'STEVESIE__API_TOKEN'

def __token():
    return os.getenv(TOKEN_ENV_KEY)

def get(url, params=None):
    logging.info('Fetching {} {}'.format(url, params or ''))
    print('Fetching {} {}'.format(url, params or ''))
    response = requests.get(url,
        verify=False, # TODO - remove! seemingly related to openSSL shipped in macOS
        headers={'Token': __token()},
        params=params)

    if response.status_code == requests.codes.unauthorized:
        raise Exception('Token unauthenticated. Please double check your STEVESIE__API_TOKEN environment variable and ensure the token was not revoked.')
    return response.json()
