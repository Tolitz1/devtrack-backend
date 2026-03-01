# """
# Project routes.
# """

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.project import ProjectCreate, ProjectResponse
from app.models.project import Project
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User
from fastapi import HTTPException

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # """
    # Create a project for authenticated user.
    # """

    new_project = Project(
        title=project.title,
        description=project.description,
        owner_id=current_user.id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/", response_model=list[ProjectResponse])
def get_my_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # """
    # Get projects owned by authenticated user.
    # """

    projects = db.query(Project).filter(Project.owner_id == current_user.id).all()

    return projects

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # """
    # Update project only if owned by current user.
    # """

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    project.title = project_data.title
    project.description = project_data.description

    db.commit()
    db.refresh(project)

    return project

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # """
    # Delete project only if owned by current user.
    # """

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully"}