from flask import Blueprint
from controllers.DatoClienteController import DatoclienteControllers

datocliente_bp = Blueprint("Datocliente", __name__)


@datocliente_bp.route("/", methods=["GET"])
def consult():
    return DatoclienteControllers.consult()


@datocliente_bp.route("/", methods=["POST"])
def add():
    return DatoclienteControllers.create()


@datocliente_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return DatoclienteControllers.update(id)


@datocliente_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return DatoclienteControllers.delete(id)
