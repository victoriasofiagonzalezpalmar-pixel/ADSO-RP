from flask import Blueprint
from Controllers.DatoproveedorControllers import DatoproveedorControllers

datoproveedor_bp = Blueprint("Datoproveedor", __name__)


@datoproveedor_bp.route("/", methods=["GET"])
def consult():
    return DatoproveedorControllers.consult()


@datoproveedor_bp.route("/", methods=["POST"])
def add():
    return DatoproveedorControllers.create()


@datoproveedor_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return DatoproveedorControllers.update(id)


@datoproveedor_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return DatoproveedorControllers.delete(id)
