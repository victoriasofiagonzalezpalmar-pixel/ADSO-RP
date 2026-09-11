from flask import current_app, jsonify
from Models.usario import usario
import uuid

class usarioServer:

    def add(cInfo):
        uuid_usu = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_usario 
        (usu_uuid, usu_cedula, usu_nombre, usu_apellido, usu_contrasena)
        VALUES (%s, %s, %s, %s, %s)"""
        c.execute(query, (uuid_usu,
                 cInfo["Cedula"], cInfo["Nombre"], cInfo["Apellido"], cInfo["Contrasena"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_usu, 
            "Cedula": cInfo["Cedula"], 
            "Nombre": cInfo["Nombre"], 
            "Apellido": cInfo["Apellido"], 
            "Contrasena": cInfo["Contrasena"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Cedula", "Nombre", "Apellido", "Contrasena"]
        falt = [x for x in requeridos if x not in data]

        if len(falt) > 0:
            return jsonify({"Mensaje": f"Falta parametro {falt}"}, 400)
            
        return jsonify({"Mensaje": "Registrado exitosamente", "data": data}), 201

    def update():
     
 
     def delete(uuid):
      c = current_app.mysql.connection.cursor()
      query = "DELETE FROM t_usuario WHERE usu_uuid = %s"
      c .execute(query ,(uuid,))
      current_app.mysql.connection.commit()
      if c.rowcount == 0:
          c.close()
          return 400
      c.close()
      return 200
        
 
    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_usario"
        c.execute(query)
        data = c.fetchall()
        usu = [usario(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in data]
        print(data)
    