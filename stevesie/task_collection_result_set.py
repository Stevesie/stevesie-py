from typing import NamedTuple, Sequence

from stevesie.remote_resource_sequence import RemoteResourceSequence
from stevesie.task_collection_result import TaskCollectionResult

class TaskCollectionResultSetTuple(NamedTuple):
    taskCollectionId: str
    results: Sequence[TaskCollectionResult]
    # taskResult: TaskResult
    # collectedAt: datetime

TaskCollectionResultSetTuple.__new__.__defaults__ = (None,) * len(TaskCollectionResultSetTuple._fields)

class TaskCollectionResultSet(TaskCollectionResultSetTuple, RemoteResourceSequence):

    def __init__(self, meta_vars):
        self._worker_id = meta_vars['worker_id']
        self._task_collection_id = meta_vars.get('task_collection_id')
        super(TaskCollectionResultSet, self).__init__()

    @property
    def resource_path(self):
        return 'workers/{}/collection-results'.format(self._worker_id)

    def parse_api_response(self, api_json):
        return api_json
