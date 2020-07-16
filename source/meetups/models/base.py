from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):

    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)