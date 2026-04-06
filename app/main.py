from fastapi import FastAPI
from app.api.router import api_router
from app.models import servo_state
from app.database.session import engine 
from app.database.base import Base

app=FastAPI()
Base.metadata.create_all(bind=engine)#
app.include_router(api_router)