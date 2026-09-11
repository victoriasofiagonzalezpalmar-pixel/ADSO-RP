from flask import current_app, jsonify
from Models.clasifica import clasifica
import uuid

class clasificaServer:

    def add(cInfo):
        uuid_cla = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO clasifica 
        (cla_uuid, cla_pro_id, cla_cat_id)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_cla,
                 cInfo["Pro_Id"], cInfo["Cat_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_cla, 
            "Pro_Id": cInfo["Pro_Id"], 
            "Cat_Id": cInfo["Cat_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Pro_Id", "Cat_Id"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
        

     def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_clasifica WHERE cla_uuid = %s"
        c .execute(query , (uuid ,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200
        
    

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM clasifica"
        c.execute(query)
        data = c.fetchall()
        cla = [clasifica(row[0], row[1], row[2], row[3]).to_dict() for row in data]
        print(data)
        