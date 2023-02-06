from typing import Generic, Optional, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

DataType = TypeVar('DataType')

class PostBase(BaseModel):
    id: int
    title: str
    uri_picture: str | None
    uri_post: str
    posted: int
    parsed: int

    class Config:
        orm_mode = True


class IResponseBase(GenericModel, Generic[DataType]):
    result: Optional[DataType] = None
