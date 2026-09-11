from flask import current_app
from Models.devolucion import Devolucion
import uuid

class DevolucionServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_devolucion")
        rows = c.fetchall()
        return [Devolucion(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_devolucion (dev_uuid, dev_estado_producto, dev_motivos, dev_tipo_producto, dev_fecha_devolucion) VALUES (%s, %s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["estado_producto"], cInfo["motivos"], cInfo["tipo_producto"], cInfo["fecha_devolucion"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "estado_producto": cInfo["estado_producto"],
            "motivos": cInfo["motivos"],
            "tipo_producto": cInfo["tipo_producto"],
            "fecha_devolucion": cInfo["fecha_devolucion"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_devolucion SET dev_estado_producto = %s, dev_motivos = %s, dev_tipo_producto = %s, dev_fecha_devolucion = %s WHERE dev_id = %s"
        c.execute(query, (cInfo["estado_producto"], cInfo["motivos"], cInfo["tipo_producto"], cInfo["fecha_devolucion"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_devolucion WHERE dev_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
