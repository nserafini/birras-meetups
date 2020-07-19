from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from meetups.core.config import settings


def get_engine(dsn: str):
    return create_engine(dsn)

def get_maker(dsn: str):
    return sessionmaker(autocommit=False, autoflush=False, bind=get_engine(dsn))

@contextmanager
def get_session(dsn: str):
    try:
        maker = get_maker(dsn)
        session = maker()
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

def db():
    with get_session(settings.DSN) as session:
        yield session