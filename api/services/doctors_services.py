# schemas
from api.schemas.doctors_schemas import DoctorCreate, Doctor
# models
from api.models.doctors_models import Doctor
# sqlalchemy
from sqlalchemy.orm import Session


def get_doctors(db: Session, skip=0, limit=100) -> Doctor:
    return db.query(Doctor).offset(skip).limit(limit).all()
