from flask import current_app
from Models.datoproveedor import DatoProveedor
import uuid

class DatoProveedorServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_datoproveedor")
        rows = c.fetchall()
        return [DatoProveedor(row[0], row[1], row[2], row[3], row[4]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_datoproveedor (ato_uuid, ato_telefono, ato_correo, ato_pro_id) VALUES (%s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["telefono"], cInfo["correo"], cInfo["pro_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "telefono": cInfo["telefono"],
            "correo": cInfo["correo"],
            "pro_id": cInfo["pro_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_datoproveedor SET ato_telefono = %s, ato_correo = %s, ato_pro_id = %s WHERE ato_id = %s"
        c.execute(query, (cInfo["telefono"], cInfo["correo"], cInfo["pro_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_datoproveedor WHERE ato_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
