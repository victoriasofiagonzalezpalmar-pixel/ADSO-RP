from flask import Blueprint
from Controllers.CategoriaControllers import CategoriaControllers

categoria_bp = Blueprint("Categoria", __name__)


@categoria_bp.route("/", methods=["GET"])
def consult():
    return CategoriaControllers.consult()


@categoria_bp.route("/", methods=["POST"])
def add():
    return CategoriaControllers.create()


@categoria_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return CategoriaControllers.update(id)


@categoria_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return CategoriaControllers.delete(id)
