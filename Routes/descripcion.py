from flask import Blueprint
from Controllers.DescripcionController import DescripcionController

descripcion_bp = Blueprint("Descripcion", __name__)

@descripcion_bp.route("/", methods=["GET"])
def consult():
    return DescripcionController.read()

@descripcion_bp.route("/", methods=["POST"])
def add():
    return DescripcionController.add()

@descripcion_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return DescripcionController.update(rid)

@descripcion_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return DescripcionController.delete(rid)
