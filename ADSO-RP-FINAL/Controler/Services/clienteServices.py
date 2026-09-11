from flask import current_app
from Models.cliente import Cliente
import uuid

class ClienteServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_cliente")
        rows = c.fetchall()
        return [Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_cliente (cli_uuid, cli_identificacion, cli_primer_nombre, cli_segundo_nombre, cli_primer_apellido, cli_segundo_apellido) VALUES (%s, %s, %s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["identificacion"], cInfo["primer_nombre"], cInfo["segundo_nombre"], cInfo["primer_apellido"], cInfo["segundo_apellido"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "identificacion": cInfo["identificacion"],
            "primer_nombre": cInfo["primer_nombre"],
            "segundo_nombre": cInfo["segundo_nombre"],
            "primer_apellido": cInfo["primer_apellido"],
            "segundo_apellido": cInfo["segundo_apellido"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_cliente SET cli_identificacion = %s, cli_primer_nombre = %s, cli_segundo_nombre = %s, cli_primer_apellido = %s, cli_segundo_apellido = %s WHERE cli_id = %s"
        c.execute(query, (cInfo["identificacion"], cInfo["primer_nombre"], cInfo["segundo_nombre"], cInfo["primer_apellido"], cInfo["segundo_apellido"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_cliente WHERE cli_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
