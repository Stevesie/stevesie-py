import pytest

@pytest.fixture
def task_collection(task_collection_field_json):
    return {
        "id": "52c3de1e-df17-491a-863e-dd588dc1de4a",
        "taskId": "3d47b479-bcd5-468d-8bad-f079cd3f820e",
        "collectionName": "access_token",
        "path": "./",
        "createdAt": "2017-11-27 04:26:47",
        "updatedAt": "2018-04-16 23:53:40",
        "isFeatured": True,
        "taskCollectionFields": [
            task_collection_field_json
        ],
        "childTaskCollections": []
    }
