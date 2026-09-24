from flask import current_app
from Models.usuario import Usuario
import uuid

class UsuarioServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_usario")
            rows = c.fetchall()
            return [Usuario(row[0], row[1], row[2], row[3], row[4], row[5]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_usario: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_usario (usu_uuid, usu_cedula, usu_nombre, usu_apellido, usu_contrasena) VALUES (%s, %s, %s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["cedula"], cInfo["nombre"], cInfo["apellido"], cInfo["contrasena"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "cedula": cInfo["cedula"],
            "nombre": cInfo["nombre"],
            "apellido": cInfo["apellido"],
            "contrasena": cInfo["contrasena"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_usario: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_usario SET usu_cedula = %s, usu_nombre = %s, usu_apellido = %s, usu_contrasena = %s WHERE usu_id = %s"
            c.execute(query, (cInfo["cedula"], cInfo["nombre"], cInfo["apellido"], cInfo["contrasena"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_usario: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_usario WHERE usu_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_usario (por uuid): {str(e)}")
