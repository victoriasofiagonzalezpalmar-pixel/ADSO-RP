from flask import current_app
from Models.realiza import Realiza
import uuid

class RealizaServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_realiza")
            rows = c.fetchall()
            return [Realiza(row[0], row[1], row[2], row[3]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_realiza: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_realiza (rea_uuid, rea_cli_id, rea_dev_id) VALUES (%s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["cli_id"], cInfo["dev_id"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "cli_id": cInfo["cli_id"],
            "dev_id": cInfo["dev_id"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_realiza: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_realiza SET rea_cli_id = %s, rea_dev_id = %s WHERE rea_id = %s"
            c.execute(query, (cInfo["cli_id"], cInfo["dev_id"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_realiza: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_realiza WHERE rea_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_realiza (por uuid): {str(e)}")
