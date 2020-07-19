from typing import List

from pydantic import BaseModel as BaseAPI
from pydantic import constr
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

from meetups.models.base import BaseModel

class User(BaseModel):

    __tablename__ = "users"

    name = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(128))
    meetups = relationship("Meetup", secondary="meetup_users")
    roles = relationship("Role", secondary="user_roles")

    def __init__(self, name, email, password):   
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def is_admin(self):   
        for role in self.roles:
            if role.name == 'admin':
                return True
        return False

class UserOUT(BaseAPI):
    id: constr(max_length=255)
    name: constr(max_length=255)
    email: constr(max_length=255)

    class Config:
        orm_mode = True