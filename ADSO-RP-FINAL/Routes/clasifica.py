from flask import Blueprint
from Controllers.ClasificaController import ClasificaController

clasifica_bp = Blueprint("Clasifica", __name__)

@clasifica_bp.route("/", methods=["GET"])
def consult():
    return ClasificaController.read()

@clasifica_bp.route("/", methods=["POST"])
def add():
    return ClasificaController.add()

@clasifica_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return ClasificaController.update(rid)

@clasifica_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return ClasificaController.delete(rid)
