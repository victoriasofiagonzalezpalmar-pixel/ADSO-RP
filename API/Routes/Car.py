from flask import Blueprint
from Controllers.CarController import CarController

car_bp = Blueprint("car",__name__)

@car_bp.route('/', methods=["get"])
def home():
    data = CarController.read()
    return data

@car_bp.route('/', methods=["post"])
def add():     
    return "yuiuyyu"

@car_bp.route('/<id>', methods=["delete"])
def delete(id):     
    return "yuiuyyu"
