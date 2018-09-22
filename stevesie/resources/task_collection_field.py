from typing import NamedTuple
from datetime import datetime

from stevesie.remote_resource import RemoteResource

class TaskCollectionFieldTuple(NamedTuple):
    id: str
    field_name: str
    field_type: str
    is_primary_key: bool
    created_at: datetime

TaskCollectionFieldTuple.__new__.__defaults__ = (None,) * len(TaskCollectionFieldTuple._fields)

class TaskCollectionField(TaskCollectionFieldTuple, RemoteResource):
    pass
