from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.user_schema import UserCreate, UserLogin
from app.crud.user_crud import create_user, get_user_by_username
from app.core.security import verify_password, create_access_token
from app.database.connection import get_db
from app.utils.logger import log_event, log_error

router= APIRouter(prefix="/users",tags=["Users"])
#Creacion usuario
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)

    if existing_user:
        log_error(f"Registro fallido: usuario ya existe -> {user.username}")
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    new_user = create_user(db, user)

    log_event(f"Usuario creado: {user.username}")

    return {"message": "Usuario creado correctamente"}
#dependencias DB (importado)
#-------Registro-------
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = get_user_by_username(db, user.username)

        if not db_user:
            return {"error": "usuario no existe"}

        if not verify_password(user.password, db_user.password_hash):
            return {"error": "password incorrecto"}

        token = create_access_token(data={"sub": db_user.username})

        return {"access_token": token, "token_type": "bearer"}

    except Exception as e:
        print("🔥🔥🔥 ERROR REAL:", repr(e))
        return {"error": str(e)}