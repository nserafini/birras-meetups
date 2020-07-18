from typing import List

from pydantic import BaseModel as BaseAPI
from pydantic import constr
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from meetups.models.base import BaseModel

class User(BaseModel):

    __tablename__ = "users"

    name = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(128))

    roles = relationship("Role", secondary="user_roles")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserOUT(BaseAPI):
    id: constr(max_length=255)
    name: constr(max_length=255)
    email: constr(max_length=255)

    class Config:
        orm_mode = True