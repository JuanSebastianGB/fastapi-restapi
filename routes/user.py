from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.models import UserModel
from config.db import session
from models.schemas import UserCreate, ItemCreate, User
from services import user as user_service
from services import item as item_service

user_router = APIRouter()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@user_router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_service.create_user(db=db, user=user)


@user_router.get("/users", status_code=status.HTTP_200_OK, response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@user_router.get("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@user_router.get("/users/{user_id}/items", status_code=status.HTTP_200_OK)
def get_user_items(user_id: int, db: Session = Depends(get_db)):
    items = user_service.get_user_items(db, user_id)
    return items


@user_router.post("/users/{user_id}/items")
def create_user_item(user_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_user_item(db, item, user_id)
