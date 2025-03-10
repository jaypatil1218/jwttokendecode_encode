from sqlalchemy import (
    Column,
    String,
    Integer
)

from app.models.BaseModel import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    signupid = Column(Integer, nullable=False)
    subscriptionname = Column(String, nullable=False)
    employeecode = Column(String, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    employeeid = Column(Integer, nullable=False)
