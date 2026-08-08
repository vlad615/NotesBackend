from pydantic import BaseModel
from typing import Generic, TypeVar
from v1.tasks.shemas import GetTasksResponse, DomainTask

T = TypeVar("T")


class FieldError(BaseModel):
    error: str
    field: str


class BaseResponse(BaseModel, Generic[T]):
    data: T
    resultCode: int
    messages: list[str]
    fieldsErrors: list[FieldError]
