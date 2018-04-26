import pytest

@pytest.fixture
def worker(workflow_json, vault_entry_json, work_extraction_json):
    return {
        "id": "f961a8f5-8923-451d-993e-d9316b624822",
        "name": "My custom worker!",
        "userId": "7601f0ab-6961-4d3c-8cfa-1eb4d39a1fc7",
        "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
        "createdAt": "2017-12-28 12:42:57",
        "updatedAt": "2018-03-21 00:49:57",
        "workflow": workflow_json,
        "vaultEntries": [
            vault_entry_json
        ],
        "workSchedules": [],
        "workExtractions": [
            work_extraction_json
        ]
    }
