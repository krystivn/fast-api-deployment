from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class NoteCreate(BaseModel):
    name: str
    description: str


class ResponseSchema(BaseModel, Generic[T]):
    detail: str
    result: Optional[T] = None