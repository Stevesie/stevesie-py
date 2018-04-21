from abc import ABC, abstractmethod


class RemoteResource(ABC):

    def __init__(self, id):
        self._id = id
        self._hydrated = False
        super(RemoteResource, self).__init__()

    @property
    def id(self):
        return self._id

    @property
    def hydrated(self):
        return self._hydrated

    @property
    @abstractmethod
    def resource_url(self):
        pass
