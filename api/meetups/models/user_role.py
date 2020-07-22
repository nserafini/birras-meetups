from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from meetups.models.base import BaseModel
from sqlalchemy import String

class UserRole(BaseModel):

    __tablename__ = "user_roles"

    user_id = Column(String, ForeignKey("users.id"))
    role_id = Column(String, ForeignKey("roles.id"))

    __table_args__ = (
        UniqueConstraint(
            "user_id", "role_id", name="user_roles_rel"
        ),
    )
