from sqlalchemy.orm import Session
from models.models import UserModel
from models.schemas import UserCreate


def get_user(db: Session, user_id: int):
    """
    Retrieve a user from the database by their ID.

    Parameters:
        - db (Session): The database session.
        - user_id (int): The ID of the user to retrieve.

    Returns:
        - UserModel: The user object, if it exists in the database.
    """
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of users from the database.

    Parameters:
        - db (Session): The database session.
        - skip (int): The number of users to skip.
        - limit (int): The maximum number of users to retrieve.

    Returns:
        - List[UserModel]: A list of user objects.
    """
    return db.query(UserModel).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user from the database by their email address.

    Parameters:
        - db (Session): The database session.
        - email (str): The email address of the user to retrieve.

    Returns:
        - UserModel: The user object, if it exists in the database.
    """
    return db.query(UserModel).filter(UserModel.email == email).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.

    Parameters:
        - db (Session): The database session.
        - user (UserCreate): The user information to create.

    Returns:
        - None
    """
    fake_password = user.password+"temporalpwd"
    db_user = UserModel(email=user.email, hashed_password=fake_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_user_items(db: Session, user_id: int):
    """
    Retrieve a user's items from the database.

    Parameters:
        - db (Session): The database session.
        - user_id (int): The ID of the user whose items to retrieve.

    Returns:
        - List[ItemModel]: A list of item objects belonging to the user.
    """
    return get_user(db, user_id).items()
