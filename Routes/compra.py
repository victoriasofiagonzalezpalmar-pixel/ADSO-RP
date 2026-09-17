from flask import Blueprint
from Controllers.CompraController import CompraController

compra_bp = Blueprint("Compra", __name__)

@compra_bp.route("/", methods=["GET"])
def consult():
    return CompraController.read()

@compra_bp.route("/", methods=["POST"])
def add():
    return CompraController.add()

@compra_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return CompraController.update(rid)

@compra_bp.route("/<string:uuid>", methods=["DELETE"])
def delete(uuid):
    return CompraController.delete(uuid)
