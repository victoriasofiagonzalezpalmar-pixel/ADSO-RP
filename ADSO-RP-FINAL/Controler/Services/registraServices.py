from flask import current_app
from Models.registra import Registra
import uuid

class RegistraServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_registra")
        rows = c.fetchall()
        return [Registra(row[0], row[1], row[2], row[3]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_registra (rej_uuid, rej_usu_id, rej_com_id) VALUES (%s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["usu_id"], cInfo["com_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "usu_id": cInfo["usu_id"],
            "com_id": cInfo["com_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_registra SET rej_usu_id = %s, rej_com_id = %s WHERE rej_id = %s"
        c.execute(query, (cInfo["usu_id"], cInfo["com_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_registra WHERE rej_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
