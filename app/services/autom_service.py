from datetime import datetime, timedelta
from app.crud.servo_crud import get_servo, update_servo


def controlar_servos(db):
    ahora=datetime.now()
    acciones=[]
    #Cada 3 días por 60 segundos
    #Servo 1
    
    servo1=get_servo(db,"servo_1")
    if not servo1 or(ahora-servo1.last_activacion)>=timedelta(days=3):
        acciones.append({
            "servo":1,
            "duracion_segundos":60
        })
        update_servo(db,"servo_1")
    #Servo 2 cada 14 días por 15 segundos
    servo2=get_servo(db,"servo2")
    if not servo2 or (ahora-servo2.last_activacion)>=timedelta(days=14):
        acciones.append({
            "servo":2,
            "duracion_segundos":15
        })
        update_servo(db,"servo_2")

    #Servo 3 cada 12 horas por 30 segundos
    servo3=get_servo(db,"servo_3")
    if not servo3 or ( ahora-servo3.last_activacion)>= timedelta(hours=12):
        acciones.append({
            "servo": 3,
            "duracion_segundos": 30
        })
        update_servo(db,"servo_3")
        
    return acciones

def controlar_luz(hay_luz: bool):
    ahora = datetime.now()
    hora = ahora.hour

    acciones = []

    if hora >= 6:
        if not hay_luz:
            acciones.append("Encender LEDs")
        else:
            acciones.append("Apagar LEDs")

    return acciones
        
    