from pytest import fixture
from sqlalchemy.orm import Session

from meetups.core.config import settings
from meetups.core.database import get_engine
from meetups.core.database import get_session

from meetups.models.base import BaseModel
from meetups.models.meetup import Meetup
from meetups.models.user import User
from meetups.models.meetup_user import MeetupUser
from meetups.models.role import Role
from meetups.models.user_role import UserRole


@fixture(scope="session")
def dsn():
    return "sqlite://///app/source/tests/meetups_test.db?check_same_thread=False"


@fixture
def renew_db(dsn):
    engine = get_engine(dsn)
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


@fixture
def db_session(dsn, renew_db):
    with get_session(dsn) as session:
        yield session