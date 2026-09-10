from flask import Blueprint
from Controllers.ProductoControllers import ProductoControllers

producto_bp = Blueprint("Producto", __name__)


@producto_bp.route("/", methods=["GET"])
def consult():
    return ProductoControllers.consult()


@producto_bp.route("/", methods=["POST"])
def add():
    return ProductoControllers.create()


@producto_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return ProductoControllers.update(id)


@producto_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return ProductoControllers.delete(id)
