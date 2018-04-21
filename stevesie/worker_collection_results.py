from stevesie.remote_resource_sequence import RemoteResourceSequence


class WorkerCollectionResults(RemoteResourceSequence):

    @property
    def resource_path(self):
        return 'workers/{}/collection-results'.format(self.id)
