import pytest

@pytest.fixture
def work_extraction(task_collection_field_json):
    return {
        "id": "121e2410-7aac-4735-9c51-e6754a8c78fd",
        "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
        "taskCollectionFieldId": "cf2dc0ff-bd8d-4106-9ebd-098213efd9b2",
        "createdAt": "2017-12-28 12:45:53",
        "updatedAt": "2017-12-28 12:45:53",
        "taskCollectionField": task_collection_field_json
    }
