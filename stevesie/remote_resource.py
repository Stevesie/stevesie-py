class RemoteResource(object):

    def __init__(self, id):
        self._id = id
        self._hydrated = False

    @property
    def id(self):
        return self._id

    @property
    def hydrated(self):
        return self._hydrated
