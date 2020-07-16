from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from meetups.models.base import BaseModel

class Meetup(BaseModel):

    __tablename__ = "meetups"

    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)

    users = relationship("User", secondary="meetup_users")
