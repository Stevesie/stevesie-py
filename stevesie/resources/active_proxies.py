import logging

from stevesie.remote_resource_sequence import RemoteResourceSequence

from stevesie.utils import api
from stevesie.resources.proxy import Proxy

class ActiveProxies(RemoteResourceSequence):

    def launch(self, location='nyc3'):
        send_json = {
            'location': location,
            'blurImages': False
        }
        resp_json, status_code = api.post(api.BASE_URL + 'proxies', send_json)
        if status_code == 400:
            logging.info('Failed to launch proxy.')
            return False
        return self.hydrate([resp_json['item']])

    @property
    def collection_type(self):
        return Proxy

    @property
    def resource_path(self):
        return 'proxies/current'
