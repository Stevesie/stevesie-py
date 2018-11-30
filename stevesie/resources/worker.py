import logging
import time

from typing import NamedTuple
from datetime import datetime

from stevesie.utils import api

from stevesie.remote_resource import RemoteResource
from stevesie.resources.task import Task
from stevesie.resources.workflow import Workflow
from stevesie.resources.worker_collection_results import WorkerCollectionResults

class WorkerFields(NamedTuple):
    id: str
    name: str
    created_at: datetime
    task: Task
    workflow: Workflow

WorkerFields.__new__.__defaults__ = (None,) * len(WorkerFields._fields)

class Worker(WorkerFields, RemoteResource):

    def run_params(self):
        if self.task:
            return self.task.task_dependencies
        else:
            return self.workflow.workflow_parameters

    def run_param_by_name(self, name):
        return next(p for p in self.run_params() if p.name == name)

    def run(self, inputs=None, saveResults=True):
        inputs = inputs or {}
        resp_json, status_code = api.post(self.resource_url + '/runs', {'inputs': inputs, 'saveResults': saveResults})
        if status_code == 400:
            if resp_json['errors'].get('proxy'):
                logging.info('Please launch a proxy to run your worker.')
            return False
        return resp_json

    def fetch_results(self, limit=None):
        return self.__build_worker_collection_results().fetch(limit)

    def load_results(self, local_filepath):
        return self.__build_worker_collection_results().load_from_file(local_filepath)

    @property
    def resource_path(self):
        assert self.id
        return 'workers/{}'.format(self.id)

    def __build_worker_collection_results(self):
        collection_results = WorkerCollectionResults()
        collection_results.worker_id = self.id
        return collection_results
