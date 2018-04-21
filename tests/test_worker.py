import uuid
import pytest

from stevesie.worker import Worker

def test_init():
    worker_id = uuid.uuid4()
    worker = Worker(worker_id)
    assert worker.id == worker_id
    assert worker.is_hydrated == False
