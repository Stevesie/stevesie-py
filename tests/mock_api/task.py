import pytest

@pytest.fixture
def task(task_header_json):
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
        "app": {
          "id": "e43a024d-9e16-41ea-8d16-b8b0e8d88464",
          "name": "Nextdoor",
          "description": "Access your account programmatically.",
          "website": "https://test.com/",
          "slug": "test",
          "createdAt": "2016-06-30 02:08:06",
          "updatedAt": "2018-04-21 13:13:09",
          "isPublic": True,
          "iconUrl": "/assets/media/test.png"
        },
        "platform": {
          "id": "08560fdf-fd8a-4fa5-8eb3-361af615b146",
          "name": "iPhone",
          "createdAt": "2016-05-17 02:05:49",
          "updatedAt": "2016-06-03 01:24:18"
        },
        "taskDependencies": [
          {
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
          },
          {
            "id": "bb751dc7-df0f-4d74-a0bf-2528990490ff",
            "taskId": "3d47b479-bcd5-468d-8bad-f079cd3f820e",
            "variableName": "password",
            "name": "password",
            "description": "password",
            "sampleValue": "password",
            "createdAt": "2017-11-27 04:22:52",
            "updatedAt": "2017-11-27 04:22:52",
            "isSecure": True,
            "isIntercept": True,
            "isSampleDefault": False
          }
        ],
        "taskHeaders": [
          task_header_json
        ],
        "taskQueryParams": [],
        "taskCollections": [
          {
            "id": "52c3de1e-df17-491a-863e-dd588dc1de4a",
            "taskId": "3d47b479-bcd5-468d-8bad-f079cd3f820e",
            "collectionName": "access_token",
            "path": "./",
            "createdAt": "2017-11-27 04:26:47",
            "updatedAt": "2018-04-16 23:53:40",
            "isFeatured": True,
            "taskCollectionFields": [
              {
                "id": "6cd423d2-e045-4afe-8261-0ba920eb1a5f",
                "taskCollectionId": "52c3de1e-df17-491a-863e-dd588dc1de4a",
                "fieldName": "id_token",
                "fieldType": "string",
                "isPrimaryKey": False,
                "createdAt": "2017-11-27 04:26:47",
                "updatedAt": "2018-02-11 02:54:10"
              }
            ],
            "childTaskCollections": []
          }
        ]
      }
