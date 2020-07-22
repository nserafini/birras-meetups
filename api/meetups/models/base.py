from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()

def generate_uuid():
    return str(uuid4())

class BaseModel(Base):

    __abstract__ = True
    id = Column(String, primary_key=True, default=generate_uuid, unique=True)