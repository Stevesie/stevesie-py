import pytest

@pytest.fixture
def task_collection_result():
    return {
        "object" : {
            "classified" : [ {
                "price" : "0",
                "flagged" : False,
                "currency" : "USD",
                "description" : "Free boxes for moving and shipping.\nContact John.",
                "title" : "Free boxes for moving and shipping",
                "sold" : False,
                "id" : "90e76525-af09-4344-9911-937b7e622b02"
            } ],
            "id" : 1094794774283615870
        },
        "taskResultId" : "1d354b79-e218-406c-a1a8-638794dd6939",
        "collectedAt" : "2018-04-18 19:00:29"
    }
