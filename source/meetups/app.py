from fastapi import FastAPI

from meetups.core.config import settings

from meetups.models.base import BaseModel
from meetups.models.meetup import Meetup
from meetups.models.user import User
from meetups.models.meetup_user import MeetupUser
from meetups.models.role import Role
from meetups.models.user_role import UserRole

from meetups.routers.meetup import meetup_router
from meetups.routers.user import user_router
from meetups.core.database import get_engine

def db_init(dsn):
    engine = get_engine(dsn)
    BaseModel.metadata.create_all(engine)

def create_app():
    app = FastAPI(title=settings.API_NAME, version=settings.API_VERSION)
    app.include_router(meetup_router, prefix="/meetups", tags=["Meetups"])
    app.include_router(user_router, prefix="/users", tags=["Users"])
    return app

db_init(settings.DSN)
app = create_app()

