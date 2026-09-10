from flask import jsonify, request
from Services.AlmacenaServices import AlmacenaServices


class AlmacenaController:

    @staticmethod
    def read():
        data = AlmacenaServices.read()
        return jsonify({"mensaje": data}), 200

    @staticmethod
    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        # Campos requeridos para registrar la relacion compra-producto
        requeridos = ["com_id", "pro_id", "cantidad"]
        falta = [x for x in requeridos if x not in data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = AlmacenaServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": x}), 200

    @staticmethod
    def update(id):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        requeridos = ["com_id", "pro_id", "cantidad"]
        falta = [x for x in requeridos if x not in body_data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = AlmacenaServices.update(id, body_data)
        return jsonify({"mensaje": "Se actualizo correctamente", "data": x}), 200

    @staticmethod
    def delete(uuid):
        result = AlmacenaServices.delete(uuid)
        if result ==408:
            return jsonify({"mensaje":"no se encontro el registro"})
            return jsonify({"mensaje": "Se elimino correctamente", "data": result}), 200
