from stevesie.remote_resource_sequence import RemoteResourceSequence
from stevesie.resources.task_collection_result_set import TaskCollectionResultSet

class WorkerCollectionResults(RemoteResourceSequence):

    _worker_id = None

    @property
    def worker_id(self):
        return self._worker_id

    @worker_id.setter
    def worker_id(self, value):
        self._worker_id = value

    def for_task_collection_id(self, task_collection_id):
        return [r for r in self.items() if r.task_collection_id == task_collection_id][0]

    @property
    def collection_type(self):
        return TaskCollectionResultSet

    @property
    def resource_path(self):
        assert self.worker_id
        return 'workers/{}/collection-results'.format(self._worker_id)
