from flask import Blueprint
from Controllers.DatoProveedorController import DatoProveedorController

datoproveedor_bp = Blueprint("DatoProveedor", __name__)

@datoproveedor_bp.route("/", methods=["GET"])
def consult():
    return DatoProveedorController.read()

@datoproveedor_bp.route("/", methods=["POST"])
def add():
    return DatoProveedorController.add()

@datoproveedor_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return DatoProveedorController.update(rid)

@datoproveedor_bp.route("/<string:uuid>", methods=["DELETE"])
def delete(uuid):
    return DatoProveedorController.delete(uuid)
