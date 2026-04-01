from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings

# Configuración de hash
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

### Hash de Contraseña
def hash_password(password:str):
    return pwd_context.hash(password)
