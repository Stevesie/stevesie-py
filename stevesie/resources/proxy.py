from typing import NamedTuple
from datetime import datetime

from stevesie.remote_resource import RemoteResource

class ProxyTuple(NamedTuple):
    id: str
    hostname: str
    port: int
    location: str
    created_at: datetime

ProxyTuple.__new__.__defaults__ = (None,) * len(ProxyTuple._fields)

class Proxy(ProxyTuple, RemoteResource):
    
    @property
    def resource_path(self):
        assert self.id
        return 'proxies/{}'.format(self.id)
