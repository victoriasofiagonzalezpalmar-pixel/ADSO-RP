from flask import current_app
from Models.cliente import Cliente
import uuid

class ClienteServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_cliente")
            rows = c.fetchall()
            return [Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_cliente: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_cliente (cli_uuid, cli_identificacion, cli_primer_nombre, cli_segundo_nombre, cli_primer_apellido, cli_segundo_apellido) VALUES (%s, %s, %s, %s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["identificacion"], cInfo["primer_nombre"], cInfo["segundo_nombre"], cInfo["primer_apellido"], cInfo["segundo_apellido"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "identificacion": cInfo["identificacion"],
            "primer_nombre": cInfo["primer_nombre"],
            "segundo_nombre": cInfo["segundo_nombre"],
            "primer_apellido": cInfo["primer_apellido"],
            "segundo_apellido": cInfo["segundo_apellido"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_cliente: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_cliente SET cli_identificacion = %s, cli_primer_nombre = %s, cli_segundo_nombre = %s, cli_primer_apellido = %s, cli_segundo_apellido = %s WHERE cli_id = %s"
            c.execute(query, (cInfo["identificacion"], cInfo["primer_nombre"], cInfo["segundo_nombre"], cInfo["primer_apellido"], cInfo["segundo_apellido"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_cliente: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_cliente WHERE cli_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_cliente (por uuid): {str(e)}")
