from pydantic import BaseModel

class AuthIN(BaseModel):
    user: str
    password: str

class AuthOUT(BaseModel):
    token: str