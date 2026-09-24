from flask import Blueprint
from Controllers.DatoClienteController import DatoClienteController

datocliente_bp = Blueprint("DatoCliente", __name__)

@datocliente_bp.route("/", methods=["GET"])
def consult():
    return DatoClienteController.read()

@datocliente_bp.route("/", methods=["POST"])
def add():
    return DatoClienteController.add()

@datocliente_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return DatoClienteController.update(rid)

@datocliente_bp.route("/<string:uuid>", methods=["DELETE"])
def delete(uuid):
    return DatoClienteController.delete(uuid)
