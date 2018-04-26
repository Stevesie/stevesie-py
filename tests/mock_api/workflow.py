import pytest

@pytest.fixture
def workflow(workflow_task_json, workflow_parameter_json, workflow_task_dependency_json,
             workflow_maintainer_json):
    return {
        "id": "680e580a-6c0f-4325-b2a0-4bd610078798",
        "name": "Newsfeed",
        "description": "Access raw data.",
        "createdAt": "2017-12-03 12:46:27",
        "updatedAt": "2018-04-19 01:34:23",
        "slug": "data-newsfeed",
        "isPublic": True,
        "workflowTasks": [
            workflow_task_json
        ],
        "workflowTaskDependencies": [
            workflow_task_dependency_json
        ],
        "workflowParameters": [
            workflow_parameter_json
        ],
        "workflowMaintainers": [
            workflow_maintainer_json
        ]
    }
