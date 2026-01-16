from sqlalchemy.orm import Session
from database.models import EntryLog
from datetime import datetime

def create_entry_request(db: Session, block, flat, visitor_name, visitor_type, pass_mode, status, scanned_at=None):
    entry = EntryLog(
        block=block,
        flat_number=flat,
        visitor_name=visitor_name,
        visitor_type=visitor_type,
        pass_mode=pass_mode,
        status=status,
        scanned_at = scanned_at or datetime.utcnow()
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry.log_id

def get_entry(db: Session, log_id: int):
    return db.query(EntryLog).filter(EntryLog.log_id == log_id).first()

def update_entry(db: Session, log_id: int, new_status: str):
    entry = db.query(EntryLog).filter(EntryLog.log_id == log_id).first()
    if entry:
        entry.status = new_status
        db.commit()
        db.refresh(entry)
    return entry
