from sqlalchemy.orm import Session
from meetups.core.exceptions import ResourceNotFound
from meetups.models.user import User
from datetime import datetime
class UserService:
    @classmethod
    def get_one(cls, db: Session, user_id: str):
        user = db.query(User).get(user_id)
        if not user:
            raise ResourceNotFound(user_id)
        return user

    @classmethod
    def get_all(cls, db: Session):
        users = db.query(User).all()
        return users

    @classmethod
    def get_notifications(cls, db: Session, user_id: str):
        user = cls.get_one(db, user_id)
        today_meetups = []
        for meetup in user.meetups:
            if meetup.date.date() == datetime.today().date():
                today_meetups.append(meetup)
        return today_meetups