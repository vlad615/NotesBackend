from fastapi import APIRouter
from fastapi import HTTPException
from datetime import datetime

router = APIRouter(prefix="/todolists")

todolists = [
    {"id": 1, "title": "To be happy", "addedDate": datetime.now(), "order": 0},
    {"id": 2, "title": "React", "addedDate": datetime.now(), "order": 1},
    {"id": 3, "title": "FastApi", "addedDate": datetime.now(), "order": 2},
]


@router.get("/")
def get_todolists():
    return todolists


@router.post("/")
def create_todolist(title: str):
    new_todolist = {
        "id": len(todolists) + 1,
        "title": title,
        "addedDate": datetime.now(),
        "order": len(todolists),
    }
    todolists.append(new_todolist)
    return new_todolist


@router.get("/{todolistId}")
def get_todolist(todolistId: int):
    for todolist in todolists:
        if todolist["id"] == todolistId:
            return todolist
    raise HTTPException(status_code=404, detail="To-Do list not found")


@router.put("/{todolistId}")
def change_todolist(todolistId: int, title: str):
    for todolist in todolists:
        if todolist["id"] == todolistId:
            todolist["title"] = title
            return todolist
    raise HTTPException(status_code=404, detail="To-Do list not found")
