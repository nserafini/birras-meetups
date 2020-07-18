from typing import List
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from meetups.core.database import db
from meetups.services.user import UserService
from meetups.core.config import settings
from meetups.models.user import UserOUT

user_router = APIRouter()

@user_router.get("/{id}", response_model=UserOUT, status_code=200)
def get_one_user(id: str, db: Session = Depends(db)):
    user = UserService.get_one(db, id)
    return user

@user_router.get("", response_model=List[UserOUT], status_code=200)
def get_all_users(db: Session = Depends(db)):
    users = UserService.get_all(db)
    return users