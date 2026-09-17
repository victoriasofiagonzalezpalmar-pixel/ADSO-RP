from flask import Blueprint
from Controllers.DevolucionController import DevolucionController

devolucion_bp = Blueprint("Devolucion", __name__)

@devolucion_bp.route("/", methods=["GET"])
def consult():
    return DevolucionController.read()

@devolucion_bp.route("/", methods=["POST"])
def add():
    return DevolucionController.add()

@devolucion_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return DevolucionController.update(rid)

@devolucion_bp.route("/<string:uuid>", methods=["DELETE"])
def delete(uuid):
    return DevolucionController.delete(uuid)
