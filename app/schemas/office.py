from pydantic import BaseModel
from datetime import datetime

class OfficeCreate(BaseModel):
    office_name: str
    office_code: str

class OfficeResponse(BaseModel):
    id: int
    office_name: str
    office_code: str
    created_at: datetime

    class Config:
        from_attributes = True