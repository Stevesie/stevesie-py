import pytest

@pytest.fixture
def worker_collection_result(task_collection_result_json):
    return {
        "taskCollectionId" : "e5d9d62e-9fe6-432d-974f-33ecd5d4b03f",
        "workerId" : "f961a8f5-8923-451d-993e-d9316b624822",
        "taskCollectionResults" : [ task_collection_result_json ],
        "total" : 157
    }
