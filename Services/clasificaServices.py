from flask import current_app
from Models.clasifica import Clasifica
import uuid

class ClasificaServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM clasifica")
            rows = c.fetchall()
            return [Clasifica(row[0], row[1], row[2], row[3]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ clasifica: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO clasifica (cla_uuid, cla_pro_id, cla_cat_id) VALUES (%s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["pro_id"], cInfo["cat_id"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "pro_id": cInfo["pro_id"],
            "cat_id": cInfo["cat_id"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT clasifica: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE clasifica SET cla_pro_id = %s, cla_cat_id = %s WHERE cla_id = %s"
            c.execute(query, (cInfo["pro_id"], cInfo["cat_id"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE clasifica: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM clasifica WHERE cla_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE clasifica (por uuid): {str(e)}")
