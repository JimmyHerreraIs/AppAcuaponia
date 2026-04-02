from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.crud.measurement_crud import *
from app.schemas.measurement_schema import MeasurementCreate
from app.core.dependencies.auth import get_current_user
from app.database.connection import get_db
from app.utils.logger import log_event
router= APIRouter(prefix="/measurements",tags=["Measurements"])

@router.post("/")
def create(
    measurement: MeasurementCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_m = create_measurement(db, measurement)

    log_event(f"Medición creada para fish {measurement.fish_id}")

    return new_m