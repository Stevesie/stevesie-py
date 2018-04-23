from collections import namedtuple
from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.task_collection_field import TaskCollectionField

class TaskCollectionTuple(NamedTuple):
    id: str
    name: str
    created_at: datetime
    childTaskCollections: Sequence['TaskCollection']
    taskCollectionFields: Sequence[TaskCollectionField]

TaskCollectionTuple.__new__.__defaults__ = (None,) * len(TaskCollectionTuple._fields)

class TaskCollection(TaskCollectionTuple, RemoteResource):
    pass
