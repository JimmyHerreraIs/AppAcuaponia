from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings

# Configuración de hash
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

### Hash de Contraseña
def hash_password(password:str):
    return pwd_context.hash(password)
#Verificar la contraseña
def verify_password(texto_plano_password:str, hash_password:str)-> bool:
    return pwd_context.verify(texto_plano_password, hash_password)
#---Crear token-----
def create_access_token(data:dict):
    copia=data.copy()
    
    expire=datetime.utcnow()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    copia.update({"exp":expire})
    
    encoded_jwt= jwt.encode(
        copia,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt
#Verificar el token
def verify_token(token:str):
    try:
        payload= jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None