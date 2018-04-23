from collections import namedtuple
from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource

class TaskCollectionFieldTuple(NamedTuple):
    id: str
    fieldName: str
    fieldType: str
    isPrimaryKey: bool
    created_at: datetime

TaskCollectionFieldTuple.__new__.__defaults__ = (None,) * len(TaskCollectionFieldTuple._fields)

class TaskCollectionField(TaskCollectionFieldTuple, RemoteResource):
    pass
