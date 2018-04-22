from collections import namedtuple
from typing import NamedTuple
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.task import Task

class WorkerFields(NamedTuple):
    id: str
    name: str
    created_at: datetime
    # user: RemoteResource
    task: Task
    # workflow: RemoteResource
    # vault_entries: RemoteResource
    # work_schedules: RemoteResource
    # work_extractions: RemoteResource

WorkerFields.__new__.__defaults__ = (None,) * len(WorkerFields._fields)

class Worker(WorkerFields, RemoteResource):

    @property
    def resource_path(self):
        return 'workers/{}'.format(self.id)
