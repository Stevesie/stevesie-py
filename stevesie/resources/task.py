from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.resources.task_dependency import TaskDependency
from stevesie.resources.task_collection import TaskCollection

class TaskFields(NamedTuple):
    id: str
    name: str
    description: str
    is_public: bool
    slug: str
    method: str
    scheme: str
    host: str
    port: int
    path: str
    body: str
    created_at: datetime
    task_dependencies: Sequence[TaskDependency]
    task_collections: Sequence[TaskCollection]

TaskFields.__new__.__defaults__ = (None,) * len(TaskFields._fields)

class Task(TaskFields, RemoteResource):

    @property
    def resource_path(self):
        assert self.id
        return 'tasks/{}'.format(self.id)
