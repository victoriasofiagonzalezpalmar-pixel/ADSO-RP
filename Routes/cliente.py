from flask import Blueprint
from Controllers.ClienteControllers import ClienteControllers

cliente_bp = Blueprint("Cliente", __name__)


@cliente_bp.route("/", methods=["GET"])
def consult():
    return ClienteControllers.consult()


@cliente_bp.route("/", methods=["POST"])
def add():
    return ClienteControllers.create()


@cliente_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return ClienteControllers.update(id)


@cliente_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return ClienteControllers.delete(id)
