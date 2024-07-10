from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

from config import get_settings

settings = get_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieves the current user based on the provided token.

    Args:
        token (str): The authentication token.

    Returns:
        str: The user identifier extracted from the token.

    Raises:
        HTTPException: If the token is invalid or does not contain a valid user identifier.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=settings.jwt_algorithm)
        token_data: str = payload.get("sub")

        if token_data is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
    
    return token_data