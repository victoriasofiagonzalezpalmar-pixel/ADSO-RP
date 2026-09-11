from flask import Blueprint
from controllers.ProveedorController import ProveedorControllers

proveedor_bp = Blueprint("Proveedor", __name__)


@proveedor_bp.route("/", methods=["GET"])
def consult():
    return ProveedorControllers.consult()


@proveedor_bp.route("/", methods=["POST"])
def add():
    return ProveedorControllers.create()


@proveedor_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return ProveedorControllers.update(id)


@proveedor_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return ProveedorControllers.delete(id)
