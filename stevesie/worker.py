from collections import namedtuple
from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.task import Task
from stevesie.task_collection_result_set import TaskCollectionResultSet

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

    def __init__(self, *args, **kwargs):
        self.result_sets = {}
        super(Worker, self).__init__(*args, **kwargs)

    def fetch_results(self, task_collection_id=None):
        r = TaskCollectionResultSet({'worker_id': self.id, 'task_collection_id': task_collection_id})
        f = r.fetch()

    @property
    def resource_path(self):
        return 'workers/{}'.format(self.id)
