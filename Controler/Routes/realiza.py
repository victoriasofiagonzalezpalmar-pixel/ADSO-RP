from flask import Blueprint
from controllers.RealizaController import RealizaControllers

realiza_bp = Blueprint("Realiza", __name__)


@realiza_bp.route("/", methods=["GET"])
def consult():
    return RealizaControllers.consult()


@realiza_bp.route("/", methods=["POST"])
def add():
    return RealizaControllers.create()


@realiza_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return RealizaControllers.update(id)


@realiza_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return RealizaControllers.delete(id)
