from stevesie.remote_resource import RemoteResource


class Worker(RemoteResource):

    def resource_url(self):
        return 'workers/{}'.format(self.id)
