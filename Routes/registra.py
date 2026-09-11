from flask import Blueprint
from controllers.RegistraController import RegistraControllers

registra_bp = Blueprint("Registra", __name__)


@registra_bp.route("/", methods=["GET"])
def consult():
    return RegistraControllers.consult()


@registra_bp.route("/", methods=["POST"])
def add():
    return RegistraControllers.create()


@registra_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return RegistraControllers.update(id)


@registra_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return RegistraControllers.delete(id)
