from flask import current_app
from Models.compra import Compra
import uuid

class CompraServices:
   

    @staticmethod
    def add(cInfo):
        try:
            uuid_str = str(uuid.uuid4())
            c = current_app.mysql.connection.cursor()
            query = "INSERT INTO t_compra (com_uuid, com_numero_compra, com_monto_total, com_fecha_compra, com_pag_id, com_cli_id) VALUES (%s, %s, %s, %s, %s, %s)"
            c.execute(query, (uuid_str, cInfo["numero_compra"], cInfo["monto_total"], cInfo["fecha_compra"], cInfo["pag_id"], cInfo["cli_id"]))
            current_app.mysql.connection.commit()
            new_id = c.lastrowid
            return {"id": new_id, "uuid": uuid_str, "numero_compra": cInfo["numero_compra"],
            "monto_total": cInfo["monto_total"],
            "fecha_compra": cInfo["fecha_compra"],
            "pag_id": cInfo["pag_id"],
            "cli_id": cInfo["cli_id"]}
        except Exception as e:
            current_app.mysql.connection.rollback() if hasattr(current_app.mysql, "connection") else None
            raise RuntimeError(f"Error en INSERT t_compra: {str(e)}")

    @staticmethod
    def delete(uuid):
    
            c = current_app.mysql.connection.cursor()
            query ="DELETE FROM t_com WHERE com_uuid = %s"
            c.execute(query, (uuid,))
            current_app.mysql.connection.commit()
            if c.rowcount ==0:
                c.close()
                return 404

                c.close()
                return 200
        
def read():
        try:
            c = current_app.mysql.connection.cursor()
            query =SELECT * FROM t_compra
           c.execute(query)
           data =c.fetchall()
           print(data)
           c.close()
           
            x =  [Compra(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for w in data]
        return x
 
 def update(rid, cInfo):
         try:
             c = current_app.mysql.connection.cursor()
             query = """ 
             
              UPDATE t_compra SET com_numero_compra = %s, com_monto_total = %s, com_fecha_compra = %s, com_pag_id = %s, com_cli_id = %s WHERE com_id = %s"
 
             """
             c.execute(query, (cInfo["numero_compra"], cInfo["monto_total"], cInfo["fecha_compra"], cInfo["pag_id"], cInfo["cli_id"], rid))
 
             current_app.mysql.connection.commit()
             if c.rowcount == 0:
                 c.close()
                 return 404
 
                 c.close()
                 
             return 200
             c.close()
             data 
 
                 
             return {"id": rid, **cInfo}
         except Exception as e:
             raise RuntimeError(f"Error en UPDATE t_compra: {str(e)}")
 