from flask import jsonify, request
from Services.compraServices import CompraServices


class CompraController:

    
    def read():
        data = CompraServices.read()
        return jsonify({"mensaje": data}), 200

    
    def add():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        # Campos requeridos para registrar una compra
        requeridos = ["numero_compra", "monto_total", "fecha_compra", "pag_id", "cli_id"]
        falta = [x for x in requeridos if x not in data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = CompraServices.add(data)
        return jsonify({"mensaje": "Se registro correctamente", "data": x}), 200

    
    def update(id):
        body_data = request.get_json(silent=True)
        if not body_data:
            return jsonify({"mensaje": "El cuerpo esta vacio o invalido"}), 400

        requeridos = ["numero_compra", "monto_total", "fecha_compra", "pag_id", "cli_id"]
        falta = [x for x in requeridos if x not in body_data]

        if falta:
            return jsonify({"mensaje": f"Faltan parametros: {falta}"}), 400

        x = CompraServices.update(id, body_data)
        return jsonify({"mensaje": "Se actualizo correctamente", "data": x}), 200

    
    def delete(uuid):
            x = CompraServices.delete(uuid)
            if x ==404:
                return jsonify({"mensaje":"no se encontro el registro"}), x
            else:
                return jsonify({"mensaje": "Se elimino correctamente"}), x
    
