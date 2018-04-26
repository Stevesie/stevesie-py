import pytest

@pytest.fixture
def vault_entry(user_vault_entry_json):
    return {
      "id": "e6c5011c-eed5-4340-93b3-a4aa910179f2",
      "userWorkflowId": "f961a8f5-8923-451d-993e-d9316b624822",
      "workflowParameterId": "0155f71c-a833-435f-837d-d1e66c6a2548",
      "userVaultEntryId": "b488642b-c693-427c-a634-3665abc47030",
      "createdAt": "2018-03-21 00:47:27",
      "updatedAt": "2018-03-21 00:47:27",
      "userVaultEntry": user_vault_entry_json
    }
