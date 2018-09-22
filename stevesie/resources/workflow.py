from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource
from stevesie.resources.workflow_parameter import WorkflowParameter
from stevesie.resources.workflow_task import WorkflowTask

class WorkflowFields(NamedTuple):
    id: str
    name: str
    description: str
    is_public: bool
    slug: str
    created_at: datetime
    workflow_parameters: Sequence[WorkflowParameter]
    workflow_tasks: Sequence[WorkflowTask]

WorkflowFields.__new__.__defaults__ = (None,) * len(WorkflowFields._fields)

class Workflow(WorkflowFields, RemoteResource):

    @property
    def resource_path(self):
        assert self.id
        return 'workflows/{}'.format(self.id)
