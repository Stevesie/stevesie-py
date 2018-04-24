from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource_sequence import RemoteResourceSequence
from stevesie.task_collection_result import TaskCollectionResult

class TaskCollectionResultSetTuple(NamedTuple):
    taskCollectionId: str
    taskCollectionResults: Sequence[TaskCollectionResult]
    total: int

TaskCollectionResultSetTuple.__new__.__defaults__ = (None,) * len(TaskCollectionResultSetTuple._fields)

class TaskCollectionResultSet(TaskCollectionResultSetTuple, RemoteResourceSequence):

    @property
    def collection_field(self):
        return 'taskCollectionResults'
