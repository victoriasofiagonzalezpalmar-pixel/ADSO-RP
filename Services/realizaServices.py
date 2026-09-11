from flask import current_app, jsonify
from Models.realiza import realiza
import uuid

class realizaServer:

    def add(cInfo):
        uuid_rea = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_realiza 
        (rea_uuid, rea_cli_id, rea_dev_id)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_rea,
                 cInfo["Cli_Id"], cInfo["Dev_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_rea, 
            "Cli_Id": cInfo["Cli_Id"], 
            "Dev_Id": cInfo["Dev_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Cli_Id", "Dev_Id"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
        

     def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_realiza WHERE rea_uuid = %s"
        c .execute(query ,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 400
        c.close()
        return 200
    
    
    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_realiza"
        c.execute(query)
        data = c.fetchall()
        rea = [realiza(row[0], row[1], row[2], row[3]).to_dict() for row in data]
        print(data)
        