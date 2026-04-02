from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.crud.fish_crud import *
from app.schemas.fish_schema import FishCreate, FishUpdate
from app.core.dependencies.auth import get_current_user
from app.database.connection import get_db

router = APIRouter(prefix="/fish",tags=["Fish"])

#------CREATE-----
@router.post("/")
def create(fish:FishCreate, db:Session=Depends(get_db),user=Depends(get_current_user)):
    return create_fish(db,fish)

#-------READ------
@router.get("/")
def get_all(db:Session=Depends(get_db),user=Depends(get_current_user)):
    return get_all_fish(db)

#------UPDATE-----
@router.put("/{fish_id}")
def update(fish_id:int, fish: FishUpdate,db:Session=Depends(get_db),user=Depends(get_current_user)):
    updated=update_fish(db,fish_id, fish)
    
    if not updated:
        raise HTTPException(status_code=404, detail='Pescado no encontrado')
    return updated

#-------DELETE------
@router.delete("/{fish_id}")
def delete(fish_id: int, db:Session=Depends(get_db),user=Depends(get_current_user)):
    deleted=delete_fish(db,fish_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="Pescado no encontrado")
    
    return deleted