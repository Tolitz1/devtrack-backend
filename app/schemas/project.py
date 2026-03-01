# """
# Pydantic schemas for Project.
# """

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    description: str | None = None


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str | None

    class Config:
        from_attributes = True