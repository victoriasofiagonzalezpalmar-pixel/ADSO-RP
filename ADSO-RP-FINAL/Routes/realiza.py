from flask import Blueprint
from Controllers.RealizaController import RealizaController

realiza_bp = Blueprint("Realiza", __name__)

@realiza_bp.route("/", methods=["GET"])
def consult():
    return RealizaController.read()

@realiza_bp.route("/", methods=["POST"])
def add():
    return RealizaController.add()

@realiza_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return RealizaController.update(rid)

@realiza_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return RealizaController.delete(rid)
