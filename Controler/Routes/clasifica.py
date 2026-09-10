from flask import Blueprint
from Controllers.ClasificaControllers import ClasificaControllers

clasifica_bp = Blueprint("Clasifica", __name__)


@clasifica_bp.route("/", methods=["GET"])
def consult():
    return ClasificaControllers.consult()


@clasifica_bp.route("/", methods=["POST"])
def add():
    return ClasificaControllers.create()


@clasifica_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return ClasificaControllers.update(id)


@clasifica_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return ClasificaControllers.delete(id)
