from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from entry.service import (
    create_entry_request,
    get_entry,
    update_entry
)
from entry.schema import EntryCreate, EntryUpdate

router = APIRouter()

@router.post("/")
def add_entry(entry: EntryCreate, db: Session = Depends(get_db)):
    return create_entry_request(
        db,
        entry.block,
        entry.flat,
        entry.visitor_name,
        entry.visitor_type,
        entry.pass_mode,
        entry.status
    )

@router.get("/{block}/{flat}")
def fetch_entry(block: str, flat: str, db: Session = Depends(get_db)):
    return get_entry(db, block, flat)

@router.put("/{block}/{flat}")
def modify_entry(block: str, flat: str, entry: EntryUpdate, db: Session = Depends(get_db)):
    return update_entry(
        db,
        block,
        flat,
        entry.visitor_name,
        entry.visitor_type,
        entry.pass_mode,
        entry.status
    )
