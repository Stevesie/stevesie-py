from abc import ABC, abstractmethod

from stevesie.utils import api

class RemoteResource(ABC):

    def __init__(self, id):
        self._id = id
        self._is_hydrated = False
        super(RemoteResource, self).__init__()

    def fetch(self):
        return api.get(self.resource_url)

    @property
    def id(self):
        return self._id

    @property
    def is_hydrated(self):
        return self._is_hydrated

    @property
    @abstractmethod
    def resource_url(self):
        pass
