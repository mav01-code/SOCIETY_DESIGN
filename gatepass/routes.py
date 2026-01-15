from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from gatepass.service import (
    create_gatepass,
    get_gatepass,
    update_gatepass
)
from gatepass.schema import GatePassCreate, GatePassUpdate

router = APIRouter()

@router.post("/")
def add_gatepass(gatepass: GatePassCreate, db: Session = Depends(get_db)):
    return create_gatepass(
        db,
        gatepass.block,
        gatepass.flat,
        gatepass.pass_type,
        gatepass.issued_to,
        gatepass.valid_from,
        gatepass.valid_till,
        gatepass.status
    )

@router.get("/{block}/{flat}")
def fetch_gatepass(block: str, flat: str, db: Session = Depends(get_db)):
    return get_gatepass(db, block, flat)

@router.put("/{block}/{flat}")
def modify_gatepass(block: str, flat: str, gatepass: GatePassUpdate, db: Session = Depends(get_db)):
    return update_gatepass(
        db,
        block,
        flat,
        gatepass.pass_type,
        gatepass.issued_to,
        gatepass.valid_from,
        gatepass.valid_till,
        gatepass.status
    )
