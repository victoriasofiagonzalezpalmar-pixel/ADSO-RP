from flask import Blueprint
from Controllers.ClienteController import ClienteController

cliente_bp = Blueprint("Cliente", __name__)

@cliente_bp.route("/", methods=["GET"])
def consult():
    return ClienteController.read()

@cliente_bp.route("/", methods=["POST"])
def add():
    return ClienteController.add()

@cliente_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return ClienteController.update(rid)

@cliente_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return ClienteController.delete(rid)
