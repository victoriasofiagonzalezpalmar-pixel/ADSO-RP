from flask import current_app, jsonify
from Models.rejistra import rejistra
import uuid

class rejistraServer:

    def add(cInfo):
        uuid_rej = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_rejistra 
        (rej_uuid, rej_usu_id, rej_com_id)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_rej,
                 cInfo["Usu_Id"], cInfo["Com_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_rej, 
            "Usu_Id": cInfo["Usu_Id"], 
            "Com_Id": cInfo["Com_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Usu_Id", "Com_Id"]
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
        query = "SELECT * FROM t_rejistra"
        c.execute(query)
        data = c.fetchall()
        rej = [rejistra(row[0], row[1], row[2], row[3]).to_dict() for row in data]
        print(data)
        