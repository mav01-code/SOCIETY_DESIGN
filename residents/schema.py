from pydantic import BaseModel

class ResidentCreate(BaseModel):
    block: str
    flat: str
    name: str
    phone: str


class ResidentUpdate(BaseModel):
    name: str
    phone: str
