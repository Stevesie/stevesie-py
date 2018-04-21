from abc import ABC, abstractmethod

from stevesie.utils import api

class RemoteResource(ABC):

    def __init__(self, id):
        self._id = id
        self._state = None
        super(RemoteResource, self).__init__()

    def fetch(self):
        self._state = api.get(self.resource_url)
        return self.state

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    @property
    def is_hydrated(self):
        return self._state != None

    @property
    @abstractmethod
    def resource_path(self):
        pass

    @property
    def resource_url(self):
        return api.BASE_URL + self.resource_path
