# """
# Task model definition.

# Represents a task inside a project.
# """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="todo")

    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"))

    project = relationship("Project", backref="tasks")