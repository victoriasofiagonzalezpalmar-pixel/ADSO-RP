from flask import current_app
from Models.datoproveedor import DatoProveedor
import uuid

class DatoProveedorServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_datoproveedor")
            rows = c.fetchall()
            return [DatoProveedor(row[0], row[1], row[2], row[3], row[4]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_datoproveedor: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_datoproveedor (ato_uuid, ato_telefono, ato_correo, ato_pro_id) VALUES (%s, %s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["telefono"], cInfo["correo"], cInfo["pro_id"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "telefono": cInfo["telefono"],
            "correo": cInfo["correo"],
            "pro_id": cInfo["pro_id"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_datoproveedor: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_datoproveedor SET ato_telefono = %s, ato_correo = %s, ato_pro_id = %s WHERE ato_id = %s"
            c.execute(query, (cInfo["telefono"], cInfo["correo"], cInfo["pro_id"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_datoproveedor: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_datoproveedor WHERE ato_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_datoproveedor (por uuid): {str(e)}")
