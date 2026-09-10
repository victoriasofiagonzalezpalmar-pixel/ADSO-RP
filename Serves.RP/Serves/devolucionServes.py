from flask import current_app, jsonify
from Models.devolucion import devolucion
import uuid

class devolucionServer:

    def add(cInfo):
        uuid_dev = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_devolucion 
        (dev_uuid, dev_estado_producto, dev_motivos, dev_tipo_producto, dev_fecha_devolucion)
        VALUES (%s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_dev,
                 cInfo["Estado_Producto"], cInfo["Motivos"], cInfo["Tipo_Producto"], cInfo["Fecha_Devolucion"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_dev, 
            "Estado_Producto": cInfo["Estado_Producto"], 
            "Motivos": cInfo["Motivos"], 
            "Tipo_Producto": cInfo["Tipo_Producto"], 
            "Fecha_Devolucion": cInfo["Fecha_Devolucion"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Estado_Producto", "Motivos", "Tipo_Producto", "Fecha_Devolucion"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
        pass

    def delete():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_devolucion"
        c.execute(query)
        data = c.fetchall()
        dev = [devolucion(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in data]
        print(data)
        