from pydantic import BaseModel

class ResidentCreate(BaseModel):
    name: str
    authorization: str
    total_family_members: int

class ResidentUpdate(BaseModel):
    name: str
    authorization: str
    total_family_members: int
    block: str
    flat_number: str