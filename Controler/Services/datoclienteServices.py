from flask import current_app, jsonify
from Models.datocliente import datocliente
import uuid

class datoclienteServer:

    def add(cInfo):
        uuid_dat = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_datocliente 
        (dat_uuid, dat_correo, dat_telefono, dat_direccion, dat_cli_id)
        VALUES (%s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_dat,
                 cInfo["Correo"], cInfo["Telefono"], cInfo["Direccion"], cInfo["Cli_Id"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_dat, 
            "Correo": cInfo["Correo"], 
            "Telefono": cInfo["Telefono"], 
            "Direccion": cInfo["Direccion"], 
            "Cli_Id": cInfo["Cli_Id"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Correo", "Telefono", "Direccion", "Cli_Id"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
        

     def delete(uuid):
      c = current_app.mysql.connection.cursor()
      query = "DELETE FROM t_datocliente WHERE dat_uuid = %s"
      c .execute(query , (uuid,))
      current_app.mysql.connection.commit()
      if c.rowcount == 0:
          c.close()
          return 404
      c.close()
      return 200
   

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_datocliente"
        c.execute(query)
        data = c.fetchall()
        dat = [datocliente(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in data]
        print(data)
        