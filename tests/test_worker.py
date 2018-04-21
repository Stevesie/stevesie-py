import uuid
import pytest

import requests_mock

from stevesie.worker import Worker

def test_init():
    worker_id = uuid.uuid4()
    worker = Worker(worker_id)
    assert worker.id == worker_id
    assert worker.is_hydrated == False

def test_hydration():
    worker_id = uuid.uuid4()
    worker = Worker(worker_id)
    with requests_mock.mock() as m:
        m.get(worker.resource_url, text='{}')
        worker.fetch()
    assert worker.is_hydrated == True
