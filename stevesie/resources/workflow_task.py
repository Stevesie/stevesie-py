from typing import NamedTuple
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.resources.task import Task

class WorkflowTaskTuple(NamedTuple):
    id: str
    created_at: datetime
    task: Task

WorkflowTaskTuple.__new__.__defaults__ = (None,) * len(WorkflowTaskTuple._fields)

class WorkflowTask(WorkflowTaskTuple, RemoteResource):
    pass
