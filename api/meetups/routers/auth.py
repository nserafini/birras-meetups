from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import Response
import jwt
from sqlalchemy.orm import Session

from meetups.core.database import db
from meetups.core.config import settings
from meetups.models.auth import AuthIN
from meetups.models.auth import AuthOUT
from meetups.services.user import UserService

auth_router = APIRouter()


@auth_router.post("/login", response_model=AuthOUT, status_code=200)
def login(response: Response, credentials: AuthIN, db: Session = Depends(db)):
    user = UserService.auth(db, credentials.dict())
    token = jwt.encode({'user':{'id': user.id, 'user': user.name}}, settings.API_KEY)
    response.set_cookie("token", value=token.decode("utf-8"))
    return {"token": token}

@auth_router.delete("/logout", status_code=204)
def logout(response: Response):
    response.delete_cookie("token")