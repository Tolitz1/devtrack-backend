# """
# Project model definition.

# Represents a project owned by a user.
# """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Project(Base):
    # """
    # SQLAlchemy ORM model for projects table.
    # """

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", backref="projects")