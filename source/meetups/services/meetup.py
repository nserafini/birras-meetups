from sqlalchemy.orm import Session
from meetups.models.meetup import Meetup

class MeetupService:
    @classmethod
    def create(cls, db: Session, meetup: dict):
        meetup = Meetup(**meetup)
        db.add(meetup)
        db.commit()
        db.refresh(meetup)
        return meetup

    @classmethod
    def delete(cls, db: Session, meetup_id: int):
        meetup = cls.get_one(db, meetup_id)
        db.delete(meetup)
        db.commit()
        return meetup

    @classmethod
    def update(cls, db: Session, meetup_id: int, meetup_update: dict):
        meetup = cls.get_one(db, meetup_id)
        for key, value in meetup_update:
            setattr(meetup, key, value)
        db.commit()
        db.refresh(meetup)
        return meetup

    @classmethod
    def get_all(cls, db: Session):
        contacts = db.query(Meetup).all()
        return contacts


    @classmethod
    def get_one(cls, db: Session, meetup_id: int):
        meetup = db.query(Meetup).get(meetup_id)
        return meetup