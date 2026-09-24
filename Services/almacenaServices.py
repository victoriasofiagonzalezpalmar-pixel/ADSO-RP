from flask import current_app
from Models.almacena import Almacena
import uuid

class AlmacenaServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM almacena")
            rows = c.fetchall()
            return [Almacena(row[0], row[1], row[2], row[3], row[4]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ almacena: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO almacena (alm_uuid, alm_cantidad, alm_com_id, alm_pro_id) VALUES (%s, %s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["cantidad"], cInfo["com_id"], cInfo["pro_id"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "cantidad": cInfo["cantidad"],
            "com_id": cInfo["com_id"],
            "pro_id": cInfo["pro_id"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT almacena: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE almacena SET alm_cantidad = %s, alm_com_id = %s, alm_pro_id = %s WHERE alm_id = %s"
            c.execute(query, (cInfo["cantidad"], cInfo["com_id"], cInfo["pro_id"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE almacena: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM almacena WHERE alm_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE almacena (por uuid): {str(e)}")
