import os
from dotenv import load_dotenv

# Busca el .env en varias ubicaciones (carpeta actual, Controler, raiz del proyecto)
_ruta_actual = os.path.dirname(os.path.abspath(__file__))
_raiz = os.path.dirname(_ruta_actual)
for _posible in [os.path.join(_ruta_actual, ".env"), os.path.join(_raiz, ".env"), ".env"]:
    if os.path.exists(_posible):
        load_dotenv(_posible)
        break
else:
    load_dotenv()

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "aplicli33")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_CONNECT_TIMEOUT = 5
