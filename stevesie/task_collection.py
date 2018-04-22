from collections import namedtuple
from typing import NamedTuple, Sequence
from datetime import datetime

from stevesie.remote_resource import RemoteResource

class TaskCollectionTuple(NamedTuple):
    id: str
    name: str
    created_at: datetime
    childTaskCollections: Sequence['TaskCollection']

TaskCollectionTuple.__new__.__defaults__ = (None,) * len(TaskCollectionTuple._fields)

class TaskCollection(TaskCollectionTuple, RemoteResource):

    @property
    def resource_path(self):
        return 'task-collections/{}'.format(self.id)
