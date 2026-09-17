from flask import Blueprint
from Controllers.AlmacenaController import AlmacenaController

almacena_bp = Blueprint("Almacena", __name__)

@almacena_bp.route("/", methods=["GET"])
def consult():
    return AlmacenaController.read()

@almacena_bp.route("/", methods=["POST"])
def add():
    return AlmacenaController.add()

@almacena_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return AlmacenaController.update(rid)

@almacena_bp.route("/<string:uuid>", methods=["DELETE"])
def delete(uuid):
    return AlmacenaController.delete(uuid)
