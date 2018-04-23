from typing import NamedTuple

from stevesie.remote_resource import RemoteResource

class TaskCollectionResultTuple(NamedTuple):
    object: object

TaskCollectionResultTuple.__new__.__defaults__ = (None,) * len(TaskCollectionResultTuple._fields)

class TaskCollectionResult(TaskCollectionResultTuple, RemoteResource):
    pass
