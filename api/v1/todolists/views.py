from fastapi import APIRouter
from fastapi import HTTPException
from .shemas import TodoListResponse, CreateTodolist, UpdateTodolist
from settings import settings
from .crud import (
    get_todolist as getTC,
    create_todolist as createTC,
    change_todolist as changeTC,
    get_todolists as getTCs,
    delete_todolist as deleteTC,
)

router = APIRouter(prefix="/todo-lists", tags=["Todo Lists"])


@router.post("/", status_code=201, response_model=TodoListResponse)
def create_todolist(t: CreateTodolist):
    return createTC(t.title)


@router.get("/", response_model=list[TodoListResponse])
def get_todolists():
    return getTCs()


@router.get("/{todolistId}", response_model=TodoListResponse)
def get_todolist(todolistId: int):
    todolist = getTC(todolistId)
    if todolist:
        return todolist
    raise HTTPException(status_code=404, detail="To-Do list not found")


@router.put("/{todolistId}", response_model=TodoListResponse)
def change_todolist(todolistId: int, t: UpdateTodolist):
    todolist = changeTC(todolistId, t.title)
    if todolist:
        return todolist
    raise HTTPException(status_code=404, detail="To-Do list not found")


@router.delete("/{todolistId}", status_code=204)
def delete_todolist(todolistId: int):
    todolist = deleteTC(todolistId)
    if not todolist:
        raise HTTPException(status_code=404, detail="To-Do list not found")
