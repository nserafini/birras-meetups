from datetime import datetime
from typing import List

from pydantic import BaseModel as BaseAPI
from pydantic import constr
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from meetups.models.base import BaseModel
from meetups.models.user import UserOUT

class Meetup(BaseModel):

    __tablename__ = "meetups"

    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)

    users = relationship("User", secondary="meetup_users")


class MeetupIN(BaseAPI):
    name: constr(max_length=255)
    description: constr(max_length=255)
    date: datetime
    users: List = []

class MeetupOUT(BaseAPI):
    id: constr(max_length=255)
    name: constr(max_length=255)
    description: constr(max_length=255)
    date: datetime
    users: List[UserOUT] = []

    class Config:
        orm_mode = True