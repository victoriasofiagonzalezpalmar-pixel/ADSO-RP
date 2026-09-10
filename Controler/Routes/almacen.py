from flask import Blueprint
from controllers.AlmacenaController import AlmacenControllers

almacen_bp = Blueprint("Almacen", __name__)


@almacen_bp.route("/", methods=["GET"])
def consult():
    return AlmacenControllers.consult()


@almacen_bp.route("/", methods=["POST"])
def add():
    return AlmacenControllers.create()


@almacen_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return AlmacenControllers.update(id)


@almacen_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return AlmacenControllers.delete(id)
