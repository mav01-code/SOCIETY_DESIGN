from fastapi import APIRouter
from sqlalchemy.orm import Session
from database.db import get_db
from entry.service import (
    create_entry_request,
    get_entry,
    update_entry
)
router = APIRouter()

