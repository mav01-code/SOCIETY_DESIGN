from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from users.service import create_user, get_user, update_user, delete_user
from users.schema import UsersCreate, UsersUpdate, LoginRequest
from database.models import Users

router = APIRouter()

@router.post("/")
def add_user(user: UsersCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.password, user.role)

@router.get("/{user_id}")
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(
        Users.username == user.username,
        Users.password == user.password
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "user_id": db_user.user_id,
        "username": db_user.username,
        "role": db_user.role
    }



@router.put("/{user_id}")
def update_users(user: UsersUpdate, user_id: int, db: Session = Depends(get_db)):
    return update_user(db, user_id, user.username, user.password, user.role)

@router.delete("/{user_id}")
def delete_users(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)