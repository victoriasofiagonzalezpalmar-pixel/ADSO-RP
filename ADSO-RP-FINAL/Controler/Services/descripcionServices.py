from flask import current_app
from Models.descripcion import Descripcion
import uuid

class DescripcionServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_descripcion")
        rows = c.fetchall()
        return [Descripcion(row[0], row[1], row[2], row[3], row[4]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_descripcion (des_uuid, des_talla, des_color, des_pro_id) VALUES (%s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["talla"], cInfo["color"], cInfo["pro_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "talla": cInfo["talla"],
            "color": cInfo["color"],
            "pro_id": cInfo["pro_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_descripcion SET des_talla = %s, des_color = %s, des_pro_id = %s WHERE des_id = %s"
        c.execute(query, (cInfo["talla"], cInfo["color"], cInfo["pro_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_descripcion WHERE des_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
