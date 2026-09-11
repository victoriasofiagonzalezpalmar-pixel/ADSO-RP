from flask import Blueprint
from Controllers.UsuarioController import UsuarioController

usuario_bp = Blueprint("Usuario", __name__)

@usuario_bp.route("/", methods=["GET"])
def consult():
    return UsuarioController.read()

@usuario_bp.route("/", methods=["POST"])
def add():
    return UsuarioController.add()

@usuario_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return UsuarioController.update(rid)

@usuario_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return UsuarioController.delete(rid)
