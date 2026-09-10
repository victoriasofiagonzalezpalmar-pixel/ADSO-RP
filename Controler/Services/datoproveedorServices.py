from flask import current_app, jsonify
from Models.Datoproveedor import Datoproveedor
import uuid

class datoproveedorServer:

    def add(cInfo):
        uuid_ato = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_datoproveedor 
        (ato_uuid, ato_telefono, ato_correo, ato_pro_id)
        VALUES (%s, %s, %s, %s)"""
        c.execute(query, (uuid_ato,
                 cInfo["Telefono"], cInfo["Correo"], cInfo["Pro_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_ato, 
            "Telefono": cInfo["Telefono"], 
            "Correo": cInfo["Correo"], 
            "Pro_Id": cInfo["Pro_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Telefono", "Correo", "Pro_Id"]
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
        query = "SELECT * FROM t_datoproveedor"
        c.execute(query)
        data = c.fetchall()
        ato = [Datoproveedor(row[0], row[1], row[2], row[3], row[4]).to_dict() for row in data]
        print(data)
        