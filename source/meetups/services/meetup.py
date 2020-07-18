import math
from sqlalchemy.orm import Session

from meetups.core.exceptions import ResourceNotFound
from meetups.models.meetup import Meetup
from meetups.services.user import UserService
from meetups.services.weather import WeatherService

class MeetupService:
    @classmethod
    def create(cls, db: Session, meetup: dict):
        meetup = Meetup(**meetup)
        db.add(meetup)
        db.commit()
        db.refresh(meetup)
        return meetup

    @classmethod
    def get_one(cls, db: Session, meetup_id: str):
        meetup = db.query(Meetup).get(meetup_id)
        if not meetup:
            raise ResourceNotFound(meetup_id)
        return meetup

    @classmethod
    def get_all(cls, db: Session):
        meetups = db.query(Meetup).all()
        return meetups

    @classmethod
    def add_user(cls, db: Session, meetup_id: str, user_id: str):
        meetup = cls.get_one(db, meetup_id)
        user = UserService.get_one(db, user_id)
        meetup.users.append(user)
        db.commit()
        db.refresh(meetup)
        return meetup

    @classmethod
    def calculate_beer(cls, db: Session, meetup_id: str):
        meetup = cls.get_one(db, meetup_id)
        participants = len(meetup.users)
        temperature = WeatherService.get_temperature(meetup.date.strftime("%s"))

        if temperature < 20:
            beers = participants * 0.75

        if temperature > 20 and temperature < 24:
            beers = participants * 1

        if temperature > 24:
            beers = participants * 2

        beer_packs = math.ceil(beers/6)
        
        return beer_packs

    @classmethod
    def get_temperature(cls, db: Session, meetup_id: str):
        meetup = db.query(Meetup).get(meetup_id)
        temperature = WeatherService.get_temperature(meetup.date.strftime("%s"))
        return temperature