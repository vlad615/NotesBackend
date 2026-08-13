from pydantic import BaseModel, Field
from datetime import datetime


class BaseTodolist(BaseModel):
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    color: str | None = None


class CreateTodolist(BaseTodolist):
    title: str = Field(min_length=1, max_length=100)


class UpdateTodolist(BaseTodolist):
    title: str | None = Field(default=None, min_length=1, max_length=100)


class TodoListResponse(BaseModel):
    id: int
    title: str
    color: str
    order: int
    addedDate: datetime
    description: str
