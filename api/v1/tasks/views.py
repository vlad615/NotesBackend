from fastapi import APIRouter
from fastapi import HTTPException
from .crud import (
    get_tasks as get_Tk,
    create_task as create_Tk,
    change_task,
    delete_task as del_Tk,
    delete_all_tasks,
)
from .shemas import CreateTaskModel, UpdateTaskModel, DomainTask

router = APIRouter(prefix="/todo-lists/{todolistId}/tasks", tags=["Tasks of Todo"])


@router.get("/", response_model=list[DomainTask])
def get_tasks(todolistId: int):
    tasks = get_Tk(todolistId)
    if tasks == 0:
        raise HTTPException(status_code=404, detail="Todo List Not Found")
    return tasks


@router.post("/", status_code=201, response_model=DomainTask)
def create_task(todolistId: int, task: CreateTaskModel):
    task = create_Tk(todolistId, task)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Todo List Not Found")


@router.put("/{taskId}", response_model=DomainTask)
def update_task(todolistId: int, taskId: str, task: UpdateTaskModel):
    task = change_task(todolistId, taskId, task)
    if type(task) != "tuple":
        return task
    raise HTTPException(status_code=404, detail=task[1])


@router.delete("/{taskId}", status_code=204)
def delete_task(todolistId: int, taskId: str):
    task = del_Tk(todolistId, taskId)
    if task[0]:
        return {"resultCode": task[0], "message": task[1]}
    raise HTTPException(status_code=404, detail=task[1])


@router.delete("/", status_code=204)
def delete_tasks(todolistId: int):
    task = delete_all_tasks(todolistId)
    if task[0]:
        return {"resultCode": task[0], "message": task[1]}
    raise HTTPException(status_code=404, detail=task[1])
