from flask import flask
from flask_mysqldb import MYSQL
from config import config
from Routes import loadRoutes

app = flask(__name__)

app,config.from_object(config)
mysql = MYSQL(app)

app.mysql = mysql

loadRoutes(app)


app.run(debug=True,port=6600, host='0.0.0.0')

