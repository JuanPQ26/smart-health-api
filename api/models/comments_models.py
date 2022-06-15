# sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
# database
from database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    stars = Column(Integer)

    title = Column(String)
    body = Column(String)

    is_active = Column(Boolean, default=True)

    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    doctor = relationship("Doctor", back_populates="comments")
    user = relationship("User", back_populates="comments")
