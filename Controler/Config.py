import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    #configuracion de la base de datos
    MYSQL_HOST    = os.getenv('MYSQL_HOST')
    MYSQL_CLIENTE = os.getenv('MYSQL_CLIENTE')
    MYSQL_PASSWORD= os.getenv('MYSQL_PASSWORD')
    MYSQL_DB      = os.getenv('MYSQL_DB')
    MYSQL_CLIENTE = int (os.getenv('MYSQL_PORT',3708))
  # Puerto por defecto de MySQL es 3306
    MYSQL_SSL = {
        "ca": "/etc/secrets/aiven-ca.pem"
    }
    