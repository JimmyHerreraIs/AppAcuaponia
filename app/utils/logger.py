import logging 
import os

#se crea la carpeta logs
if not os.path.exists("logs"):
    os.makedirs("logs")
    
#Configuracion
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname) -%(message)s"
)

def log_event(message: str):
    logging.info(message)
    
def log_error(message:str):
    logging.error(message)