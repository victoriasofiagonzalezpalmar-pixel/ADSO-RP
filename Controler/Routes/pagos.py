from flask import Blueprint
from controllers.PagoController import PagosControllers

pagos_bp = Blueprint("Pagos", __name__)


@pagos_bp.route("/", methods=["GET"])
def consult():
    return PagosControllers.consult()


@pagos_bp.route("/", methods=["POST"])
def add():
    return PagosControllers.create()


@pagos_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return PagosControllers.update(id)


@pagos_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return PagosControllers.delete(id)
