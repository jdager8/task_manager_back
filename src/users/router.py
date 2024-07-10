from typing import List
from fastapi import APIRouter, Depends

from database import get_db
from dependencies import get_current_user

from .service import UserService

from .schemas import UserBase

router = APIRouter(tags=["users"])

@router.get("/users")
async def get_users(
    session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> List[UserBase]:
    """
    Retrieve all users.

    Parameters:
    - session: The database session.
    - current_user: The current authenticated user.

    Returns:
    - A list of UserBase objects representing all users.
    """
    return UserService(session).get_all()