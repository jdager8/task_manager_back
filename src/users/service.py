from sqlalchemy.orm import Session
from typing import List

from .models import User

from .schemas import UserBase, UserCreate

class UserService():
    """
    Service class for managing user-related operations.
    """

    def __init__(self, session = Session):
        self.session = session
    
    def get_all(self) -> List[UserBase]:
        """
        Retrieves all users from the database.

        Returns:
            List[UserBase]: A list of user objects.
        """
        return self.session.query(User).all()
    
    def get_by_username(self, username: str) -> UserBase:
        """
        Retrieves a user by their username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            UserBase: The user object.
        """
        return self.session.query(User).filter(User.username == username).first()
    
    def create(self, user: UserCreate) -> UserBase:
        """
        Creates a new user in the database.

        Args:
            user (UserCreate): The user data to create.

        Returns:
            UserBase: The created user object.
        """
        db_user = User(
            username=user.username,
            email=user.email,
            password=user.password
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user