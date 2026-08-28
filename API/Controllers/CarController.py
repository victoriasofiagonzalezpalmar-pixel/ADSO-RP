from flask import jsonify, request
from Services.CarService import CarService

class CarController:

    def read():
        data = CarService.read()
        return jsonify({"mensaje":data})


# blueprint