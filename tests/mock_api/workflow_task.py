import pytest

@pytest.fixture
def workflow_task(task_json):
    return {
        "id": "83ca4ba0-73a6-49e9-99c8-71a0097fccd8",
        "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
        "createdAt": "2017-12-03 12:46:27",
        "updatedAt": "2017-12-03 12:46:27",
        "task": task_json
    }
