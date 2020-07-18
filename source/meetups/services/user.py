from sqlalchemy.orm import Session
from meetups.models.user import User

class UserService:
    @classmethod
    def get_one(cls, db: Session, user_id: int):
        user = db.query(User).get(user_id)
        del user.password_hash
        return user