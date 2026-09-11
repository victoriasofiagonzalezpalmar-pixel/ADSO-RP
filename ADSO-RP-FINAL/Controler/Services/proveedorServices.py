from flask import current_app
from Models.proveedor import Proveedor
import uuid

class ProveedorServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_proveedor")
        rows = c.fetchall()
        return [Proveedor(row[0], row[1], row[2], row[3]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_proveedor (edor_uuid, edor_nit, edor_nombre) VALUES (%s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["nit"], cInfo["nombre"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "nit": cInfo["nit"],
            "nombre": cInfo["nombre"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_proveedor SET edor_nit = %s, edor_nombre = %s WHERE edor_id = %s"
        c.execute(query, (cInfo["nit"], cInfo["nombre"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_proveedor WHERE edor_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
