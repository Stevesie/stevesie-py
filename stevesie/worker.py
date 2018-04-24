from collections import namedtuple
from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.task import Task
from stevesie.worker_collection_results import WorkerCollectionResults

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
        self._worker_collection_results = None
        super(Worker, self).__init__(*args, **kwargs)

    def fetch_results(self, task_collection_id=None):
        self._worker_collection_results = WorkerCollectionResults({'worker_id': self.id, 'task_collection_id': task_collection_id}).fetch()
        return self._worker_collection_results

    @property
    def resource_path(self):
        return 'workers/{}'.format(self.id)
