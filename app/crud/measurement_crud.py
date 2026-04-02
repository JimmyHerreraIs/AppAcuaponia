from sqlalchemy.orm import Session
from app.models.measurement import Measurement
from app.schemas.measurement_schema import MeasurementCreate

def create_measurement(db:Session, measurement: MeasurementCreate):
    db_measurement= Measurement(**measurement.dict())
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement

def get_measurements_by_fish(db:Session, fish_id:int):
    return db.query(Measurement).filter(Measurement.fish_id==fish_id).all()