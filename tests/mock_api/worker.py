import pytest


@pytest.fixture
def worker(workflow_json):
    return {
        "id": "f961a8f5-8923-451d-993e-d9316b624822",
        "name": "My custom worker!",
        "userId": "7601f0ab-6961-4d3c-8cfa-1eb4d39a1fc7",
        "workflowId": "680e580a-6c0f-4325-b2a0-4bd610078798",
        "createdAt": "2017-12-28 12:42:57",
        "updatedAt": "2018-03-21 00:49:57",
        "workflow": workflow_json,
        "vaultEntries": [
          {
            "id": "e6c5011c-eed5-4340-93b3-a4aa910179f2",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "workflowParameterId": "0155f71c-a833-435f-837d-d1e66c6a2548",
            "userVaultEntryId": "b488642b-c693-427c-a634-3665abc47030",
            "createdAt": "2018-03-21 00:47:27",
            "updatedAt": "2018-03-21 00:47:27",
            "userVaultEntry": {
              "id": "b488642b-c693-427c-a634-3665abc47030",
              "userId": "7601f0ab-6961-4d3c-8cfa-1eb4d39a1fc7",
              "entryName": "email-f961a8f5-8923-451d-993e-d9316b624822-1514464999349",
              "entryValue": "XXX",
              "secureNonce": "XXX",
              "createdAt": "2017-12-28 12:43:19",
              "updatedAt": "2018-04-18 23:06:05"
            }
          },
          {
            "id": "d3661ae9-31f6-4e57-85d4-a84d3061d364",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "workflowParameterId": "5a8eb55e-fcd4-4f47-8631-639073d582ce",
            "userVaultEntryId": "09b5aeb6-b5c0-49a9-b3ab-e931d8a53939",
            "createdAt": "2018-03-21 00:47:35",
            "updatedAt": "2018-03-21 00:47:35",
            "userVaultEntry": {
              "id": "09b5aeb6-b5c0-49a9-b3ab-e931d8a53939",
              "userId": "7601f0ab-6961-4d3c-8cfa-1eb4d39a1fc7",
              "entryName": "password-f961a8f5-8923-451d-993e-d9316b624822-1514465040537",
              "entryValue": "XXX",
              "secureNonce": "XXX",
              "createdAt": "2017-12-28 12:44:01",
              "updatedAt": "2018-04-18 23:06:05"
            }
          }
        ],
        "workSchedules": [],
        "workExtractions": [
          {
            "id": "121e2410-7aac-4735-9c51-e6754a8c78fd",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "taskCollectionFieldId": "cf2dc0ff-bd8d-4106-9ebd-098213efd9b2",
            "createdAt": "2017-12-28 12:45:53",
            "updatedAt": "2017-12-28 12:45:53",
            "taskCollectionField": {
              "id": "cf2dc0ff-bd8d-4106-9ebd-098213efd9b2",
              "taskCollectionId": "e5d9d62e-9fe6-432d-974f-33ecd5d4b03f",
              "fieldName": "creation_date",
              "fieldType": "epoch",
              "sampleValue": "1491000920",
              "isPrimaryKey": False,
              "isRequired": False,
              "isDefaultExtraction": True,
              "createdAt": "2017-04-01 17:10:45",
              "updatedAt": "2017-04-01 17:10:45"
            }
          },
          {
            "id": "526a2523-528d-42b5-844b-30709bdaa1b9",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "taskCollectionFieldId": "33edf9e6-1464-496a-af6a-0ce91fb0f368",
            "createdAt": "2017-12-28 12:45:53",
            "updatedAt": "2017-12-28 12:45:53",
            "taskCollectionField": {
              "id": "33edf9e6-1464-496a-af6a-0ce91fb0f368",
              "taskCollectionId": "e5d9d62e-9fe6-432d-974f-33ecd5d4b03f",
              "fieldName": "id",
              "fieldType": "number",
              "sampleValue": "4677204932",
              "isPrimaryKey": True,
              "isRequired": True,
              "isDefaultExtraction": True,
              "createdAt": "2017-04-01 17:11:54",
              "updatedAt": "2017-04-01 17:11:54"
            }
          },
          {
            "id": "297086c9-d7d4-4fb8-b1d0-018691838f92",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "taskCollectionFieldId": "89b80a85-04b7-4b86-aaab-be970ca93820",
            "createdAt": "2017-12-28 12:45:53",
            "updatedAt": "2017-12-28 12:45:53",
            "taskCollectionField": {
              "id": "89b80a85-04b7-4b86-aaab-be970ca93820",
              "taskCollectionId": "075e1114-02f0-46ac-bd59-9720cd7cec86",
              "fieldName": "body",
              "fieldType": "text",
              "sampleValue": "This is the best comment ever!",
              "isPrimaryKey": False,
              "isRequired": False,
              "isDefaultExtraction": True,
              "createdAt": "2017-04-01 17:16:40",
              "updatedAt": "2017-04-01 17:16:40"
            }
          },
          {
            "id": "051bbe50-7e55-48a2-ac65-6496442a93ea",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "taskCollectionFieldId": "1f5e3ada-9212-4cb9-889f-7fdfd6ae8ac1",
            "createdAt": "2017-12-28 12:45:53",
            "updatedAt": "2017-12-28 12:45:53",
            "taskCollectionField": {
              "id": "1f5e3ada-9212-4cb9-889f-7fdfd6ae8ac1",
              "taskCollectionId": "075e1114-02f0-46ac-bd59-9720cd7cec86",
              "fieldName": "id",
              "fieldType": "number",
              "sampleValue": "92366080",
              "isPrimaryKey": True,
              "isRequired": True,
              "isDefaultExtraction": True,
              "createdAt": "2017-04-01 17:18:37",
              "updatedAt": "2017-04-01 17:18:37"
            }
          },
          {
            "id": "ada8661a-7281-4081-83d4-3851258ce7c9",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "taskCollectionFieldId": "b825d14e-3645-4f97-87d1-98fcee69e4f6",
            "createdAt": "2018-03-21 01:30:12",
            "updatedAt": "2018-03-21 01:30:12",
            "taskCollectionField": {
              "id": "b825d14e-3645-4f97-87d1-98fcee69e4f6",
              "taskCollectionId": "58e626f7-4e95-4e96-a067-d19c06eb3306",
              "fieldName": "name",
              "fieldType": "string",
              "isPrimaryKey": False,
              "isRequired": False,
              "isDefaultExtraction": True,
              "createdAt": "2018-03-21 01:29:22",
              "updatedAt": "2018-03-21 01:29:22"
            }
          },
          {
            "id": "cb996d9a-a8b8-442d-9e2e-010e5e65e3ff",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "taskCollectionFieldId": "8f8f9da2-0af4-461a-b604-476f7c6f3758",
            "createdAt": "2018-03-21 01:30:12",
            "updatedAt": "2018-03-21 01:30:12",
            "taskCollectionField": {
              "id": "8f8f9da2-0af4-461a-b604-476f7c6f3758",
              "taskCollectionId": "58e626f7-4e95-4e96-a067-d19c06eb3306",
              "fieldName": "photo_url",
              "fieldType": "image",
              "isPrimaryKey": False,
              "isRequired": False,
              "isDefaultExtraction": True,
              "createdAt": "2018-03-21 01:29:39",
              "updatedAt": "2018-03-21 01:29:39"
            }
          },
          {
            "id": "df30c15f-8525-4f41-9973-ac340284f709",
            "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
            "taskCollectionFieldId": "d5f8bfea-72f2-4edf-9653-ef244529af07",
            "createdAt": "2018-03-21 01:30:12",
            "updatedAt": "2018-03-21 01:30:12",
            "taskCollectionField": {
              "id": "d5f8bfea-72f2-4edf-9653-ef244529af07",
              "taskCollectionId": "58e626f7-4e95-4e96-a067-d19c06eb3306",
              "fieldName": "../id",
              "fieldType": "number",
              "isPrimaryKey": True,
              "isRequired": True,
              "isDefaultExtraction": True,
              "createdAt": "2018-03-21 01:28:51",
              "updatedAt": "2018-03-21 01:34:26"
            }
          }
        ]
    }
