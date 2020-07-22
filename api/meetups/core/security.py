from fastapi import Depends
from fastapi.security import APIKeyHeader
from fastapi.requests import Request
import jwt

from meetups.core.database import get_session
from meetups.core.config import settings
from meetups.core.exceptions import UnauthorizedRequest
from meetups.core.exceptions import ForbiddenNotLogged
from meetups.core.exceptions import ForbiddenNoAdminRole

from meetups.services.user import UserService

X_API_KEY = APIKeyHeader(name="X-API-Key")

def is_authorize(x_api_key: str = Depends(X_API_KEY)):
    valid_key = settings.API_KEY
    if not valid_key or valid_key != x_api_key:
        raise UnauthorizedRequest(x_api_key)
    return True

def is_logged(request: Request):
    try:
        token = request.cookies.get("token")
        token = jwt.decode(token, settings.API_KEY)
    except Exception:
       raise ForbiddenNotLogged(token)
    return True

def is_admin(request: Request):
    try:
        token = request.cookies.get("token")
        token = jwt.decode(token, settings.API_KEY)
    except Exception:
       raise ForbiddenNotLogged(token)

    with get_session(settings.DSN) as db:
        try:
            user = UserService.get_one(db, token['user']['id'])
        except Exception:
            raise ForbiddenNotLogged(token)
        
        if is_admin and not user.is_admin():
            raise ForbiddenNoAdminRole(token)
    return True

