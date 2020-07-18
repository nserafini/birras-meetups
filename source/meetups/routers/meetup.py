from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from meetups.core.database import db
from meetups.services.meetup import MeetupService
from meetups.core.config import settings
from meetups.models.meetup import MeetupIN, MeetupOUT

meetup_router = APIRouter()

@meetup_router.post("", response_model=MeetupOUT, status_code=201)
def create_meetup(meetup: MeetupIN, db: Session = Depends(db)):
    meetup = MeetupService.create(db, meetup)
    return meetup

@meetup_router.get("/{id}", response_model=MeetupOUT, status_code=200)
def get_one_meetup(id: str, db: Session = Depends(db)):
    meetup = MeetupService.get_one(db, id)
    return meetup

@meetup_router.get("", response_model=List[MeetupOUT], status_code=200)
def get_all_meetups(db: Session = Depends(db)):
    meetups = MeetupService.get_all(db)
    return meetups

@meetup_router.put("/{id}/users/{user_id}", response_model=MeetupOUT, status_code=200)
def add_user(id: str, user_id: str, db: Session = Depends(db)):
    meetup = MeetupService.add_user(db, id, user_id)
    return meetup

@meetup_router.get("/{id}/beers", status_code=200)
def calculate_beers(id: str, db: Session = Depends(db)):
    beers = MeetupService.calculate_beer(db, id)
    return {'beers': beers}

@meetup_router.get("/{id}/temperature", status_code=200)
def get_temperature(id: str, db: Session = Depends(db)):
    temperature = MeetupService.get_temperature(db, id)
    return {'temperature': temperature}