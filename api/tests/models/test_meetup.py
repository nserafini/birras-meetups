from datetime import datetime
from meetups.models.meetup import Meetup
from meetups.models.user import User

def test_meetup_model(db_session):
    name = "daily"
    description = "test_description"
    date = datetime.now()

    meetup = Meetup(name=name, description=description, date=date)

    db_session.add(meetup)
    db_session.flush()

    assert meetup.name == name
    assert meetup.description == description
    assert meetup.date == date

def test_meetup_add_users(db_session):
    meetup = Meetup(name="daily", description="team daily", date=datetime.now())
    user_foo = User(name="foo", email="foo@mail.com", password="1234")
    user_bar = User(name="bar", email="bar@mail.com", password="4321")

    meetup.users.append(user_foo)
    meetup.users.append(user_bar)

    db_session.add(meetup)
    db_session.commit()
    db_session.refresh(meetup)
    
    assert meetup.users[0].id == user_foo.id
    assert meetup.users[1].id == user_bar.id