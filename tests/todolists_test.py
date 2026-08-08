from conf import client
from datetime import datetime
from api.v1.todolists.crud import todolists

base_url = "/api/v1/todo-lists"


def test_get_todolists():
    response = client.get(base_url)

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_todolist():
    response = client.get(f"{base_url}/3")
    res_json = response.json()
    addedDate = res_json.pop("addedDate")

    assert response.status_code == 200
    assert type(addedDate) == str
    assert datetime.fromisoformat(addedDate)
    assert res_json == {
        "id": 3,
        "title": "FastApi",
        "color": "primery",
        "order": 2,
    }


def test_create_todolist():
    response = client.post(f"{base_url}/", json={"title": "hello"})

    assert response.status_code == 201
    assert response.json()["title"] == "hello"
    assert response.json()["id"] == 4


def test_change_todolist():
    response = client.put(
        f"{base_url}/4", json={"title": "hel", "color": "primery", "order": 2, "id": 4}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "hel"
    assert response.json()["id"] == 4


def test_delete_todolist():
    response = client.delete(f"{base_url}/4")
    res_get = client.get(f"{base_url}/")

    assert response.status_code == 204
    assert len(res_get.json()) == 3
    assert len(res_get.json()) == 3
