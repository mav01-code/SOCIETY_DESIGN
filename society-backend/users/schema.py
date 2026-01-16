from pydantic import BaseModel

class UsersCreate(BaseModel):
    username: str
    password_hash: str
    role: str

class UsersUpdate(BaseModel):
    username: str
    password_hash: str
    role: str