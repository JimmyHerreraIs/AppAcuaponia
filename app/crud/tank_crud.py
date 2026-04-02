from sqlalchemy.orm import Session 
from app.models.tank import Tank
from app.schemas.tank_schema import TankCreate

def create_tank(db:Session, tank: TankCreate):
    db_tank=Tank(**tank.dict())
    db.add(db_tank)
    db.commit()
    db.refresh(db_tank)
    return db_tank

def get_all_tanks(db:Session):
    return db.query(Tank).all()