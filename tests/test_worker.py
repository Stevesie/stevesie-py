import os
import uuid
import pytest
import tempfile
import json

import requests_mock

from stevesie.worker import Worker

# from tests.mock_api.worker import worker as worker_json


def test_init():
    worker_id = uuid.uuid4()
    worker = Worker(worker_id)
    assert worker.id == worker_id
    assert worker.is_hydrated == False

def test_hydration(worker_json):
    worker_id = uuid.uuid4()
    worker = Worker(worker_id)

    with requests_mock.mock() as m:
        m.get(worker.resource_url, json={'item': worker_json})
        worker = worker.fetch()
    
    assert worker.is_hydrated == True
    assert worker.name == 'My custom worker!'

    with tempfile.NamedTemporaryFile() as tf:
        worker.save_to_file(tf.name)
        loaded_json = json.load(tf)
        assert loaded_json['name'] == 'My custom worker!'
        assert loaded_json['workflow']['name'] == 'Newsfeed'
        assert loaded_json['workflow']['workflow_tasks'][0]['id'] == '83ca4ba0-73a6-49e9-99c8-71a0097fccd8'
