# ADSO-RP - Proyecto Corregido

## Estructura
```
ADSO-RP/
├── .env                  # Variables de entorno (MySQL)
├── requirements.txt      # Dependencias
├── Models/               # Modelos de datos (15 entidades)
├── Routes/               # Blueprints de rutas + documentacion Swagger
└── Controler/
    ├── app.py            # Punto de entrada
    ├── Config.py         # Configuracion MySQL
    ├── Controllers/      # Controladores (15)
    └── Services/         # Servicios con consultas MySQL (15)
```

## Instalacion
```
pip install -r requirements.txt
```
Si `mysqlclient` falla en Windows:
```
pip install pymysql
```
Y agrega al inicio de `app.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

## Ejecutar
```
cd Controler
python app.py
```
Abrir: http://localhost:6600/documentacion/  (Swagger UI)

## Errores corregidos
- app.py: `app,Config.from_object` -> `app.config.from_object`; `loadRoutes` con nombre correcto
- Config.py: `MYSQL_CLIENTE` -> `MYSQL_PORT`
- .env: `MYSQL_CLIENTE=root` -> `MYSQL_USER=root`; se elimino bloque mysql_ssl invalido
- requirements.txt: `flask-mysql` -> `flask-mysqldb` + `mysqlclient`
- Controllers: nombres de clase y metodos estandarizados (read/add/update/delete)
- Services: clase renombrada (XServices), read() retorna datos, update()/delete() implementados, add() retorna dict (no jsonify)
- Routes: imports corregidos (Controllers.XController, clase singular), metodos llamados correctamente
- registraServices.py: conflicto de merge Git resuelto
- documentacion.py: titulo ADSO-RP, swagger.json embebido, registrado en rutas
- Agregados __init__.py en todos los paquetes
