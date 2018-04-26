import pytest

@pytest.fixture
def user_vault_entry():
    return {
        "id": "b488642b-c693-427c-a634-3665abc47030",
        "userId": "7601f0ab-6961-4d3c-8cfa-1eb4d39a1fc7",
        "entryName": "email-f961a8f5-8923-451d-993e-d9316b624822-1514464999349",
        "entryValue": "XXX",
        "secureNonce": "XXX",
        "createdAt": "2017-12-28 12:43:19",
        "updatedAt": "2018-04-18 23:06:05"
    }
