from sqlalchemy.orm import Session
from models.models import ItemModel
from models.schemas import ItemCreate


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve items from the database.

    Parameters:
        - db (Session): The database session.
        - skip (int): The number of items to skip in the query (default 0).
        - limit (int): The maximum number of items to retrieve (default 100).

    Returns:
        - List[ItemModel]: A list of ItemModel objects.
    """
    return db.query(ItemModel).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    """
    Create a new item owned by a user in the database.

    Parameters:
        - db (Session): The database session.
        - item (ItemCreate): The data for the new item.
        - user_id (int): The ID of the user who will own the new item.

    Returns:
        - ItemModel: The newly created item object.
    """
    db_item = ItemModel(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
