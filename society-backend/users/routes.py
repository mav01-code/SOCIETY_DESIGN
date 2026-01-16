from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from users.service import create_user, get_user, update_user, delete_user
from users.schema import UsersCreate, UsersUpdate

router = APIRouter()

@router.post("/")
def add_user(user: UsersCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.password_hash, user.role)

@router.get("/{user_id}")
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.put("/{user_id}")
def update_users(user: UsersUpdate, user_id: int, db: Session = Depends(get_db)):
    return update_user(db, user_id, user.username, user.password_hash, user.role)

@router.delete("/{user_id}")
def delete_users(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)