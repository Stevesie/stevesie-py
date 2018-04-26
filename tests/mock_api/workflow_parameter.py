import pytest

@pytest.fixture
def workflow_parameter():
    return {
        "id": "5a8eb55e-fcd4-4f47-8631-639073d582ce",
        "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
        "proxyFillTaskDependencyId": "bb751dc7-df0f-4d74-a0bf-2528990490ff",
        "fieldType": "string",
        "name": "Password",
        "description": "Password for your account - keep this encrypted",
        "createdAt": "2017-12-03 12:46:27",
        "updatedAt": "2018-03-21 01:03:46",
        "isSecure": True,
        "isRequired": True,
        "isIntercept": False,
        "isSampleDefault": False
    }
