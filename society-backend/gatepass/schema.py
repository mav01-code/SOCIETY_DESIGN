from pydantic import BaseModel
from datetime import datetime

class GatePassCreate(BaseModel):
    block: str
    flat_number: str
    valid_from: datetime
    valid_until: datetime

class GatePassUpdate(BaseModel):
    pass_id: int
    block: str
    flat_number: str
    valid_from: datetime
    valid_until: datetime
