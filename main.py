# services
from api.services import users_services
from api.services import doctors_services
from api.services import comments_services
# schemas
from api.schemas.doctors_schemas import Doctor
from api.schemas.users_schemas import User
from api.schemas.comments_schemas import Comment
# database
from database import Base, engine, SessionLocal
# fastapi
from fastapi import FastAPI, Depends
# sqlalchemy
from sqlalchemy.orm import Session


# create dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# create all tables in database
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/v1/doctors", response_model=list[Doctor])
def get_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return doctors_services.get_doctors(db, skip, limit)


@app.get("/v1/users", response_model=list[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return users_services.get_users(db, skip, limit)


@app.get("/v1/comments", response_model=list[Comment])
def get_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return comments_services.get_comments(db, skip, limit)
