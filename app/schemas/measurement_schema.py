from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MeasurementBase(BaseModel):
    fish_id:int
    peso: Optional[float]= None
    tamaño: Optional[float]=None
    oxigeno_consumido:Optional[float]=None
    temperatura:Optional[float]=None
    ph: Optional[float]=None
    
class MeasurementCreate(MeasurementBase):
    pass

class MeasurementUpdate(MeasurementBase):
    peso: Optional[float]= None
    tamaño: Optional[float]=None
    oxigeno_consumido:Optional[float]=None
    temperatura:Optional[float]=None
    ph: Optional[float]=None
    
class MeasurementResponse(MeasurementBase):
    id: int
    fecha: datetime
    class Config:
        from_attributes= True