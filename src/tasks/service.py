from sqlalchemy.orm import Session
from typing import List

from .models import Task

from .schemas import TaskBase

class TaskService():
    """
    This class provides methods to interact with the task data in the database.
    """

    def __init__(self, session = Session):
        """
        Initializes a new instance of the TaskService class.

        Args:
            session: The database session to use. Defaults to Session.
        """
        self.session = session
    
    def get_all(self) -> List[TaskBase]:
        """
        Retrieves all tasks from the database.

        Returns:
            A list of TaskBase objects representing all the tasks in the database.
        """
        return self.session.query(Task).all()
    
    def get_by_id(self, task_id: int) -> TaskBase:
        """
        Retrieves a task from the database by its ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            A TaskBase object representing the retrieved task.
        """
        return self.session.query(Task).filter(Task.id == task_id).first()
    
    def get_by_user(self, user_id: int) -> List[TaskBase]:
        """
        Retrieves all tasks for a specific user from the database.

        Args:
            user_id: The ID of the user to retrieve tasks for.

        Returns:
            A list of TaskBase objects representing all the tasks for the specified user.
        """
        return self.session.query(Task).filter(Task.user_id == user_id).all()
    
    def create(self, task: TaskBase) -> TaskBase:
        """
        Creates a new task in the database.

        Args:
            task: The TaskBase object representing the task to create.

        Returns:
            A TaskBase object representing the created task.
        """
        db_task = Task(
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            completed=task.completed,
            user_id=task.user_id
        )
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return db_task
    
    def update(self, task_id: int, task: TaskBase) -> TaskBase:
        """
        Updates an existing task in the database.

        Args:
            task_id: The ID of the task to update.
            task: The TaskBase object representing the updated task.

        Returns:
            A TaskBase object representing the updated task.
        """
        db_task = self.get_by_id(task_id)
        db_task.title = task.title
        db_task.description = task.description
        db_task.due_date = task.due_date
        db_task.completed = task.completed
        db_task.user_id = task.user_id
        self.session.commit()
        self.session.refresh(db_task)
        return db_task
    
    def delete(self, task_id: int) -> TaskBase:
        """
        Deletes a task from the database.

        Args:
            task_id: The ID of the task to delete.

        Returns:
            A TaskBase object representing the deleted task.
        """
        self.session.query(Task).filter(Task.id == task_id).delete()
        self.session.commit()
        return task_id
