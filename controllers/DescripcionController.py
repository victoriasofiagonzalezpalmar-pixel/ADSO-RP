from flask import jsonify, request
from Services.descripcionServices import DescripcionServices


class DescripcionController:

    
    def read():
        data = DescripcionServices.read()
        return jsonify({"mensaje": data}), 200

    
    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        # Campos requeridos para registrar descripcion de producto
        requeridos = ["talla", "color", "pro_id"]
        falta = [x for x in requeridos if x not in data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = DescripcionServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": x}), 200

    
    def update(id):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        requeridos = ["talla", "color", "pro_id"]
        falta = [x for x in requeridos if x not in body_data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = DescripcionServices.update(id, body_data)
        return jsonify({"mensaje": "Se actualizo correctamente", "data": x}), 200

    
    def delete(uuid):
                x = DescripcionServices.delete(uuid)
                if x ==404:
                    return jsonify({"mensaje":"no se encontro el registro"}), x
                else:
                    return jsonify({"mensaje": "Se elimino correctamente"}), x