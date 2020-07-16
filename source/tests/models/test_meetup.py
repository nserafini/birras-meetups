from datetime import datetime
from pytest import raises
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
