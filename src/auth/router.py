from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth.service import AuthService
from database import get_db
from users.schemas import UserBase, UserCreate
from auth.schemas import Token

router = APIRouter(tags=["auth"])

@router.post("/login")
async def authenticate(login: OAuth2PasswordRequestForm = Depends(), session = Depends(get_db)) -> Token:
    """
    Authenticates a user with the provided username and password.

    Args:
        login (OAuth2PasswordRequestForm): The login credentials provided by the user.
        session: The database session.

    Returns:
        Token: The authentication token for the user.
    """
    return AuthService(session).authenticate_user(login.username, login.password)

@router.post("/register")
async def register(user: UserCreate, session = Depends(get_db)) -> UserBase:
    """
    Registers a new user with the provided user details.

    Args:
        user (UserCreate): The user details for registration.
        session: The database session.

    Returns:
        UserBase: The registered user details.
    """
    return AuthService(session).register_user(user)