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
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    is_admin = Column(Integer, default=0) 
    office = Column(String, nullable=False)
    position = Column(String, nullable=False)