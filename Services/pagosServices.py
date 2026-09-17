from flask import current_app
from Models.pagos import Pagos
import uuid

class PagosServices:
    @staticmethod
    def read():
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("SELECT * FROM t_pagos")
            rows = c.fetchall()
            return [Pagos(row[0], row[1], row[2], row[3]).to_dict() for row in rows]
        except Exception as e:
            raise RuntimeError(f"Error en READ t_pagos: {str(e)}")

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_pagos (pag_uuid, pag_monto, pag_metodo_transaccion) VALUES (%s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["monto"], cInfo["metodo_transaccion"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "monto": cInfo["monto"],
            "metodo_transaccion": cInfo["metodo_transaccion"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_pagos: {str(e)}")

    @staticmethod
    def update(rid, cInfo):
        try:
            c = current_app.mysql.connection.cursor()
            query = "UPDATE t_pagos SET pag_monto = %s, pag_metodo_transaccion = %s WHERE pag_id = %s"
            c.execute(query, (cInfo["monto"], cInfo["metodo_transaccion"], rid))
            current_app.mysql.connection.commit()
            if c.rowcount == 0:
                return None
            return {"id": rid, **cInfo}
        except Exception as e:
            raise RuntimeError(f"Error en UPDATE t_pagos: {str(e)}")

    @staticmethod
    def delete(uuid):
        try:
            c = current_app.mysql.connection.cursor()
            c.execute("DELETE FROM t_pagos WHERE pag_uuid = %s", (uuid,))
            current_app.mysql.connection.commit()
            return c.rowcount
        except Exception as e:
            raise RuntimeError(f"Error en DELETE t_pagos (por uuid): {str(e)}")
