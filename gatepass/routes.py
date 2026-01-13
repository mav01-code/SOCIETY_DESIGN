from fastapi import APIRouter
from sqlalchemy.orm import Session
from database.db import get_db

router = APIRouter()

@router.get("/ping")
def ping():
    return {"status": "Gatepass service alive"}
