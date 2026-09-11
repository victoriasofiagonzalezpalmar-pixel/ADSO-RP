from flask import current_app
from Models.datocliente import DatoCliente
import uuid

class DatoClienteServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_datocliente")
        rows = c.fetchall()
        return [DatoCliente(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_datocliente (dat_uuid, dat_correo, dat_telefono, dat_direccion, dat_cli_id) VALUES (%s, %s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["correo"], cInfo["telefono"], cInfo["direccion"], cInfo["cli_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "correo": cInfo["correo"],
            "telefono": cInfo["telefono"],
            "direccion": cInfo["direccion"],
            "cli_id": cInfo["cli_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_datocliente SET dat_correo = %s, dat_telefono = %s, dat_direccion = %s, dat_cli_id = %s WHERE dat_id = %s"
        c.execute(query, (cInfo["correo"], cInfo["telefono"], cInfo["direccion"], cInfo["cli_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_datocliente WHERE dat_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
