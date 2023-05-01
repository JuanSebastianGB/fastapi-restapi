from sqlalchemy.orm import Session
from models.models import UserModel
from models.schemas import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def create_user(db: Session, user: UserCreate):
    fake_password = user.password+"temporalpwd"
    db_user = UserModel(email=user.email, hashed_password=fake_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_user_items(db: Session, user_id: int):
    return get_user(db, user_id).items()
