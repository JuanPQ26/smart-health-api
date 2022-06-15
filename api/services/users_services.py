# schemas
from api.schemas.users_schemas import UserCreate
# models
from api.models.users_models import User
# sqlalchemy
from sqlalchemy.orm import Session


def get_users(db: Session, skip=0, limit=100):
    return db.query(User).offset(skip).limit(limit).all()
