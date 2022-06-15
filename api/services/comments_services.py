# schemas
from api.schemas.comments_schemas import CommentCreate
# models
from api.models.comments_models import Comment
# sqlalchemy
from sqlalchemy.orm import Session


def get_comments(db: Session, skip=0, limit=100):
    return db.query(Comment).offset(skip).limit(limit).all()
