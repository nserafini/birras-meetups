from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from meetups.core.database import db
from meetups.services.meetup import MeetupService
from meetups.core.config import settings

meetup_router = APIRouter()

@meetup_router.post("", status_code=201)
def create_meetup(meetup: dict, db: Session = Depends(db)):
    meetup = MeetupService.create(db, meetup)
    return meetup

@meetup_router.delete("/{id}", status_code=204)
def delete_contact(id: int, db: Session = Depends(db)):
    MeetupService.delete(db, id)

@meetup_router.put("/{contact_id}", status_code=200)
def update_contact(contact_id: int, meetup: dict, db: Session = Depends(db)):
    meetup = MeetupService.update(db, contact_id, meetup)
    return meetup

@meetup_router.get("", status_code=200)
def get_all_contacts(db: Session = Depends(db)):
    meetups = MeetupService.get_all(db)
    return meetups

@meetup_router.get("/{id}", status_code=200)
def get_meetup(id: int, db: Session = Depends(db)):
    meetup = MeetupService.get_one(db, id)
    return meetup