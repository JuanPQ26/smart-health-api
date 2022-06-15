from pydantic import BaseModel
# schemas
from api.schemas.comments_schemas import Comment


class DoctorBase(BaseModel):
    fullname: str
    email: str


class DoctorCreate(DoctorBase):
    password: str


class Doctor(DoctorBase):
    id: int
    is_active: str
    comments: list[Comment] = []

    class Config:
        orm_mode = True