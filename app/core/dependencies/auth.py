from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User
from app.core.security import verify_token

security= HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials=Depends(security),
    db:Session = Depends(get_db)
):
    token=credentials.credentials
    payload=verify_token(token)
    
    if payload in None:
        raise HTTPException(status_code=401, detail="Token invalido")
    
    username=payload.get("sub")
    
    user=db.query(User).filter(User.username==username).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return user