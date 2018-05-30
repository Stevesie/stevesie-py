from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.task_collection_field import TaskCollectionField

class TaskDependencyTuple(NamedTuple):
    id: str
    variable_name: str
    name: str
    created_at: datetime

TaskDependencyTuple.__new__.__defaults__ = (None,) * len(TaskDependencyTuple._fields)

class TaskDependency(TaskDependencyTuple, RemoteResource):
    pass