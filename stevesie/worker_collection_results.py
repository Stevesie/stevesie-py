from typing import NamedTuple, Sequence

from stevesie.remote_resource_sequence import RemoteResourceSequence
from stevesie.task_collection_result_set import TaskCollectionResultSet


class WorkerCollectionResults(RemoteResourceSequence):

    def __init__(self, meta_vars):
        self._worker_id = meta_vars['worker_id']
        self._task_collection_id = meta_vars.get('task_collection_id')
        super(WorkerCollectionResults, self).__init__()

    @property
    def collection_type(self):
        return TaskCollectionResultSet

    @property
    def resource_path(self):
        return 'workers/{}/collection-results'.format(self._worker_id)

    @property
    def resource_params(self):
        return {'taskCollectionId': self._task_collection_id}
