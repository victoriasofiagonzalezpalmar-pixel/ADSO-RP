from flask import current_app
from Models.datocliente import DatoCliente
import uuid

class DatoClienteServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_datocliente")
            rows = c.fetchall()
            return [DatoCliente(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_datocliente: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_datocliente (dat_uuid, dat_correo, dat_telefono, dat_direccion, dat_cli_id) VALUES (%s, %s, %s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["correo"], cInfo["telefono"], cInfo["direccion"], cInfo["cli_id"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "correo": cInfo["correo"],
            "telefono": cInfo["telefono"],
            "direccion": cInfo["direccion"],
            "cli_id": cInfo["cli_id"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_datocliente: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_datocliente SET dat_correo = %s, dat_telefono = %s, dat_direccion = %s, dat_cli_id = %s WHERE dat_id = %s"
            c.execute(query, (cInfo["correo"], cInfo["telefono"], cInfo["direccion"], cInfo["cli_id"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_datocliente: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_datocliente WHERE dat_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_datocliente (por uuid): {str(e)}")
