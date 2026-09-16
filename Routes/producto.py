from flask import Blueprint
from Controllers.ProductoController import ProductoController

producto_bp = Blueprint("Producto", __name__)

@producto_bp.route("/", methods=["GET"])
def consult():
    return ProductoController.read()

@producto_bp.route("/", methods=["POST"])
def add():
    return ProductoController.add()

@producto_bp.route("/<int:rid>", methods=["PUT"])
def update(rid):
    return ProductoController.update(rid)

@producto_bp.route("/<int:rid>", methods=["DELETE"])
def delete(rid):
    return ProductoController.delete(rid)
