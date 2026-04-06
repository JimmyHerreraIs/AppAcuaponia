from datetime import datetime, timedelta

servo_motor_1=None
servo_motor_2=None
servo_motor_3=None

def controlar_servos():
    global servo_motor_1,servo_motor_1,servo_motor_3
    
    ahora=datetime.now()
    acciones=[]
    #Cada 3 días por 60 segundos
    if not servo_motor_1 or(ahora-servo_motor_1)>=timedelta(days=3):
        acciones.append({
            "servo":1,
            "acciones":"activar",
            "duracion_segundos":60
        })
        servo_motor_1=ahora
    #Servo 2 cada 14 días por 15 segundos
    if not servo_motor_2 or (ahora-servo_motor_2)>=timedelta(days=14):
        acciones.append({
            "servo":2,
            "accion":"activar",
            "duracion_segundos":15
        })
        servo_motor_2= ahora
    #Servo 3 cada 12 horas por 30 segundos
    if not servo_motor_3 or ( ahora-servo_motor_3)>= timedelta(hours=12):
        acciones.append({
            "servo": 3,
            "accion": "activar",
            "duracion_segundos": 30
        })
        servo_motor_3=ahora
        
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
        
    