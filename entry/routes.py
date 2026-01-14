from fastapi import APIRouter
from sqlalchemy.orm import Session
from database.db import get_db
from entry.service import (
    create_entry_request,
    get_entry,
    update_entry
)
router = APIRouter()

@router.post("/")
# (db: Session, block, flat, visitor_name, visitor_type, pass_mode, status):
def add_entry():
    pass

@router.get("/")
def get_entry():
    pass

@router.put("/{block}/{flat}")
def update_entry():
    pass