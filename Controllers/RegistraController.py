from flask import jsonify, request
from Services.registraServices import RegistraServices

class RegistraController:

    @staticmethod
    def read():
        try:
            data = RegistraServices.read()
            return jsonify({"mensaje": data, "total": len(data), "status": "ok"}), 200
        except Exception as e:
            return jsonify({"mensaje": "Error al consultar", "error": str(e), "status": "error"}), 500

    @staticmethod
    def add():
        try:
            data = request.get_json(silent=True)
            if not data:
                return jsonify({"mensaje": "El cuerpo esta vacio o invalido", "status": "error"}), 400
            requeridos = ["usu_id", "com_id"]
            falta = [x for x in requeridos if x not in data]
            if falta:
                return jsonify({"mensaje": f"Faltan parametros: {falta}", "status": "error"}), 400
            nuevo = RegistraServices.add(data)
            return jsonify({"mensaje": "Se registro correctamente", "data": nuevo, "status": "ok"}), 201
        except Exception as e:
            return jsonify({"mensaje": "Error al registrar", "error": str(e), "status": "error"}), 500

    @staticmethod
    def update(rid):
        try:
            data = request.get_json(silent=True)
            if not data:
                return jsonify({"mensaje": "El cuerpo esta vacio o invalido", "status": "error"}), 400
            requeridos = ["usu_id", "com_id"]
            falta = [x for x in requeridos if x not in data]
            if falta:
                return jsonify({"mensaje": f"Faltan parametros: {falta}", "status": "error"}), 400
            result = RegistraServices.update(rid, data)
            if result is None:
                return jsonify({"mensaje": "No se encontro el registro", "status": "error"}), 404
            return jsonify({"mensaje": "Se actualizo correctamente", "data": result, "status": "ok"}), 200
        except Exception as e:
            return jsonify({"mensaje": "Error al actualizar", "error": str(e), "status": "error"}), 500

    @staticmethod
    def delete(uuid):
        try:
            rowcount = RegistraServices.delete(uuid)
            if rowcount == 0:
                return jsonify({"mensaje": "No se encontro el registro", "status": "error"}), 404
            return jsonify({"mensaje": "Se elimino correctamente", "status": "ok"}), 200
        except Exception as e:
            return jsonify({"mensaje": "Error al eliminar", "error": str(e), "status": "error"}), 500
