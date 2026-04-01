from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database.base import Base

class Tank(Base):
    __tablename__='tank'
    
    id=Column(Integer, primary_key=True, index=True)
    nombre=Column(String, nullable=False)
    ubicacion=Column(String,nullable=True)
    capacidad=Column(Float,nullable=True)
    
    fish=relationship('Fish', back_populates="tank")