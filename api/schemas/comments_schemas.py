from pydantic import BaseModel


class CommentBase(BaseModel):
    stars: int
    title: str
    body: str
    doctor_id: int
    user_id: int


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True