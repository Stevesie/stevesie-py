from typing import NamedTuple, Sequence

from stevesie.remote_resource_sequence import RemoteResourceSequence
from stevesie.resources.task_collection_result import TaskCollectionResult

class TaskCollectionResultSetTuple(NamedTuple):
    worker_id: str
    task_collection_id: str
    task_collection_results: Sequence[TaskCollectionResult]
    total: int

TaskCollectionResultSetTuple.__new__.__defaults__ = (None,) \
    * len(TaskCollectionResultSetTuple._fields)

class TaskCollectionResultSet(TaskCollectionResultSetTuple, RemoteResourceSequence):

    @property
    def results(self):
        return [o.object for o in self.task_collection_results]

    @property
    def collection_field(self):
        return 'task_collection_results'

    @property
    def resource_path(self):
        assert self.worker_id
        return 'workers/{}/collection-results'.format(self.worker_id)

    @property
    def resource_params(self):
        return {'taskCollectionId': self.task_collection_id}
