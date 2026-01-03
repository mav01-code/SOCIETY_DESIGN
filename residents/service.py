from sqlalchemy.orm import Session
from .models import Resident

# CRUD Operations for Resident
def create_resident(db: Session, name, authorization, total_family_members, block, flat_number): # CREATE
    resident = Resident(name = name, authorization = authorization, total_family_members = total_family_members, block = block, flat_number = flat_number)
    db.add(resident)
    db.commit()
    db.refresh(resident)
    return resident

def get_resident(db: Session, block, flat_number): # RETRIEVE
    return db.query(Resident).filter(Resident.block == block, Resident.flat_number == flat_number).first() 
    # first() returns first matched record or None instead of returning an sql object

def update_resident(db: Session, name, authorization, total_family_members, block, flat_number): # UPDATE
    resident = get_resident(db, block, flat_number)
    if not resident:
        return None
    resident.name = name
    resident.authorization = authorization
    resident.total_family_members = total_family_members
    db.commit()
    db.refresh(resident)
    return resident

def delete_resident(db: Session, block, flat_number): # DELETE
    resident = get_resident(db, block, flat_number)
    if not resident:
        return None
    db.delete(resident)
    db.commit()
    return resident