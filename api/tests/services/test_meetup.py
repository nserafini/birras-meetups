from datetime import datetime
from meetups.services.meetup import MeetupService
from meetups.models.meetup import Meetup
from meetups.models.user import User
import random
import string
from unittest.mock import patch

def randstr(max=10):
    return "".join(random.choices(string.ascii_lowercase, k=max))

@patch('meetups.services.meetup.WeatherService.get_temperature')
def test_calculate_beer_cold_temperature(get_temperature_mock, db_session):
    get_temperature_mock.return_value = 15
    meetup = Meetup(name=randstr(), description=randstr(), date=datetime.now())

    for _ in range(15):
        user = User(name=randstr(), email=randstr(), password=randstr())
        meetup.users.append(user)

    db_session.add(meetup)
    db_session.commit()

    beers, packs = MeetupService.calculate_beer(db_session, meetup.id)
    assert beers == 11.25
    assert packs == 2


@patch('meetups.services.meetup.WeatherService.get_temperature')
def test_calculate_beer_tempered_temperature(get_temperature_mock, db_session):
    get_temperature_mock.return_value = 23
    meetup = Meetup(name=randstr(), description=randstr(), date=datetime.now())

    for _ in range(15):
        user = User(name=randstr(), email=randstr(), password=randstr())
        meetup.users.append(user)

    db_session.add(meetup)
    db_session.commit()

    beers, packs = MeetupService.calculate_beer(db_session, meetup.id)
    assert beers == 15
    assert packs == 3



@patch('meetups.services.meetup.WeatherService.get_temperature')
def test_calculate_beer_hot_temperature(get_temperature_mock, db_session):
    get_temperature_mock.return_value = 31
    meetup = Meetup(name=randstr(), description=randstr(), date=datetime.now())

    for _ in range(15):
        user = User(name=randstr(), email=randstr(), password=randstr())
        meetup.users.append(user)

    db_session.add(meetup)
    db_session.commit()

    beers, packs = MeetupService.calculate_beer(db_session, meetup.id)
    assert beers == 30
    assert packs == 5