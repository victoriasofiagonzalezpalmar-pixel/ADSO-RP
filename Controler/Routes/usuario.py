from flask import Blueprint
from Controllers.UsuarioControllers import UsuarioControllers

usuario_bp = Blueprint("Usuario", __name__)


@usuario_bp.route("/", methods=["GET"])
def consult():
    return UsuarioControllers.consult()


@usuario_bp.route("/", methods=["POST"])
def add():
    return UsuarioControllers.create()


@usuario_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return UsuarioControllers.update(id)


@usuario_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return UsuarioControllers.delete(id)
