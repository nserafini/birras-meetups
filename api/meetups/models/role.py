from pydantic import BaseModel as BaseAPI
from pydantic import constr

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from meetups.models.base import BaseModel

class Role(BaseModel):

    __tablename__ = "roles"

    name = Column(String(255), unique=True, nullable=False)

class RoleOUT(BaseAPI):
    id: constr(max_length=255)
    name: constr(max_length=255)

    class Config:
        orm_mode = True