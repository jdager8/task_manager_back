from pydantic import BaseModel, Field
from datetime import datetime

from users.schemas import UserBase

class TaskBase(BaseModel):
    """
    Represents the base schema for a task.

    Attributes:
        id (int): The unique identifier for the task.
        title (str): The title of the task.
        description (str): The description of the task.
        due_date (datetime): The due date of the task. Defaults to the current date and time.
        completed (bool): Indicates whether the task is completed or not. Defaults to False.
        user_id (int): The ID of the user associated with the task.
        user (UserBase): The user associated with the task.
    """
    id: int
    title: str
    description: str
    due_date: datetime = Field(default=datetime.today())
    completed: bool = Field(default=False)
    user_id: int
    user: UserBase

class TaskCreate(BaseModel):
    """
    Represents the schema for creating a new task.

    Attributes:
        title (str): The title of the task.
        description (str): The description of the task.
        due_date (datetime): The due date of the task. Defaults to the current date and time.
        completed (bool): Indicates whether the task is completed or not. Defaults to False.
        user_id (int): The ID of the user associated with the task. Defaults to 1.
    """
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=255)
    due_date: datetime = Field(default=datetime.today())
    completed: bool = Field(default=False)
    user_id: int = Field(default=1)

class TaskUpdate(TaskCreate):
    pass
