from flask import Blueprint
from Controllers.DevolucionControllers import DevolucionControllers

devolucion_bp = Blueprint("Devolucion", __name__)


@devolucion_bp.route("/", methods=["GET"])
def consult():
    return DevolucionControllers.consult()


@devolucion_bp.route("/", methods=["POST"])
def add():
    return DevolucionControllers.create()


@devolucion_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return DevolucionControllers.update(id)


@devolucion_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return DevolucionControllers.delete(id)
