from stevesie.remote_resource import RemoteResource


class Worker(RemoteResource):

    @property
    def resource_path(self):
        return 'workers/{}'.format(self.id)
