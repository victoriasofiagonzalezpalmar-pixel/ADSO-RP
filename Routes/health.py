from flask import Blueprint, jsonify, current_app

health_bp = Blueprint("health", __name__)

@health_bp.route("/")
def health():
    """Endpoint de diagnostico: verifica que la API y MySQL respondan."""
    estado = {"api": "ok", "mysql": "desconectado", "tablas": []}
    try:
        c = current_app.mysql.connection.cursor()
        c.execute("SHOW TABLES")
        tablas = [row[0] for row in c.fetchall()]
        estado["mysql"] = "conectado"
        estado["tablas"] = tablas
        estado["num_tablas"] = len(tablas)
        return jsonify(estado), 200
    except Exception as e:
        estado["error"] = str(e)
        estado["solucion"] = "Verifica que MySQL este corriendo y el .env tenga host/user/password/db correctos. La base de datos debe existir."
        return jsonify(estado), 500
