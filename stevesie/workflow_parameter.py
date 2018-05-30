from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource

class WorkflowParameterTuple(NamedTuple):
    id: str
    name: str
    sample_value: str
    created_at: datetime

WorkflowParameterTuple.__new__.__defaults__ = (None,) * len(WorkflowParameterTuple._fields)

class WorkflowParameter(WorkflowParameterTuple, RemoteResource):
    pass
