import os
# services
from api.services import users_services, doctors_services, comments_services
# schemas
from api.schemas.doctors_schemas import Doctor
from api.schemas.users_schemas import User
from api.schemas.comments_schemas import Comment
# database
from database import Base, engine, SessionLocal
# fastapi
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
# sqlalchemy
from sqlalchemy.orm import Session
# uvicorn
import uvicorn


# create dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# add cors enable
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info")
