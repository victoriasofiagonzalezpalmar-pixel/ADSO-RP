from flask import jsonify, request
from Services.usuarioServices import UsuarioServices


class UsuarioController:

    @staticmethod
    def read():
        data = UsuarioServices.read()
        return jsonify({"mensaje": data}), 200

    @staticmethod
    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        # Campos requeridos para registrar un usuario
        requeridos = ["cedula", "nombre", "apellido", "contrasena"]
        falta = [x for x in requeridos if x not in data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = UsuarioServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": x}), 200

    @staticmethod
    def update(id):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        requeridos = ["cedula", "nombre", "apellido", "contrasena"]
        falta = [x for x in requeridos if x not in body_data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = UsuarioServices.update(id, body_data)
        return jsonify({"mensaje": "Se actualizo correctamente", "data": x}), 200

    @staticmethod
    def delete(id):
        result = UsuarioServices.delete(id)
        return jsonify({"mensaje": "Se elimino correctamente", "data": result}), 200
