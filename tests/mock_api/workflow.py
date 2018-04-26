import pytest

@pytest.fixture
def workflow(task_json):
    return {
      "id": "680e580a-6c0f-4325-b2a0-4bd610078798",
      "name": "Newsfeed",
      "description": "Access raw data.",
      "createdAt": "2017-12-03 12:46:27",
      "updatedAt": "2018-04-19 01:34:23",
      "slug": "data-newsfeed",
      "isPublic": True,
      "workflowTasks": [
        {
          "id": "83ca4ba0-73a6-49e9-99c8-71a0097fccd8",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "createdAt": "2017-12-03 12:46:27",
          "updatedAt": "2017-12-03 12:46:27",
          "task": task_json
        },
        {
          "id": "8f2ae7fd-0cd2-4d7b-b6bd-6a0577b9431a",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "taskId": "e1b13dc4-1365-41e9-96e0-dd1c3508113c",
          "createdAt": "2017-12-03 12:46:27",
          "updatedAt": "2017-12-03 12:46:27",
          "task": task_json
        }
      ],
      "workflowTaskDependencies": [
        {
          "id": "bbd5b079-929a-4718-9088-ddddec4b322b",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "taskDependencyId": "bb751dc7-df0f-4d74-a0bf-2528990490ff",
          "createdAt": "2017-12-03 12:46:27",
          "updatedAt": "2017-12-03 12:46:27",
          "workflowParameter": {
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
          },
          "workflowParameterId": "5a8eb55e-fcd4-4f47-8631-639073d582ce"
        },
        {
          "id": "14ec2f2f-6a34-40fc-874e-45682bf8041a",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "taskDependencyId": "4a1ef39c-f5fe-4350-8d64-ebefb9498f86",
          "createdAt": "2017-12-03 12:46:27",
          "updatedAt": "2017-12-03 12:46:27",
          "workflowParameter": {
            "id": "0155f71c-a833-435f-837d-d1e66c6a2548",
            "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
            "proxyFillTaskDependencyId": "4a1ef39c-f5fe-4350-8d64-ebefb9498f86",
            "fieldType": "string",
            "name": "Email",
            "description": "Email address to log in to your account",
            "createdAt": "2017-12-03 12:46:27",
            "updatedAt": "2018-03-21 01:03:40",
            "isSecure": False,
            "isRequired": True,
            "isIntercept": False,
            "isSampleDefault": False
          },
          "workflowParameterId": "0155f71c-a833-435f-837d-d1e66c6a2548"
        },
        {
          "id": "bde1dee6-881c-435c-8e08-4a1311c52ecc",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "taskDependencyId": "af2293a0-66c2-4e97-82fe-6f9594dd0b01",
          "createdAt": "2017-12-03 12:46:27",
          "updatedAt": "2017-12-03 12:46:27",
          "taskCollectionField": {
            "id": "6cd423d2-e045-4afe-8261-0ba920eb1a5f",
            "taskCollectionId": "52c3de1e-df17-491a-863e-dd588dc1de4a",
            "fieldName": "id_token",
            "fieldType": "string",
            "isPrimaryKey": False,
            "createdAt": "2017-11-27 04:26:47",
            "updatedAt": "2018-02-11 02:54:10"
          },
          "taskCollectionFieldId": "6cd423d2-e045-4afe-8261-0ba920eb1a5f"
        }
      ],
      "workflowParameters": [
        {
          "id": "0155f71c-a833-435f-837d-d1e66c6a2548",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "proxyFillTaskDependencyId": "4a1ef39c-f5fe-4350-8d64-ebefb9498f86",
          "fieldType": "string",
          "name": "Email",
          "description": "Email address to log in to your account",
          "createdAt": "2017-12-03 12:46:27",
          "updatedAt": "2018-03-21 01:03:40",
          "isSecure": False,
          "isRequired": True,
          "isIntercept": False,
          "isSampleDefault": False
        },
        {
          "id": "5a8eb55e-fcd4-4f47-8631-639073d582ce",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "proxyFillTaskDependencyId": "bb751dc7-df0f-4d74-a0bf-2528990490ff",
          "fieldType": "string",
          "name": "Nextdoor Password",
          "description": "Password for your account - keep this encrypted",
          "createdAt": "2017-12-03 12:46:27",
          "updatedAt": "2018-03-21 01:03:46",
          "isSecure": True,
          "isRequired": True,
          "isIntercept": False,
          "isSampleDefault": False
        }
      ],
      "workflowMaintainers": [
        {
          "id": "c911761b-56f2-4f38-a773-c7a38d926be8",
          "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
          "userId": "7601f0ab-6961-4d3c-8cfa-1eb4d39a1fc7",
          "isAdmin": True,
          "createdAt": "2018-04-18 12:36:58",
          "updatedAt": "2018-04-18 12:36:58",
          "username": "steve"
        }
      ]
    }
