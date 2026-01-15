from pydantic import BaseModel
from datetime import datetime

class EntryCreate(BaseModel):
    block: str
    flat: str
    visitor_name: str
    visitor_type: str
    pass_mode: str
    status: str
    scanned_at: datetime

class EntryUpdate(BaseModel):
    status: str