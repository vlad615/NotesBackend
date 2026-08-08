from conf import client
from datetime import datetime
from api.v1.tasks.crud import tasks
from api.v1.tasks.shemas import TaskPriority, TaskStatus

base_url = lambda td: f"api/v1/todo-lists/{td}/tasks"


def test_get_tasks():
    print(base_url(1))
    response = client.get(base_url(1))
    assert response.status_code == 200


def test_create_task():
    task = {
        "description": "i want my wife to be happy",
        "title": "do this",
        "status": TaskStatus.InProgress,
        "priority": TaskPriority.Hi,
        "startDate": datetime.now().isoformat(),
        "deadline": datetime.now().isoformat(),
    }
    response = client.post(base_url(2), json=task)
    res_json = response.json()
    assert response.status_code == 201
    assert res_json["todoListId"] == 2
    for key, value in task.items():
        assert res_json[key] == value


def test_change_task():
    response = client.put(
        f"{base_url(1)}/1",
        json={
            "title": "hel",
            "priority": TaskPriority.Hi,
            "status": TaskStatus.InProgress,
            "description": "i want my wife to be happy",
            "startDate": datetime.now().isoformat(),
            "deadline": datetime.now().isoformat(),
            "spendtime": datetime.now().isoformat(),
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "hel"
    assert response.json()["todoListId"] == 1
    assert response.json()["id"] == "1"


def test_delete_task():
    response = client.delete(f"{base_url(1)}/1")
    res_get = client.get(base_url(1))

    assert response.status_code == 204
    assert len(res_get.json()) == 2


def test_delete_all_task():
    response = client.delete(base_url(1))
    res_get = client.get(base_url(1))

    assert response.status_code == 204
    assert len(res_get.json()) == 0
