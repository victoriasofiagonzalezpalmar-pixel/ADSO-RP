from flask import Blueprint
from Controllers.DescripcionControllers import DescripcionControllers

descripcion_bp = Blueprint("Descripcion", __name__)


@descripcion_bp.route("/", methods=["GET"])
def consult():
    return DescripcionControllers.consult()


@descripcion_bp.route("/", methods=["POST"])
def add():
    return DescripcionControllers.create()


@descripcion_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return DescripcionControllers.update(id)


@descripcion_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return DescripcionControllers.delete(id)
