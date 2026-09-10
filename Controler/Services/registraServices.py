from flask import current_app, jsonify
<<<<<<< HEAD
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
=======
<<<<<<<< HEAD:Controler/Services/rejistraServices.py
from Models.registra import registra
========
from Models.registra import rejistra
>>>>>>>> fc75b6e7c29ef8040b21aff71ad756d7a511aefa:Controler/Services/registraServices.py
import uuid

class registraServer:

    def add(cInfo):
        uuid_reg = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_registra 
        (reg_uuid, reg_usu_id, reg_com_id)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_reg,
>>>>>>> fc75b6e7c29ef8040b21aff71ad756d7a511aefa
                 cInfo["Usu_Id"], cInfo["Com_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
<<<<<<< HEAD
            "uuid": uuid_rej, 
=======
            "uuid": uuid_reg, 
>>>>>>> fc75b6e7c29ef8040b21aff71ad756d7a511aefa
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
<<<<<<< HEAD
        query = "SELECT * FROM t_rejistra"
        c.execute(query)
        data = c.fetchall()
        rej = [rejistra(row[0], row[1], row[2], row[3]).to_dict() for row in data]
=======
        query = "SELECT * FROM t_registra"
        c.execute(query)
        data = c.fetchall()
        reg = [registra(row[0], row[1], row[2], row[3]).to_dict() for row in data]
>>>>>>> fc75b6e7c29ef8040b21aff71ad756d7a511aefa
        print(data)
        