from sqlalchemy.orm import Session
from meetups.core.exceptions import ResourceNotFound
from meetups.models.user import User

class UserService:
    @classmethod
    def get_one(cls, db: Session, user_id: str):
        user = db.query(User).get(user_id)
        if not user:
            raise ResourceNotFound(user_id)
        del user.password_hash
        return user

    @classmethod
    def get_all(cls, db: Session):
        users = db.query(User).all()
        return users