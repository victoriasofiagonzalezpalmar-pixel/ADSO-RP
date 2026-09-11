from flask import jsonify, request
from Services.registraServices import RegistraServices


class RegistraController:

    
    def read():
        data = RegistraServices.read()
        return jsonify({"mensaje": data}), 200

    
    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        # Campos requeridos para registrar la relacion usuario-compra
        requeridos = ["usu_id", "com_id"]
        falta = [x for x in requeridos if x not in data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = RegistraServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": x}), 200

    
    def update(id):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        requeridos = ["usu_id", "com_id"]
        falta = [x for x in requeridos if x not in body_data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = RegistraServices.update(id, body_data)
        return jsonify({"mensaje": "Se actualizo correctamente", "data": x}), 200

    
    def delete(uuid):
                x = RegistraServices.delete(uuid)
                if x ==404:
                    return jsonify({"mensaje":"no se encontro el registro"}), x
                else:
                    return jsonify({"mensaje": "Se elimino correctamente"}), x