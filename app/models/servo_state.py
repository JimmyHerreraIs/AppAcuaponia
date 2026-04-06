from sqlalchemy import Column, Integer, String, DateTime
from app.database.base import Base

class ServoState(Base):
    __tablename__='servo_states'
    
    id=Column(Integer, primary_key=True, index=True)
    nombre=Column(String, unique=True, index=True)
    last_activacion=Column(DateTime)