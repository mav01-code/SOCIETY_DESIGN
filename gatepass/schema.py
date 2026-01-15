from pydantic import BaseModel
from datetime import datetime

class GatePassCreate(BaseModel):
    block: str
    flat: str
    pass_type: str
    issued_to: str
    valid_from: datetime
    valid_till: datetime
    status: str


class GatePassUpdate(BaseModel):
    pass_type: str
    issued_to: str
    valid_from: datetime
    valid_till: datetime
    status: str
