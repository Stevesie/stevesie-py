from typing import NamedTuple
from datetime import datetime

from stevesie.remote_resource import RemoteResource

class TaskCollectionResultTuple(NamedTuple):
    object: object
    # TODO - rethink these:
    taskResultId: str
    collectedAt: datetime

TaskCollectionResultTuple.__new__.__defaults__ = (None,) * len(TaskCollectionResultTuple._fields)

class TaskCollectionResult(TaskCollectionResultTuple, RemoteResource):
    pass
