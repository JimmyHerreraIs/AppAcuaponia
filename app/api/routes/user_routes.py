from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.user_schema import UserCreate, UserLogin
from app.crud.user_crud import create_user, get_user_by_username
from app.core.security import verify_password, create_access_token
from app.database.connection import get_db
from app.utils.logger import log_event, log_error

router= APIRouter(prefix="/users",tags=["Users"])

#dependencias DB (importado)
#-------Registro-------
@router.post("/login")
def login(user:UserLogin,db: Session= Depends(get_db)):
    db_user= get_user_by_username(db, user.username)
    
    if not db_user:
        log_error(f"Login fallido: usuario no existe -> {user.username}")
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    if not verify_password(user.password, db_user.password_hash):
        log_error(f"Login fallido: contraseña incorrecta -> {user.username}")
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    log_event(f"Login exitoso: {user.username}")

    token = create_access_token({"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}