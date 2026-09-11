from flask import current_app, jsonify
from Models.compra import compra
import uuid

class compraServer:

    def add(cInfo):
        uuid_com = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_compra 
        (com_uuid, com_numero_compra, com_monto_total, com_fecha_compra, com_pag_id, com_cli_id)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_com,
                 cInfo["Numero_Compra"], cInfo["Monto_Total"], cInfo["Fecha_Compra"], cInfo["Pag_Id"], cInfo["Cli_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_com, 
            "Numero_Compra": cInfo["Numero_Compra"], 
            "Monto_Total": cInfo["Monto_Total"], 
            "Fecha_Compra": cInfo["Fecha_Compra"], 
            "Pag_Id": cInfo["Pag_Id"], 
            "Cli_Id": cInfo["Cli_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Numero_Compra", "Monto_Total", "Fecha_Compra", "Pag_Id", "Cli_Id"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
        

     def delete(uuid):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM t_compra WHERE com_uuid = %s"
        c .execute(query ,(uuid,))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            c.close()
            return 404
        c.close()
        return 200
    
    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_compra"
        c.execute(query)
        data = c.fetchall()
        com = [compra(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for row in data]
        print(data)
        