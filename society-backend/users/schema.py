from pydantic import BaseModel

class UsersCreate(BaseModel):
    username: str
    password: str
    role: str

class UsersUpdate(BaseModel):
    username: str
    password: str
    role: str

class LoginRequest(BaseModel):
    username: str
    password: str