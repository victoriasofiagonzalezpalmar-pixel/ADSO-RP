from flask import Blueprint
from Controllers.CompraControllers import CompraControllers

compra_bp = Blueprint("Compra", __name__)


@compra_bp.route("/", methods=["GET"])
def consult():
    return CompraControllers.consult()


@compra_bp.route("/", methods=["POST"])
def add():
    return CompraControllers.create()


@compra_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return CompraControllers.update(id)


@compra_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return CompraControllers.delete(id)
