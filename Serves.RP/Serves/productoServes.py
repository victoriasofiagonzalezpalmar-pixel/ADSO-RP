from flask import current_app, jsonify
from Models.producto import producto
import uuid

class productoServer:

    def add(cInfo):
        uuid_pro = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_producto 
        (pro_uuid, pro_cofigo, pro_nombre, pro_pricio, pro_stock, pro_edor_id)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_pro,
                 cInfo["Codigo"], cInfo["Nombre"], cInfo["Pricio"], cInfo["Stock"], cInfo["Edor_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_pro, 
            "Codigo": cInfo["Codigo"], 
            "Nombre": cInfo["Nombre"], 
            "Pricio": cInfo["Pricio"], 
            "Stock": cInfo["Stock"], 
            "Edor_Id": cInfo["Edor_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Codigo", "Nombre", "Pricio", "Stock", "Edor_Id"]
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
        query = "SELECT * FROM t_producto"
        c.execute(query)
        data = c.fetchall()
        pro = [producto(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for row in data]
        print(data)
    