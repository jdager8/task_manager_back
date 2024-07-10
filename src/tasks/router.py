from fastapi import APIRouter, Depends
from typing import List

from database import get_db
from dependencies import get_current_user

from .service import TaskService

from .schemas import TaskBase, TaskCreate, TaskUpdate

router = APIRouter(tags=["tasks"])

@router.get("/tasks")
async def get_tasks(
    session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> List[TaskBase]:
    """
    Retrieve all tasks.

    Returns:
        List[TaskBase]: A list of task objects.
    """
    return TaskService(session).get_all()

@router.get("/tasks/{task_id}")
async def get_task(
    task_id: int, 
    session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> TaskBase:
    """
    Retrieve a specific task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.

    Returns:
        TaskBase: The task object.
    """
    return TaskService(session).get_by_id(task_id)

@router.get("/tasks/user/{user_id}")
async def get_tasks_by_user(
    user_id: int, 
    session = Depends(get_db), 
    current_user=Depends(get_current_user)
) -> List[TaskBase]:
    """
    Retrieve all tasks for a specific user.

    Args:
        user_id (int): The ID of the user to retrieve tasks for.

    Returns:
        List[TaskBase]: A list of task objects.
    """
    return TaskService(session).get_by_user(user_id)

@router.post("/tasks")
async def create_task(
    task: TaskCreate, 
    session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> TaskBase:
    """
    Create a new task.

    Args:
        task (TaskCreate): The task data to create.

    Returns:
        TaskBase: The created task object.
    """
    return TaskService(session).create(task)

@router.put("/tasks/{task_id}")
async def update_task(
    task_id: int, 
    task: TaskUpdate, 
    session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> TaskBase:
    """
    Update an existing task.

    Args:
        task_id (int): The ID of the task to update.
        task (TaskUpdate): The updated task data.

    Returns:
        TaskBase: The updated task object.
    """
    return TaskService(session).update(task_id, task)

@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int, 
    session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> int:
    """
    Delete a task.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        TaskBase: The deleted task object.
    """
    return TaskService(session).delete(task_id)
