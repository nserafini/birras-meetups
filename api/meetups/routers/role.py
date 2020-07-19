from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from meetups.core.database import db
from meetups.services.role import RoleService
from meetups.models.role import RoleOUT

role_router = APIRouter()

@role_router.get("/{id}", response_model=RoleOUT, status_code=200)
def get_one_role(id: str, db: Session = Depends(db)):
    role = RoleService.get_one(db, id)
    return role

@role_router.get("", response_model=List[RoleOUT], status_code=200)
def get_all_role(db: Session = Depends(db)):
    roles = RoleService.get_all(db)
    return roles