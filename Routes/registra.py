from flask import Blueprint
from Controllers.RegistraController import RegistraController

registra_bp = Blueprint("Registra", __name__)

@registra_bp.route("/", methods=["GET"])
def consult():
    return RegistraController.read()

@registra_bp.route("/", methods=["POST"])
def add():
    return RegistraController.add()

@registra_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return RegistraController.update(rid)

@registra_bp.route("/<string:uuid>", methods=["DELETE"])
def delete(uuid):
    return RegistraController.delete(uuid)
