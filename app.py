from flask import Flask
from flask_mysqldb import MySQL
from Config import Config
from Routes import loadRoutes

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)
app.mysql = mysql

loadRoutes(app)

app.run(debug=True, port=6600, host='0.0.0.0')
