from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.crud.measurement_crud import *
from app.schemas.measurement_schema import MeasurementCreate
from app.core.dependencies.auth import get_current_user
from app.database.connection import get_db
from app.utils.logger import log_event
from app.services.autom_service import controlar_servos, controlar_luz

router= APIRouter(prefix="/measurements",tags=["Measurements"])

@router.post("/")
def create(
    measurement: MeasurementCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_m = create_measurement(db, measurement)

    acciones_servos=controlar_servos()
    acciones_luz=controlar_luz(measurement.light)
    
    return{
        "measurement":new_m,
        "servos":acciones_servos,
        "luz":acciones_luz
    }