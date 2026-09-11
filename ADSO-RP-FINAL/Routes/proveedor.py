from flask import Blueprint
from Controllers.ProveedorController import ProveedorController

proveedor_bp = Blueprint("Proveedor", __name__)

@proveedor_bp.route("/", methods=["GET"])
def consult():
    return ProveedorController.read()

@proveedor_bp.route("/", methods=["POST"])
def add():
    return ProveedorController.add()

@proveedor_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return ProveedorController.update(rid)

@proveedor_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return ProveedorController.delete(rid)
