from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FishBase(BaseModel):
    especie:str
    tamaño_inicial: Optional[float]=None
    peso_inicial: Optional[float]=None
    estado: Optional[str]=None
    tank_id:Optional[int]= None
    
class FishCreate(FishBase):
    pass

class FishUpdate(FishBase):
    especie:Optional[str]=None
    tamaño_inicial: Optional[float]=None
    peso_inicial: Optional[float]=None
    estado: Optional[str]=None
    tank_id:Optional[int]= None

class FishResponse(FishBase):
    id: int
    class Config:
        from_attributes= True
        