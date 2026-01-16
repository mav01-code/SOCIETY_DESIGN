from sqlalchemy.orm import Session
from database.models import Users

def create_user(db: Session, username, password, role):
    user = Users(username = username, password = password, role = role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id):
    return db.query(Users).filter(Users.user_id == user_id).first()

def update_user(db: Session, user_id, username, password, role):
    user  =get_user(db, user_id)
    if not user:
        return None
    user.username = username
    user.password = password
    user.role = role
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id):
    user = get_user(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user