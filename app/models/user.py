# """
# User model definition.

# Represents application users in the database.
# This table will store authentication credentials
# and basic identity information.
# """

from sqlalchemy import Column, Integer, String
from app.core.database import Base


class User(Base):
    # """
    # SQLAlchemy ORM model for users table.
    # """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)