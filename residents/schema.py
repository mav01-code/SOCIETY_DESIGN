from pydantic import BaseModel

class EntryCreate(BaseModel):
    block: str
    flat: str
    visitor_name: str
    visitor_type: str
    pass_mode: str
    status: str

class EntryUpdate(BaseModel):
    visitor_name: str
    visitor_type: str
    pass_mode: str
    status: str