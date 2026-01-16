from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from gatepass.service import generate_qr, update_gatepass, get_gatepass_by_id, get_gatepasses_by_flat
from gatepass.schema import GatePassCreate, GatePassUpdate

router = APIRouter()

@router.post("/")
def add_gatepass(gatepass: GatePassCreate, db: Session = Depends(get_db)):
    return generate_qr(
        db,
        gatepass.block,
        gatepass.flat_number,
        gatepass.valid_from,
        gatepass.valid_until
    )

@router.put("/")
def modify_gatepass(gatepass: GatePassUpdate, db: Session = Depends(get_db)):
    return update_gatepass(
        db,
        gatepass.pass_id,
        gatepass.block,
        gatepass.flat_number,
        gatepass.valid_from,
        gatepass.valid_until
    )

@router.get("/{pass_id}")
def fetch_gatepass(pass_id: int, db: Session = Depends(get_db)):
    return get_gatepass_by_id(db, pass_id)

@router.get("/flat/{block}/{flat_number}")
def fetch_gatepasses_for_flat(block: str, flat_number: str, db: Session = Depends(get_db)):
    return get_gatepasses_by_flat(db, block, flat_number)
