from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskResponse
from app.models.task import Task
from app.models.project import Project
from app.models.user import User
from app.core.database import get_db
from app.core.auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/{project_id}", response_model=TaskResponse)
def create_task(
    project_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # """
    # Create task inside a project owned by user.
    # """

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        project_id=project_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/{project_id}", response_model=list[TaskResponse])
def get_tasks(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # """
    # Get tasks inside project owned by user.
    # """

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    tasks = db.query(Task).filter(Task.project_id == project_id).all()

    return tasks