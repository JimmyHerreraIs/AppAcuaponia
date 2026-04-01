from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey,String
from sqlalchemy.orm import relationship
from app.database.base import Base
from datetime import datetime

class Fish(Base):
    __tablename__='fish'
    
    id=Column(Integer, primary_key=True, index=True)
    especie=Column(String,nullable=False)
    fecha_ingreso=Column(DateTime,default=datetime.utcnow)
    
    tamaño_inicial=Column(Float,nullable=True)
    peso_inicial=Column(Float,nullable=True)
    estado=Column(String, default="vivo")#activo
    tank_id=Column(Integer, ForeignKey("tank.id"),nullable=True)
    
    tank=relationship("Tank", back_populates="fish")
    measurements=relationship(
        "Measurement",
        back_populates="fish",
        cascade="all , delete-orphan"
    )