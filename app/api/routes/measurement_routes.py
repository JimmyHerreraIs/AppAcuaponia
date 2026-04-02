from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.crud.measurement_crud import *
from app.schemas.measurement_schema import MeasurementCreate
from app.core.dependencies.auth import get_current_user
from app.database.connection import get_db

router= APIRouter(prefix="/measurements",tags=["Measurements"])

@router.post("/")
def create(measurement: MeasurementCreate, db:Session= Depends(get_db),user=Depends(get_current_user)):
    return create_measurement(db,measurement)

def get_by_fish(fish_id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    return get_measurements_by_fish(db,fish_id)