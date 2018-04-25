import os
import pytest

@pytest.fixture
def worker_json():
    json_response_filename = os.path.join(os.path.dirname(__file__), 'mock_api_resources/worker.json')
    with open(json_response_filename) as f:
        return f.read()
