from flask import current_app, jsonify
from Models.categoria import categoria
import uuid

class categoriaServer:

    def add(cInfo):
        uuid_cat = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSERT INTO t_categoria 
        (cat_uuid, cat_nombre, cat_tipo)
        VALUES (%s, %s, %s)"""
        c.execute(query, (uuid_cat,
                 cInfo["Nombre"], cInfo["Tipo"]))
        current_app.mysql.connection.commit()

        id = c.lastrowid
        data = {
            "id": id, 
            "uuid": uuid_cat, 
            "Nombre": cInfo["Nombre"], 
            "Tipo": cInfo["Tipo"]
        }
        
        if not data:
            return jsonify({"Mensaje": "El cuerpo esta vacio o es invalido"})

        requeridos = ["Nombre", "Tipo"]
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
        query = "SELECT * FROM t_categoria"
        c.execute(query)
        data = c.fetchall()
        cat = [categoria(row[0], row[1], row[2], row[3]).to_dict() for row in data]
        print(data)
        