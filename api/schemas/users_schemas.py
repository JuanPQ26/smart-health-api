from pydantic import BaseModel
# schemas
from api.schemas.comments_schemas import Comment


class UserBase(BaseModel):
    fullname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: str
    comments: list[Comment] = []

    class Config:
        orm_mode = True