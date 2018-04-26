from typing import NamedTuple
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.task import Task
from stevesie.workflow import Workflow
from stevesie.worker_collection_results import WorkerCollectionResults

class WorkerFields(NamedTuple):
    id: str
    name: str
    created_at: datetime
    task: Task
    workflow: Workflow

WorkerFields.__new__.__defaults__ = (None,) * len(WorkerFields._fields)

class Worker(WorkerFields, RemoteResource):

    def __init__(self, *args, **kwargs):
        self._worker_collection_results = None
        super(Worker, self).__init__()

    def fetch_results(self, task_collection_id=None):
        self._worker_collection_results = WorkerCollectionResults(
            {'worker_id': self.id, 'task_collection_id': task_collection_id}).fetch()
        return self._worker_collection_results

    def load_results(self, local_filepath):
        self._worker_collection_results = WorkerCollectionResults(
            {'worker_id': self.id}).load_from_file(local_filepath)
        return self._worker_collection_results

    @property
    def resource_path(self):
        return 'workers/{}'.format(self.id)
