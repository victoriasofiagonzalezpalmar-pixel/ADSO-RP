from flask import current_app, jsonify
from Models.pagos import pagos
import uuid

class pagosServer:

    def add(cInfo):
        uuid_pag = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_pagos 
        (pag_uuid, pag_monto, pag_metodo_transaccion)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_pag,
                 cInfo["monto"], cInfo["metodo_Transaccion"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_pag, 
            "monto": cInfo["monto"], 
            "metodo_Transaccion": cInfo["metodo_Transaccion"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["monto", "metodo_Transaccion"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
      
      

     def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_pagos WHERE pag_uuid = %s"
        c .execute(query ,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200
        
      
    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_pagos"
        c.execute(query)
        data = c.fetchall()
        pag = [pagos(row[0], row[1], row[2], row[3]).to_dict() for row in data]
        print(data)
        