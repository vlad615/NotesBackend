from pydantic import BaseModel, Field
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


class BaseTaskModel(BaseModel):
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    startDate: datetime | None = None
    deadline: datetime | None = None


class CreateTaskModel(BaseTaskModel):
    title: str
    status: TaskStatus = TaskStatus.Active
    priority: TaskPriority = TaskPriority.Low


class UpdateTaskModel(BaseTaskModel):
    spendtime_minutes: int = 0
    status: TaskStatus | None = None
    priority: TaskPriority | None = None


class DomainTask(UpdateTaskModel):
    id: str
    todoListId: int
    order: int
    addedDate: datetime


class GetTasksResponse(BaseModel):
    error: str | None
    totalCount: int
    items: list[DomainTask]
