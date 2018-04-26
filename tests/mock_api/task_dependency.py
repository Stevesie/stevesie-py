import pytest

@pytest.fixture
def task_dependency():
    return {
        "id": "4a1ef39c-f5fe-4350-8d64-ebefb9498f86",
        "taskId": "3d47b479-bcd5-468d-8bad-f079cd3f820e",
        "variableName": "email",
        "name": "email",
        "description": "email",
        "sampleValue": "email",
        "createdAt": "2017-11-27 04:22:52",
        "updatedAt": "2017-11-27 04:22:52",
        "isSecure": False,
        "isIntercept": True,
        "isSampleDefault": False
    }
