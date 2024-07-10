from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Settings class for the application.

    Attributes:
        database_dsn (str): The host of the database.
        jwt_secret (str): The secret key for JWT token generation.
        jwt_expires_in (str): The expiration time for JWT tokens.
        jwt_algorithm (str): The algorithm to use for JWT token generation.
        model_config (SettingsConfigDict): The configuration dictionary for the model.
    """

    database_dsn: str
    jwt_secret: str
    jwt_expires_in: str
    jwt_expires_in: str
    jwt_algorithm: str

    model_config = SettingsConfigDict(env_file="../.env")

@lru_cache()
def get_settings():
    return Settings()