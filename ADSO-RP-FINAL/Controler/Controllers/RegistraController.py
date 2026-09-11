from flask import jsonify, request
from Services.registraServices import RegistraServices

class RegistraController:

    @staticmethod
    def read():
        data = RegistraServices.read()
        return jsonify({"mensaje": data}), 200

    @staticmethod
    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400
        requeridos = ["usu_id", "com_id"]
        falta = [x for x in requeridos if x not in data]
        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400
        nuevo = RegistraServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": nuevo}), 201

    @staticmethod
    def update(rid):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400
        requeridos = ["usu_id", "com_id"]
        falta = [x for x in requeridos if x not in data]
        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400
        result = RegistraServices.update(rid, data)
        if result is None:
            return jsonify({"mensaje": "No se encontro el registro"}), 404
        return jsonify({"mensaje": "Se actualizo correctamente", "data": result}), 200

    @staticmethod
    def delete(rid):
        rowcount = RegistraServices.delete(rid)
        if rowcount == 0:
            return jsonify({"mensaje": "No se encontro el registro"}), 404
        return jsonify({"mensaje": "Se elimino correctamente"}), 200
