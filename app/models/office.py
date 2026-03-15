from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.core.database import Base

class Office(Base):
    # """
    # SQLAlchemy ORM model for Offices table.
    # """

    __tablename__ = "offices"

    id = Column(Integer, primary_key=True, index=True)
    office_name = Column(String(100), nullable=False)
    office_code = Column(String(10), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )