from stevesie.remote_resource import RemoteResource


class Worker(RemoteResource):

    @property
    def resource_url(self):
        return 'workers/{}'.format(self.id)
