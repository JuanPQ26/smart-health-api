# sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
# database
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    comments = relationship("Comment", back_populates="user")
