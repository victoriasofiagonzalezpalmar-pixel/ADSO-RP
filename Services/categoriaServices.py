from flask import current_app
from Models.categoria import Categoria
import uuid

class CategoriaServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_categoria")
            rows = c.fetchall()
            return [Categoria(row[0], row[1], row[2], row[3]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_categoria: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_categoria (cat_uuid, cat_nombre, cat_tipo) VALUES (%s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["nombre"], cInfo["tipo"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "nombre": cInfo["nombre"],
            "tipo": cInfo["tipo"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_categoria: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_categoria SET cat_nombre = %s, cat_tipo = %s WHERE cat_id = %s"
            c.execute(query, (cInfo["nombre"], cInfo["tipo"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_categoria: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_categoria WHERE cat_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_categoria (por uuid): {str(e)}")
