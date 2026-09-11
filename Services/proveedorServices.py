from flask import current_app, jsonify
from Models.Proveedor import Proveedor
import uuid

class proveedorServer:

    def add(cInfo):
        uuid_edor = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_proveedor 
        (edor_uuid, edor_nit, edor_nombre)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_edor,
                 cInfo["Nit"], cInfo["Nombre"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_edor, 
            "Nit": cInfo["Nit"], 
            "Nombre": cInfo["Nombre"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Nit", "Nombre"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
        

     def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query =  "DELETE FROM t_proveedor WHERE edor_uuid = %s "
        c .execute(query ,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200

def read():
    c = current_app.mysql.connection.cursor()
    query = "SELECT * FROM t_proveedor"
    c.execute(query)
    data = c.fetchall()
    prov = [Proveedor(row[0], row[1], row[2], row[3]).to_dict() for row in data]
    print (data)
        