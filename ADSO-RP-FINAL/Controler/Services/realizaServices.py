from flask import current_app
from Models.realiza import Realiza
import uuid

class RealizaServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_realiza")
        rows = c.fetchall()
        return [Realiza(row[0], row[1], row[2], row[3]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_realiza (rea_uuid, rea_cli_id, rea_dev_id) VALUES (%s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["cli_id"], cInfo["dev_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "cli_id": cInfo["cli_id"],
            "dev_id": cInfo["dev_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_realiza SET rea_cli_id = %s, rea_dev_id = %s WHERE rea_id = %s"
        c.execute(query, (cInfo["cli_id"], cInfo["dev_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_realiza WHERE rea_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
