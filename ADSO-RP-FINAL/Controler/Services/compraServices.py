from flask import current_app
from Models.compra import Compra
import uuid

class CompraServices:
    @staticmethod
    def read():
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT * FROM t_compra")
        rows = c.fetchall()
        return [Compra(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for row in rows]

    @staticmethod
    def add(cInfo):
        uuid_str = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO t_compra (com_uuid, com_numero_compra, com_monto_total, com_fecha_compra, com_pag_id, com_cli_id) VALUES (%s, %s, %s, %s, %s, %s)"
        c.execute(query, (uuid_str, cInfo["numero_compra"], cInfo["monto_total"], cInfo["fecha_compra"], cInfo["pag_id"], cInfo["cli_id"]))
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        return {
            "id": new_id,
            "uuid": uuid_str,
            "numero_compra": cInfo["numero_compra"],
            "monto_total": cInfo["monto_total"],
            "fecha_compra": cInfo["fecha_compra"],
            "pag_id": cInfo["pag_id"],
            "cli_id": cInfo["cli_id"]
        }

    @staticmethod
    def update(rid, cInfo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE t_compra SET com_numero_compra = %s, com_monto_total = %s, com_fecha_compra = %s, com_pag_id = %s, com_cli_id = %s WHERE com_id = %s"
        c.execute(query, (cInfo["numero_compra"], cInfo["monto_total"], cInfo["fecha_compra"], cInfo["pag_id"], cInfo["cli_id"], rid))
        current_app.mysql.connection.commit()
        if c.rowcount == 0:
            return None
        return {"id": rid, **cInfo}

    @staticmethod
    def delete(rid):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM t_compra WHERE com_id = %s", (rid,))
        current_app.mysql.connection.commit()
        return c.rowcount
