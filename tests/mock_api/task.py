import pytest

@pytest.fixture
def task(app_json, platform_json, task_dependency_json, task_header_json, task_collection_json):
    return {
        "id": "3d47b479-bcd5-468d-8bad-f079cd3f820e",
        "method": "POST",
        "scheme": "https",
        "host": "auth.test.com",
        "port": 443,
        "path": "/v1/auth",
        "body": "username={{email}}&password={{password}}&grant_type=password",
        "name": "Log In",
        "slug": "login",
        "description": "Log in with your email address and password.",
        "createdAt": "2017-11-27 04:22:52",
        "updatedAt": "2018-04-15 21:51:45",
        "isPublic": True,
        "app": app_json,
        "platform": platform_json,
        "taskDependencies": [
            task_dependency_json
        ],
        "taskHeaders": [
            task_header_json
        ],
        "taskQueryParams": [],
        "taskCollections": [
            task_collection_json
        ]
    }
