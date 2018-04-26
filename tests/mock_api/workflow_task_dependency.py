import pytest

@pytest.fixture
def workflow_task_dependency(workflow_parameter_json):
    return {
      "id": "bbd5b079-929a-4718-9088-ddddec4b322b",
      "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
      "taskDependencyId": "bb751dc7-df0f-4d74-a0bf-2528990490ff",
      "createdAt": "2017-12-03 12:46:27",
      "updatedAt": "2017-12-03 12:46:27",
      "workflowParameter": workflow_parameter_json,
      "workflowParameterId": "5a8eb55e-fcd4-4f47-8631-639073d582ce"
    }
