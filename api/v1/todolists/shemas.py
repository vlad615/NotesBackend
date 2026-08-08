from pydantic import BaseModel
from datetime import datetime


class TitleTodolist(BaseModel):
    title: str


class TodoList(TitleTodolist):
    id: int
    addedDate: datetime
    color: str
    order: int
