from flask import Blueprint
from Controllers.CategoriaController import CategoriaController

categoria_bp = Blueprint("Categoria", __name__)

@categoria_bp.route("/", methods=["GET"])
def consult():
    return CategoriaController.read()

@categoria_bp.route("/", methods=["POST"])
def add():
    return CategoriaController.add()

@categoria_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return CategoriaController.update(rid)

@categoria_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return CategoriaController.delete(rid)
