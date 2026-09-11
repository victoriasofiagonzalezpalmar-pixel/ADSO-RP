from flask import current_app
from Models.almacena import Almacena
import uuid

class AlmacenaServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM almacena")
        rows = c.fetchall()
        return [Almacena(row[0], row[1], row[2], row[3], row[4]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO almacena (alm_uuid, alm_cantidad, alm_com_id, alm_pro_id) VALUES (%s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["cantidad"], cInfo["com_id"], cInfo["pro_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "cantidad": cInfo["cantidad"],
            "com_id": cInfo["com_id"],
            "pro_id": cInfo["pro_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE almacena SET alm_cantidad = %s, alm_com_id = %s, alm_pro_id = %s WHERE alm_id = %s"
        c.execute(query, (cInfo["cantidad"], cInfo["com_id"], cInfo["pro_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM almacena WHERE alm_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
