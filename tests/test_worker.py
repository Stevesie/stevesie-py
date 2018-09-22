import uuid
import tempfile
import json

from stevesie import Worker

WORKER_ID = str(uuid.uuid4())

def test_init():
    worker = Worker(WORKER_ID)
    assert worker.id == WORKER_ID
    assert not worker.is_hydrated

def test_hydration(mock_api):
    worker = Worker(WORKER_ID)
    with mock_api:
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

def test_fetch_results(mock_api):
    worker = Worker(WORKER_ID)
    with mock_api:
        collection_results = worker.fetch_results()

    assert not worker.is_hydrated
    assert collection_results

def test_run_worker(mock_api):
    worker = Worker(WORKER_ID)
    with mock_api:
        run_result = worker.fetch().run()

    assert run_result
