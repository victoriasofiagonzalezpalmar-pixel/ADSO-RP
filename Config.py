import os
from dotenv import load_dotenv

# Busca el .env en la raiz del proyecto (un nivel arriba de Controler/)
_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_raiz, ".env"))

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "aplicli33")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
