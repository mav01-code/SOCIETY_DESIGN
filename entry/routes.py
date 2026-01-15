from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from entry.service import create_entry_request, get_entry, update_entry
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
        entry.status,
        entry.scanned_at
    )

@router.get("/{log_id}")
def fetch_entry(log_id: int, db: Session = Depends(get_db)):
    return get_entry(db, log_id)

@router.put("/{log_id}")
def modify_entry(log_id: int, entry: EntryUpdate, db: Session = Depends(get_db)):
    return update_entry(db, log_id, entry.status)
