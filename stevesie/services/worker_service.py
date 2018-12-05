from stevesie.utils import api

from stevesie import Worker

def new_worker_from_task_id(task_id):
    resp_json, status_code = api.post(api.BASE_URL_PATH + 'workers', {
        'workUnitType': 'task',
        'workUnitId': task_id})

    return Worker().hydrate(resp_json)

def temp_worker_from_task_id(task_id):
    pass
