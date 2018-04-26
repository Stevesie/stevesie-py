import uuid
import tempfile
import json

import requests_mock

from stevesie.worker import Worker

def test_init():
    worker_id = uuid.uuid4()
    worker = Worker(worker_id)
    assert worker.id == worker_id
    assert not worker.is_hydrated

def test_hydration(worker_json):
    worker_id = uuid.uuid4()
    worker = Worker(worker_id)

    with requests_mock.mock() as mock:
        mock.get(worker.resource_url, json={'item': worker_json})
        worker = worker.fetch()

    assert worker.is_hydrated
    assert worker.name == 'My custom worker!'

    with tempfile.NamedTemporaryFile() as temp_file:
        worker.save_to_file(temp_file.name)
        loaded_json = json.load(temp_file)
        assert loaded_json['name'] == 'My custom worker!'
        assert loaded_json['workflow']['name'] == 'Newsfeed'
        assert loaded_json['workflow']['workflow_tasks'][0]['id'] == \
            '83ca4ba0-73a6-49e9-99c8-71a0097fccd8'
