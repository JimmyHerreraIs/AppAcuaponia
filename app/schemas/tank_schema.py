from pydantic import BaseModel
from typing import Optional

class TankBase(BaseModel):
    nombre:str
    ubicacion:Optional[str]=None
    capacidad: Optional[str]=None
    
class TankCreate(TankBase):
    pass

class TankUpdate(BaseModel):
    nombre: Optional[str]=None
    ubicacion: Optional[str]=None
    capacidad:Optional[float]=None
    
class TankResponsive(TankBase):
    id: int
    
    class Config:
        from_attributes= True
        