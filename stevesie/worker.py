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

    def get_run_params(self):
        if self.task:
            return self.task.task_dependencies
        else:
            return self.workflow.workflow_parameters

    def run(self, params=None):
        params = params or {}

        run_params = self.get_run_params()
        for run_param in run_params:
            print(run_param)

        resp_json, status_code = api.post(self.resource_url + '/executions', params)
        if status_code == 400:
            if resp_json['errors'].get('proxy'):
                logging.info('Please launch a proxy to run your worker.')
            return False
        return True

    def build_worker_collection_results(self):
        collection_results = WorkerCollectionResults()
        collection_results.worker_id = self.id
        return collection_results

    def fetch_results(self):
        return self.build_worker_collection_results().fetch()

    def load_results(self, local_filepath):
        return self.build_worker_collection_results().load_from_file(local_filepath)

    @property
    def resource_path(self):
        return 'workers/{}'.format(self.id)
