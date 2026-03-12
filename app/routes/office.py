from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.office import OfficeCreate, OfficeResponse
from app.models.office import Office
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/offices", tags=["Offices"])

@router.post("/", response_model=OfficeResponse)
def create_office(
    office_in: OfficeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Not authorized. Admin access required."
        )

    existing = (
        db.query(Office)
        .filter(
            (Office.office_code == office_in.office_code) |
            (Office.office_name == office_in.office_name)
        )
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Office with this name or code already exists"
        )

    new_office = Office(
        office_name=office_in.office_name,
        office_code=office_in.office_code,
    )
    db.add(new_office)
    db.commit()
    db.refresh(new_office)
    return new_office