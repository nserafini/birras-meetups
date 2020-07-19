from datetime import datetime

from pytest import raises
import random
import string

from meetups.core.exceptions import ResourceNotFound
from meetups.models.user import User
from meetups.services.meetup import UserService

def randstr(max=10):
    return "".join(random.choices(string.ascii_lowercase, k=max))

def test_get_one_ok(db_session):
    user_model = User(name=randstr(), email=randstr(), password=randstr())
    db_session.add(user_model)
    db_session.commit()
    db_session.refresh(user_model)

    user = UserService.get_one(db_session, user_model.id)
    assert user.id == user_model.id

def test_get_one_not_found(db_session):
    with raises(ResourceNotFound):
        UserService.get_one(db_session, "foo_id")


def test_get_all_ok(db_session):
    user_model = User(name=randstr(), email=randstr(), password=randstr())
    db_session.add(user_model)
    db_session.commit()

    users = UserService.get_all(db_session)
    assert type(users) == list
    assert len(users) == 1

def test_get_all_no_users(db_session):
    users = UserService.get_all(db_session)
    assert len(users) == 0