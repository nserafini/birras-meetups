from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from meetups.models.base import BaseModel
from sqlalchemy import String

class MeetupUser(BaseModel):

    __tablename__ = "meetup_users"

    meetup_id = Column(String, ForeignKey("meetups.id"))
    user_id = Column(String, ForeignKey("users.id"))

    __table_args__ = (
        UniqueConstraint(
            "meetup_id", "user_id", name="meetup_users_rel"
        ),
    )
