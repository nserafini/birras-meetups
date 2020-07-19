from fastapi import Depends
from fastapi.security import APIKeyHeader

from meetups.core.config import settings
from meetups.core.exceptions import UnauthorizedRequest

X_API_KEY = APIKeyHeader(name="X-API-Key")

def authorize(x_api_key: str = Depends(X_API_KEY)):
    valid_key = settings.API_KEY
    if not valid_key or valid_key != x_api_key:
        raise UnauthorizedRequest(x_api_key)
    return True