from sqlalchemy.orm import Session
from app.models.servo_state import ServoState
from datetime import datetime
def get_servo(db:Session, nombre:str):
    return db.query(ServoState).filter(ServoState.nombre==nombre).first()

def update_servo(db:Session, nombre:str):
    servo=get_servo(db,nombre)
    
    
    
    if not servo:
        servo=ServoState(nombre=nombre,last_activation=datetime.now())
        db.add(servo)
    else:
        servo.last_activacion=datetime.now()
    
    db.commit()
    db.refresh(servo)
    return servo