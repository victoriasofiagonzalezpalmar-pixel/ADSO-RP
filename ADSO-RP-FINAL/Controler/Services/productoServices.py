from flask import current_app
from Models.producto import Producto
import uuid

class ProductoServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_producto")
        rows = c.fetchall()
        return [Producto(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_producto (pro_uuid, pro_cofigo, pro_nombre, pro_pricio, pro_stock, pro_edor_id) VALUES (%s, %s, %s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["codigo"], cInfo["nombre"], cInfo["precio"], cInfo["stock"], cInfo["edor_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "codigo": cInfo["codigo"],
            "nombre": cInfo["nombre"],
            "precio": cInfo["precio"],
            "stock": cInfo["stock"],
            "edor_id": cInfo["edor_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_producto SET pro_cofigo = %s, pro_nombre = %s, pro_pricio = %s, pro_stock = %s, pro_edor_id = %s WHERE pro_id = %s"
        c.execute(query, (cInfo["codigo"], cInfo["nombre"], cInfo["precio"], cInfo["stock"], cInfo["edor_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_producto WHERE pro_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
