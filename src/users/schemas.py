from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    """
    Represents the base schema for a user.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (EmailStr): The email address of the user.

    Config:
        from_attributes (bool): Whether to populate the model from the attributes.
    """
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., min_length=3, max_length=50)
    password: str = Field(..., pattern=r'^\d*$')