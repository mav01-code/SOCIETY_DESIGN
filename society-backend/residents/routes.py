from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from residents.service import (
    create_resident,
    get_resident,
    update_resident,
    delete_resident
)
from residents.schema import ResidentCreate, ResidentUpdate

router = APIRouter()

from fastapi import Query

@router.post("/")
def add_resident(
    resident: ResidentCreate,
    username: str = Query(...),
    db: Session = Depends(get_db)
):
    block, flat_number = username.strip().split("-")

    return create_resident(
        db,
        resident.name,
        resident.authorization,
        resident.total_family_members,
        block,
        flat_number
    )


@router.get("/{block}/{flat_number}")
def fetch_resident(block: str, flat_number: str, db: Session = Depends(get_db)):
    return get_resident(db, block, flat_number)

@router.get("/by-username/{username}")
def fetch_resident_username(username: str, db: Session = Depends(get_db)):
    username = username.strip()
    l = username.split("-")
    block = l[0]
    flat_number = l[1]
    return get_resident(db, block, flat_number)

@router.put("/{block}/{flat_number}")
def update_res(block: str, flat_number: str, data: ResidentUpdate, db: Session = Depends(get_db)):
    return update_resident(db, data.name, data.authorization, data.total_family_members, block, flat_number)

@router.delete("/{block}/{flat_number}")
def delete_res(block: str, flat_number: str, db: Session = Depends(get_db)):
    return delete_resident(db, block, flat_number)