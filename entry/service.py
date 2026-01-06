from sqlalchemy import Session
from .models import EntryLog

def create_entry_request(db: Session, block, flat, visitor_name, visitor_type, pass_mode, status):
    entry = EntryLog(
        block=block,
        flat_number=flat,
        visitor_name=visitor_name,
        visitor_type=visitor_type,
        pass_mode=pass_mode,
        status=status
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry.log_id

def get_entry(db: Session, log_id):
    entry = db.query(EntryLog).filter(EntryLog.log_id == log_id).first()
    return entry

def update_entry(db: Session, log_id, new_status):
    entry = db.query(EntryLog).filter(EntryLog.log_id == log_id).first()
    if entry:
        entry.status = new_status
        db.commit()
        db.refresh(entry)
    return entry