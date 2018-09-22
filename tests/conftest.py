import os
import re

import pytest

import requests_mock

from tests.mock_api.app import app as app_json
from tests.mock_api.platform import platform as platform_json

from tests.mock_api.task_dependency import task_dependency as task_dependency_json
from tests.mock_api.task_header import task_header as task_header_json

from tests.mock_api.task_collection_field import task_collection_field as task_collection_field_json
from tests.mock_api.task_collection import task_collection as task_collection_json

from tests.mock_api.task import task as task_json

from tests.mock_api.workflow_maintainer import workflow_maintainer as workflow_maintainer_json
from tests.mock_api.workflow_task import workflow_task as workflow_task_json
from tests.mock_api.workflow_parameter import workflow_parameter as workflow_parameter_json
from tests.mock_api.workflow_task_dependency import workflow_task_dependency \
    as workflow_task_dependency_json

from tests.mock_api.workflow import workflow as workflow_json

from tests.mock_api.user_vault_entry import user_vault_entry as user_vault_entry_json
from tests.mock_api.vault_entry import vault_entry as vault_entry_json
from tests.mock_api.work_extraction import work_extraction as work_extraction_json

from tests.mock_api.worker import worker as worker_json

from tests.mock_api.task_collection_result import task_collection_result \
    as task_collection_result_json
from tests.mock_api.worker_collection_result import worker_collection_result \
    as worker_collection_result_json

os.environ['STEVESIE_CONFIG_FILE'] = 'stevesie.test.cfg'

UUID_REGEX = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

@pytest.fixture
def mock_api(worker_json, worker_collection_result_json):
    mock = requests_mock.mock()

    mock.get(re.compile('/api/v1/workers/' + UUID_REGEX), json={'item': worker_json})
    mock.get(
        re.compile('/api/v1/workers/' + UUID_REGEX + '/collection-results'),
        json={'items': [worker_collection_result_json]})
    mock.get(
        re.compile('/api/v1/workers/' + UUID_REGEX + \
            '/collection-results\?taskCollectionId=' + UUID_REGEX + '&offset=\d+'),
        json={'item': worker_collection_result_json})
    mock.post(
        re.compile('/api/v1/workers/' + UUID_REGEX + \
            '/runs'),
        json={'item': {'taskResults': []}})

    return mock
