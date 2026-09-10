from flask import current_app, jsonify

from Models.registra import registra
import uuid

class registraServer:

    def add(cInfo):
        uuid_reg = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_registra 
        (reg_uuid, reg_usu_id, reg_com_id)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_reg,))


from Models.registra import registra

from Models.registra import registra

import uuid

class registraServer:

    def add(cInfo):
        uuid_reg = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_registra 
        (reg_uuid, reg_usu_id, reg_com_id)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_reg,

                 cInfo["Usu_Id"], cInfo["Com_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 

            "uuid": uuid_reg, 

            "uuid": uuid_reg, 

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

        query = "SELECT * FROM t_registra"
        c.execute(query)
        data = c.fetchall()
        regg = [registra(row[0], row[1], row[2], row[3]).to_dict() for row in data]

        query = "SELECT * FROM t_registra"
        c.execute(query)
        data = c.fetchall()
        reg = [registra(row[0], row[1], row[2], row[3]).to_dict() for row in data]

        print(data)
        