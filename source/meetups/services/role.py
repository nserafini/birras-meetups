from sqlalchemy.orm import Session
from meetups.core.exceptions import ResourceNotFound
from meetups.models.role import Role

class UserService:
    @classmethod
    def get_one(cls, db: Session, role_id: str):
        role = db.query(Role).get(role_id)
        if not role:
            raise ResourceNotFound(role_id)
        return role

    @classmethod
    def get_all(cls, db: Session):
        roles = db.query(Role).all()
        return roles