from datetime import datetime

tasks = {
    1: [
        {
            "id": "1",
            "todoListId": 1,
            "order": 0,
            "addedDate": datetime.now(),
            "description": "love my wife",
            "title": "<3",
            "status": 0,
            "priority": 1,
            "startDate": datetime.now(),
            "deadline": datetime.now(),
            "spendtime": datetime.now(),
        },
        {
            "id": "2",
            "todoListId": 1,
            "order": 0,
            "addedDate": datetime.now(),
            "description": "make happy",
            "title": "give",
            "status": 0,
            "priority": 2,
            "startDate": datetime.now(),
            "deadline": datetime.now(),
            "spendtime": datetime.now(),
        },
        {
            "id": "3",
            "todoListId": 1,
            "order": 0,
            "addedDate": datetime.now(),
            "description": "just be",
            "title": "be",
            "status": 0,
            "priority": 2,
            "startDate": datetime.now(),
            "deadline": datetime.now(),
            "spendtime": datetime.now(),
        },
    ],
    2: [
        {
            "id": "1",
            "todoListId": 2,
            "order": 0,
            "addedDate": datetime.now(),
            "description": "do ...",
            "title": "change styles",
            "status": 0,
            "priority": 1,
            "startDate": datetime.now(),
            "deadline": datetime.now(),
            "spendtime": datetime.now(),
        },
        {
            "id": "2",
            "todoListId": 2,
            "order": 0,
            "addedDate": datetime.now(),
            "description": "make happy",
            "title": "give",
            "status": 0,
            "priority": 2,
            "startDate": datetime.now(),
            "deadline": datetime.now(),
            "spendtime": datetime.now(),
        },
    ],
    3: [
        {
            "id": "1",
            "todoListId": 3,
            "order": 0,
            "addedDate": datetime.now(),
            "description": "make tests for tasks",
            "title": "tests",
            "status": 1,
            "priority": 3,
            "startDate": datetime.now(),
            "deadline": datetime.now(),
            "spendtime": datetime.now(),
        },
        {
            "id": "2",
            "todoListId": 3,
            "order": 0,
            "addedDate": datetime.now(),
            "description": "give current response",
            "title": "give response",
            "status": 0,
            "priority": 2,
            "startDate": datetime.now(),
            "deadline": datetime.now(),
            "spendtime": datetime.now(),
        },
    ],
}


def get_tasks(todolistId: int):
    return tasks.get(todolistId, 0)


def create_task(todolistId: int, task: dict):
    todolist = tasks.get(todolistId, 0)
    if todolist:
        new_id = int(todolist[-1]["id"]) + 1
        task = {
            "description": task.description,
            "title": task.title,
            "status": task.status,
            "priority": task.priority,
            "startDate": task.startDate,
            "deadline": task.deadline,
            "spendtime": 0,
            "id": str(new_id),
            "todoListId": todolistId,
            "order": 1,
            "addedDate": datetime.now(),
        }
        todolist.append(task)
        return task
    return None


def change_task(todolistId: int, taskId: int, task: dict):
    todolist = tasks.get(todolistId, 0)
    if not todolist:
        return (0, "Todo List not found")

    for t in todolist:
        if t["id"] == taskId:
            t.update(task)
            return t
    return (0, "Todo List not found")


def delete_task(todolistId: int, taskId: int):
    todolist = tasks.get(todolistId, 0)
    if not todolist:
        return (0, "Todo List not found")

    for index, task in enumerate(todolist):
        if task["id"] == taskId:
            del todolist[index]
            return (1, "task was delete")
    return (0, "Todo List not found")


def delete_all_tasks(todolistId):
    todolist = tasks.get(todolistId, 0)
    if not todolist:
        return (0, "Todo List not found")

    tasks[todolistId] = []
    return (1, "tasks was delete")
