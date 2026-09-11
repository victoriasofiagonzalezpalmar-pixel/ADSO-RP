from flask import Blueprint
from Controllers.PagosController import PagosController

pagos_bp = Blueprint("Pagos", __name__)

@pagos_bp.route("/", methods=["GET"])
def consult():
    return PagosController.read()

@pagos_bp.route("/", methods=["POST"])
def add():
    return PagosController.add()

@pagos_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return PagosController.update(rid)

@pagos_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return PagosController.delete(rid)
