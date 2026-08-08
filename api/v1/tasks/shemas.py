from pydantic import BaseModel
from enum import IntEnum
from datetime import datetime


class TaskStatus(IntEnum):
    Active = 0
    InProgress = 1
    Completed = 2
    Draft = 3


class TaskPriority(IntEnum):
    Low = 0
    Middle = 1
    Hi = 2
    Urgently = 3
    Later = 4


class CreateTaskModel(BaseModel):
    description: str | None
    title: str
    status: TaskStatus | None
    priority: TaskPriority | None
    startDate: datetime | None
    deadline: datetime | None


class UpdateTaskModel(CreateTaskModel):
    spendtime: datetime


class DomainTask(UpdateTaskModel):
    id: str
    todoListId: int
    order: int
    addedDate: datetime


class GetTasksResponse(BaseModel):
    error: str | None
    totalCount: int
    items: list[DomainTask]
