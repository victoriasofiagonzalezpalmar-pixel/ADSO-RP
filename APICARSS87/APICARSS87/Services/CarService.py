from flask import current_app
from Models.Car import Car

# opereraciones CRUD-> create, read, update, delete
class CarService:

    def add():
        pass

    def update():
        pass

    def delete():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_car"
        c.execute(query)
        data = c.fetchall()
        print(data)

        x = [ Car(w[0], w[1],w[2],w[3],w[4],w[5],w[6]).to_dict()  for w in data ]    
        return x

