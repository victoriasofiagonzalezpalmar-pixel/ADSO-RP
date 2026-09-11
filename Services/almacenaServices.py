from flask import current_app, jsonify
from Models.almacena import almacena
import uuid

class almacenaServer:

    def add(cInfo):
        uuid_alm = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO almacena 
        (alm_uuid, alm_cantidad, alm_com_id, alm_pro_id)
        VALUES (%s, %s, %s, %s)"""
        c.execute(query, (uuid_alm,
                 cInfo["Cantidad"], cInfo["Com_Id"], cInfo["Pro_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_alm, 
            "Cantidad": cInfo["Cantidad"], 
            "Com_Id": cInfo["Com_Id"], 
            "Pro_Id": cInfo["Pro_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Cantidad", "Com_Id", "Pro_Id"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
    

     def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_almacena WHERE alm_uuid = %s"
        c .execute(query ,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200
    
    
    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM almacena"
        c.execute(query)
        data = c.fetchall()
        alm = [almacena(row[0], row[1], row[2], row[3], row[4]).to_dict() for row in data]
        print(data)
        