from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship

from database import Base

from users.models import User

class Task(Base):
    """
    Represents a task in the task manager.
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    due_date = Column(TIMESTAMP, server_default=func.now())
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey(User.id))

    user = relationship("User", back_populates="tasks")
