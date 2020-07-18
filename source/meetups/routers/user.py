from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from meetups.core.database import db
from meetups.services.user import UserService
from meetups.core.config import settings

user_router = APIRouter()

@user_router.get("/{id}", status_code=200)
def get_user(id: int, db: Session = Depends(db)):
    user = UserService.get_one(db, id)
    return user