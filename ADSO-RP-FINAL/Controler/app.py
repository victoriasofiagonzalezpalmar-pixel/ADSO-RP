import os, sys
PROYECTO_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROYECTO_RAIZ)

from flask import Flask
from flask_mysqldb import MySQL
from Config import Config
from Routes import loadRoutes

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)
app.mysql = mysql

loadRoutes(app)

if __name__ == "__main__":
    app.run(debug=True, port=6600, host="0.0.0.0")
