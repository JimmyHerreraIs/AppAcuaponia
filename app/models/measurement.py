from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.database.base import Base
from datetime import datetime

class Measurement(Base):
    __tablename__="measurement"
    
    id=Column(Integer, primary_key=True, index=True)
    
    fish_id= Column(Integer, ForeignKey("fish.id"), nullable=False)
    fecha=Column(DateTime, default=datetime.utcnow)
    peso=Column(Float, nullable=True)
    tamaño=Column(Float, nullable=True)
    
    oxigeno_consumido=Column(Float,nullable=True)
    temperatura=Column(Float, nullable=True)
    ph=Column(Float, nullable=True)
    fish= relationship("Fish", back_populates="measurements")
    #Indices en python
    __table_args__=(
        Index("idx_fish_id", "fish_id"),
        Index("idx_fecha", "fecha"),
    )