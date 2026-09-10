from flask import current_app, jsonify
from Models.cliente import cliente
import uuid
 

class clienteServer:

    def add(cInfo):
        uuid_cli = uuid.uuid4()
        c = current_app.mysql.connection.cursor()
        query = """INSER INTO t_cliente 
        (cli_uuid, cli_identificacion, cli_primer_nombre, cli_segundo_nombre,
          cli_primer_apellido, cli_segundo_apellido)
        value
        (%s, %s, %s, %s, %s, %s,)"""
        c.execute(query,(uuid_cli,
                  cInfo["Identificacion"], cInfo["Pri_Nombre"], cInfo["seg_Nombre"],
                  cInfo["pri_Apellido"], cInfo["seg_Apellido"]))
        current_app.mysql.connectacion.commit()

        id = c.lastrowid
        data ={"id" :id, "uuid" :uuid_cli, 
              "Identificacion":cInfo["Identificacion"], "Pri_Nombre":cInfo["Pri_Nombre"],
              "seg_Nombre":cInfo["seg_Nombre"], "pri_Apellido":cInfo["pri_Apellido"],
              "seg_Apellido":cInfo["seg_Apellido"]}
        if not data:
            return jsonify({"Mensaje":" El cuerpo esta vacio o es invalido"})

        requeridos = ["Identificacion","Pri_Nombre","seg_Nombre","pri_Apellido", "seg_Apellido"]

        falt = [ x for x in requeridos if x not in data ]

        if len(falt) > 0:
            return jsonify ({"Mensaje":f"Falta parametro{falt}"}, 400)
        

    def update():
        pass

    def delete():
        pass

    def read():
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM t_cliente"
        c.execute(query)
        data = c.fatchalla()
        cli = [cliente(cli[0], cli[1], cli[2], cli[3],
                        cli[4], cli[5], cli[6]).to_dict for cliente in data]
        print(data)