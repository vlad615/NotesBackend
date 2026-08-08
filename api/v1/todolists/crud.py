from datetime import datetime

todolists = [
    {
        "id": 1,
        "title": "To be happy",
        "addedDate": datetime.now(),
        "order": 0,
        "color": "primery",
    },
    {
        "id": 2,
        "title": "React",
        "addedDate": datetime.now(),
        "order": 1,
        "color": "primery",
    },
    {
        "id": 3,
        "title": "FastApi",
        "addedDate": datetime.now(),
        "order": 2,
        "color": "primery",
    },
]


def get_todolists():
    return todolists


def create_todolist(title: str):
    new_todolist = {
        "id": todolists[-1]["id"] + 1,
        "title": title,
        "addedDate": datetime.now(),
        "order": len(todolists),
        "color": "primery",
    }
    todolists.append(new_todolist)
    return new_todolist


def get_todolist(todolistId: int):
    for todolist in todolists:
        if todolist["id"] == todolistId:
            return todolist
    return None


def change_todolist(todolistId: int, title: str):
    for todolist in todolists:
        if todolist["id"] == todolistId:
            todolist["title"] = title
            return todolist
    return None


def delete_todolist(todolistId: int):
    for index, todolist in enumerate(todolists):
        if todolist["id"] == todolistId:
            del todolists[index]
            return 1
    return 0
