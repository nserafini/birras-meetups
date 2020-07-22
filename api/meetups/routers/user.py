from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from meetups.core.database import db
from meetups.services.user import UserService
from meetups.models.user import UserOUT
from meetups.models.meetup import MeetupOUT
from meetups.models.role import RoleOUT

user_router = APIRouter()

@user_router.get("/{id}", response_model=UserOUT, status_code=200)
def get_one_user(id: str, db: Session = Depends(db)):
    user = UserService.get_one(db, id)
    return user

@user_router.get("", response_model=List[UserOUT], status_code=200)
def get_all_users(db: Session = Depends(db)):
    users = UserService.get_all(db)
    return users

@user_router.get("/{id}/meetups", response_model=List[MeetupOUT], status_code=200)
def get_meetups(id: str, db: Session = Depends(db)):
    user = UserService.get_one(db, id)
    return user.meetups

@user_router.get("/{id}/roles", response_model=List[RoleOUT], status_code=200)
def get_roles(id: str, db: Session = Depends(db)):
    user = UserService.get_one(db, id)
    return user.roles

@user_router.get("/{id}/notifications", status_code=200)
def get_notifications(id: str, db: Session = Depends(db)):
    notifications = UserService.get_notifications(db, id)
    return {"notifications": notifications}