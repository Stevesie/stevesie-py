from collections import namedtuple
from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource

class TaskCollectionFields(NamedTuple):
    id: str
    name: str
    created_at: datetime

TaskCollectionFields.__new__.__defaults__ = (None,) * len(TaskCollectionFields._fields)

class TaskCollection(TaskCollectionFields, RemoteResource):

    @property
    def resource_path(self):
        return 'task-collections/{}'.format(self.id)
