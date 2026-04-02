from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password

#------Crear-----
def create_user(db:Session, user:UserCreate):
    hashed_password=hash_password(user.password)
    
    db_user= User(
        username=user.username,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
#---Obtener el user por su username----
def get_user_by_username(db:Session, username:str):
    return db.query(User).filter(User.username==username).first()

