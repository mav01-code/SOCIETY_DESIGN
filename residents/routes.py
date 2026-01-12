from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from residents.service import (
    create_resident,
    get_all_residents,
    get_resident_by_flat,
    update_resident,
    delete_resident
)

router = APIRouter()

@router.post("/")
def add_resident(name: str, flat: str, block: str, phone: str, db: Session = Depends(get_db)):
    return create_resident(db, name, flat, block, phone)

@router.get("/")
def list_residents(db: Session = Depends(get_db)):
    return get_all_residents(db)

@router.get("/{flat}")
def get_resident(flat: str, db: Session = Depends(get_db)):
    return get_resident_by_flat(db, flat)

@router.put("/{flat}")
def update_res(flat: str, name: str, phone: str, db: Session = Depends(get_db)):
    return update_resident(db, flat, name, phone)

@router.delete("/{flat}")
def delete_res(flat: str, db: Session = Depends(get_db)):
    return delete_resident(db, flat)
