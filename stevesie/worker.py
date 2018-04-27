import logging

from typing import NamedTuple
from datetime import datetime

from stevesie.utils import api

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

    def __init__(self, meta_vars=None):
        self._worker_collection_results = None
        super(Worker, self).__init__(meta_vars)

    def run(self, params=None):
        params = params or {}
        resp_json, status_code = api.post(self.resource_url + '/executions', params)
        if status_code == 400:
            if resp_json['errors'].get('proxy'):
                logging.warn('Please launch a proxy to run your worker.')
            return False
        return True

    def fetch_results(self, task_collection_id=None):
        self._worker_collection_results = WorkerCollectionResults(
            {'worker_id': self._id, 'task_collection_id': task_collection_id}).fetch()
        return self._worker_collection_results

    def load_results(self, local_filepath):
        self._worker_collection_results = WorkerCollectionResults(
            {'worker_id': self._id}).load_from_file(local_filepath)
        return self._worker_collection_results

    @property
    def resource_path(self):
        return 'workers/{}'.format(self._id)
