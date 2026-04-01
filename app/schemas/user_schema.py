from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str
    
class UserResponsive(BaseModel):
    id: int 
    username:str
    role: str
    created_id: datetime
    
    class Config:
        from_attributes= True