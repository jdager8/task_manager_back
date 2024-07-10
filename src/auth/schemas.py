from pydantic import BaseModel

class Token(BaseModel):
    """
    Represents a token used for authentication.

    Attributes:
        access_token (str): The access token string.
        id (int): The ID of the user associated with the token.
    """
    access_token: str
    id: int