from flask import current_app
from Models.clasifica import Clasifica
import uuid

class ClasificaServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM clasifica")
        rows = c.fetchall()
        return [Clasifica(row[0], row[1], row[2], row[3]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO clasifica (cla_uuid, cla_pro_id, cla_cat_id) VALUES (%s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["pro_id"], cInfo["cat_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "pro_id": cInfo["pro_id"],
            "cat_id": cInfo["cat_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE clasifica SET cla_pro_id = %s, cla_cat_id = %s WHERE cla_id = %s"
        c.execute(query, (cInfo["pro_id"], cInfo["cat_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM clasifica WHERE cla_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
