from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from meetups.models.base import BaseModel

class MeetupUser(BaseModel):

    __tablename__ = "meetup_users"

    meetup_id = Column(Integer, ForeignKey("meetups.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    __table_args__ = (
        UniqueConstraint(
            "meetup_id", "user_id", name="meetup_users_rel"
        ),
    )
