from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from meetups.models.base import BaseModel

class Role(BaseModel):

    __tablename__ = "roles"

    name = Column(String(255), unique=True, nullable=False)
    users = relationship("User", secondary="user_roles")