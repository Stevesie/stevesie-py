import os

import requests


BASE_URL = 'https://stevesie.com/api/v1/'
TOKEN_ENV_KEY = 'STEVESIE__API_TOKEN'

def __token():
    return os.getenv('TOKEN_ENV_KEY')

def get(url, params=None):
    result = requests.get(BASE_URL + url,
        headers={'Token': __token()},
        params=params)
    return result.json()
