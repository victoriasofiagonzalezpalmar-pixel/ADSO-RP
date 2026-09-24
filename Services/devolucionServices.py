from flask import current_app
from Models.devolucion import Devolucion
import uuid

class DevolucionServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_devolucion")
            rows = c.fetchall()
            return [Devolucion(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_devolucion: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_devolucion (dev_uuid, dev_estado_producto, dev_motivos, dev_tipo_producto, dev_fecha_devolucion) VALUES (%s, %s, %s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["estado_producto"], cInfo["motivos"], cInfo["tipo_producto"], cInfo["fecha_devolucion"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "estado_producto": cInfo["estado_producto"],
            "motivos": cInfo["motivos"],
            "tipo_producto": cInfo["tipo_producto"],
            "fecha_devolucion": cInfo["fecha_devolucion"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_devolucion: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_devolucion SET dev_estado_producto = %s, dev_motivos = %s, dev_tipo_producto = %s, dev_fecha_devolucion = %s WHERE dev_id = %s"
            c.execute(query, (cInfo["estado_producto"], cInfo["motivos"], cInfo["tipo_producto"], cInfo["fecha_devolucion"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_devolucion: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_devolucion WHERE dev_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_devolucion (por uuid): {str(e)}")
