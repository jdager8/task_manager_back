from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
import jwt
from passlib.context import CryptContext

from users.service import UserService

from users.schemas import UserCreate
from auth.schemas import Token

from config import get_settings

settings = get_settings()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService():
    """
    The AuthService class provides authentication and user registration functionality.
    """

    def __init__(self, session: Session = Session):
        """
        Initializes a new instance of the AuthService class.

        Args:
            session (Session): The database session to use. Defaults to Session.
        """
        self.session = session
    
    def authenticate_user(self, username: str, password: str):
        """
        Authenticates a user with the provided username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            str: The access token for the authenticated user.

        Raises:
            HTTPException: If the provided credentials are invalid.
        """
        user = UserService(self.session).get_by_username(username)
        if user is None:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        
        if not self.verify_password(password=password, hashed_pass=user.password):
            raise HTTPException(status_code=400, detail="Invalid password")
        
        res = {
            'access_token': self.create_access_token({"sub": user.username}),
            "id": user.id
        }
        return res
    
    def register_user(self, user: UserCreate):
        """
        Registers a new user.

        Args:
            user (UserCreate): The user object containing the user details.

        Returns:
            User: The created user object.
        """
        hashed_password = self.get_hashed_password(user.password)
        user.password = hashed_password
        return UserService(self.session).create(user)
    
    def create_access_token(self, data: dict) -> str:
            """
            Creates an access token with the provided data.

            Args:
                data (dict): The data to include in the access token.

            Returns:
                str: The encoded access token.
            """
            to_encode = data.copy()
            expire = datetime.now() + timedelta(minutes=int(settings.jwt_expires_in))
            to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm)
            return encoded_jwt
    
    def get_hashed_password(self, password: str) -> str:
        """
        Hashes the provided password.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return password_context.hash(password)
    
    def verify_password(self, password: str, hashed_pass: str) -> bool:
        """
        Verifies the provided password against the hashed password.

        Args:
            password (str): The password to verify.
            hashed_pass (str): The hashed password to compare against.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        return password_context.verify(password, hashed_pass)