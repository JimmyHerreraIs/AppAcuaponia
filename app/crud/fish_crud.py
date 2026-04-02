from sqlalchemy.orm import Session
from app.models.fish import Fish
from app.schemas.fish_schema import FishCreate, FishUpdate

#--------Crear---------
def create_fish(db:Session, fish:FishCreate):
    db_fish= Fish(**fish.dict())
    db.add(db_fish)
    db.commit()
    db.refresh(db_fish)
    return db_fish
#---------Leer---------
def get_all_fish(db:Session):
    return db.query(Fish).all()

def get_fish_by_id(db:Session, fish_id: int):
    return db.query(Fish).filter(Fish.id==fish_id).first()

#--------Update---------
def update_fish(db:Session, fish_id:int , fish_update: FishUpdate):
    db_fish= get_fish_by_id(db,fish_id)
    
    if not db_fish:
        return None
    
    update_data=fish_update.dict(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_fish, key, value)
    db.commit()
    db.refresh(db_fish)
    return db_fish
#----------Delete--------
def delete_fish(db:Session, fish_id: int):
    db_fish= get_fish_by_id(db, fish_id)
    
    if not db_fish:
        return None
    db.delete(db_fish)
    db.commit()
    return db_fish