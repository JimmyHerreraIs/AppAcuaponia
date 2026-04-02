from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db, SessionLocal
from app.crud.tank_crud import *
from app.schemas.tank_schema import TankCreate
from app.core.dependencies.auth import get_current_user

router= APIRouter(prefix="/tanks",tags=["Tanks"])

@router.post("/")
def create(tank:TankCreate, db:Session=Depends(get_db),user= Depends(get_current_user)):
    return create_tank(db,tank)

@router.get("/")
def get_all(db:Session=Depends(get_db),user=Depends(get_current_user)):
    return get_all_tanks(db)