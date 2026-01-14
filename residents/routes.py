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

@router.get("/{block}/{flat}")
def get_resident(block: str, flat: str, db: Session = Depends(get_db)):
    return get_resident_by_flat(db, block, flat)


@router.put("/{block}/{flat}")
def update_res(block: str, flat: str, name: str, phone: str, db: Session = Depends(get_db)):
    return update_resident(db, block, flat, name, phone)


@router.delete("/{block}/{flat}")
def delete_res(block: str, flat: str, db: Session = Depends(get_db)):
    return delete_resident(db, block, flat)
