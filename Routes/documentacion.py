from flask import Blueprint, render_template_string, jsonify

documentacion_bp = Blueprint("documentacion", __name__)

SWAGGER_SPEC = {
  "openapi": "3.0.0",
  "info": {
    "title": "ADSO-RP",
    "version": "1.0.0",
    "description": "API ADSO-RP - Documentacion"
  },
  "paths": {
    "/usuario/": {
      "get": {
        "tags": [
          "Usuario"
        ],
        "summary": "Listar usuario",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Usuario"
        ],
        "summary": "Crear usuario",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/usuario/{id}": {
      "put": {
        "tags": [
          "Usuario"
        ],
        "summary": "Actualizar usuario"
      },
      "delete": {
        "tags": [
          "Usuario"
        ],
        "summary": "Eliminar usuario"
      }
    },
    "/almacena/": {
      "get": {
        "tags": [
          "Almacena"
        ],
        "summary": "Listar almacena",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Almacena"
        ],
        "summary": "Crear almacena",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/almacena/{id}": {
      "put": {
        "tags": [
          "Almacena"
        ],
        "summary": "Actualizar almacena"
      },
      "delete": {
        "tags": [
          "Almacena"
        ],
        "summary": "Eliminar almacena"
      }
    },
    "/categoria/": {
      "get": {
        "tags": [
          "Categoria"
        ],
        "summary": "Listar categoria",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Categoria"
        ],
        "summary": "Crear categoria",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/categoria/{id}": {
      "put": {
        "tags": [
          "Categoria"
        ],
        "summary": "Actualizar categoria"
      },
      "delete": {
        "tags": [
          "Categoria"
        ],
        "summary": "Eliminar categoria"
      }
    },
    "/clasifica/": {
      "get": {
        "tags": [
          "Clasifica"
        ],
        "summary": "Listar clasifica",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Clasifica"
        ],
        "summary": "Crear clasifica",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/clasifica/{id}": {
      "put": {
        "tags": [
          "Clasifica"
        ],
        "summary": "Actualizar clasifica"
      },
      "delete": {
        "tags": [
          "Clasifica"
        ],
        "summary": "Eliminar clasifica"
      }
    },
    "/cliente/": {
      "get": {
        "tags": [
          "Cliente"
        ],
        "summary": "Listar cliente",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Cliente"
        ],
        "summary": "Crear cliente",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/cliente/{id}": {
      "put": {
        "tags": [
          "Cliente"
        ],
        "summary": "Actualizar cliente"
      },
      "delete": {
        "tags": [
          "Cliente"
        ],
        "summary": "Eliminar cliente"
      }
    },
    "/compra/": {
      "get": {
        "tags": [
          "Compra"
        ],
        "summary": "Listar compra",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Compra"
        ],
        "summary": "Crear compra",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/compra/{id}": {
      "put": {
        "tags": [
          "Compra"
        ],
        "summary": "Actualizar compra"
      },
      "delete": {
        "tags": [
          "Compra"
        ],
        "summary": "Eliminar compra"
      }
    },
    "/datocliente/": {
      "get": {
        "tags": [
          "DatoCliente"
        ],
        "summary": "Listar datocliente",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "DatoCliente"
        ],
        "summary": "Crear datocliente",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/datocliente/{id}": {
      "put": {
        "tags": [
          "DatoCliente"
        ],
        "summary": "Actualizar datocliente"
      },
      "delete": {
        "tags": [
          "DatoCliente"
        ],
        "summary": "Eliminar datocliente"
      }
    },
    "/datoproveedor/": {
      "get": {
        "tags": [
          "DatoProveedor"
        ],
        "summary": "Listar datoproveedor",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "DatoProveedor"
        ],
        "summary": "Crear datoproveedor",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/datoproveedor/{id}": {
      "put": {
        "tags": [
          "DatoProveedor"
        ],
        "summary": "Actualizar datoproveedor"
      },
      "delete": {
        "tags": [
          "DatoProveedor"
        ],
        "summary": "Eliminar datoproveedor"
      }
    },
    "/descripcion/": {
      "get": {
        "tags": [
          "Descripcion"
        ],
        "summary": "Listar descripcion",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Descripcion"
        ],
        "summary": "Crear descripcion",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/descripcion/{id}": {
      "put": {
        "tags": [
          "Descripcion"
        ],
        "summary": "Actualizar descripcion"
      },
      "delete": {
        "tags": [
          "Descripcion"
        ],
        "summary": "Eliminar descripcion"
      }
    },
    "/devolucion/": {
      "get": {
        "tags": [
          "Devolucion"
        ],
        "summary": "Listar devolucion",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Devolucion"
        ],
        "summary": "Crear devolucion",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/devolucion/{id}": {
      "put": {
        "tags": [
          "Devolucion"
        ],
        "summary": "Actualizar devolucion"
      },
      "delete": {
        "tags": [
          "Devolucion"
        ],
        "summary": "Eliminar devolucion"
      }
    },
    "/pagos/": {
      "get": {
        "tags": [
          "Pagos"
        ],
        "summary": "Listar pagos",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Pagos"
        ],
        "summary": "Crear pagos",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/pagos/{id}": {
      "put": {
        "tags": [
          "Pagos"
        ],
        "summary": "Actualizar pagos"
      },
      "delete": {
        "tags": [
          "Pagos"
        ],
        "summary": "Eliminar pagos"
      }
    },
    "/producto/": {
      "get": {
        "tags": [
          "Producto"
        ],
        "summary": "Listar producto",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Producto"
        ],
        "summary": "Crear producto",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/producto/{id}": {
      "put": {
        "tags": [
          "Producto"
        ],
        "summary": "Actualizar producto"
      },
      "delete": {
        "tags": [
          "Producto"
        ],
        "summary": "Eliminar producto"
      }
    },
    "/proveedor/": {
      "get": {
        "tags": [
          "Proveedor"
        ],
        "summary": "Listar proveedor",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Proveedor"
        ],
        "summary": "Crear proveedor",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/proveedor/{id}": {
      "put": {
        "tags": [
          "Proveedor"
        ],
        "summary": "Actualizar proveedor"
      },
      "delete": {
        "tags": [
          "Proveedor"
        ],
        "summary": "Eliminar proveedor"
      }
    },
    "/realiza/": {
      "get": {
        "tags": [
          "Realiza"
        ],
        "summary": "Listar realiza",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Realiza"
        ],
        "summary": "Crear realiza",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/realiza/{id}": {
      "put": {
        "tags": [
          "Realiza"
        ],
        "summary": "Actualizar realiza"
      },
      "delete": {
        "tags": [
          "Realiza"
        ],
        "summary": "Eliminar realiza"
      }
    },
    "/registra/": {
      "get": {
        "tags": [
          "Registra"
        ],
        "summary": "Listar registra",
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      },
      "post": {
        "tags": [
          "Registra"
        ],
        "summary": "Crear registra",
        "responses": {
          "201": {
            "description": "Creado"
          }
        }
      }
    },
    "/registra/{id}": {
      "put": {
        "tags": [
          "Registra"
        ],
        "summary": "Actualizar registra"
      },
      "delete": {
        "tags": [
          "Registra"
        ],
        "summary": "Eliminar registra"
      }
    }
  },
  "components": {
    "schemas": {
      "Usuario": {
        "type": "object",
        "properties": {
          "usu_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "usu_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "usu_cedula": {
            "type": "string",
            "description": "cedula"
          },
          "usu_nombre": {
            "type": "string",
            "description": "nombre"
          },
          "usu_apellido": {
            "type": "string",
            "description": "apellido"
          },
          "usu_contrasena": {
            "type": "string",
            "description": "contrasena"
          }
        }
      },
      "Almacena": {
        "type": "object",
        "properties": {
          "alm_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "alm_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "alm_cantidad": {
            "type": "number",
            "description": "cantidad"
          },
          "alm_com_id": {
            "type": "integer",
            "description": "com_id"
          },
          "alm_pro_id": {
            "type": "integer",
            "description": "pro_id"
          }
        }
      },
      "Categoria": {
        "type": "object",
        "properties": {
          "cat_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "cat_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "cat_nombre": {
            "type": "string",
            "description": "nombre"
          },
          "cat_tipo": {
            "type": "string",
            "description": "tipo"
          }
        }
      },
      "Clasifica": {
        "type": "object",
        "properties": {
          "cla_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "cla_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "cla_pro_id": {
            "type": "integer",
            "description": "pro_id"
          },
          "cla_cat_id": {
            "type": "integer",
            "description": "cat_id"
          }
        }
      },
      "Cliente": {
        "type": "object",
        "properties": {
          "cli_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "cli_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "cli_identificacion": {
            "type": "string",
            "description": "identificacion"
          },
          "cli_primer_nombre": {
            "type": "string",
            "description": "primer_nombre"
          },
          "cli_segundo_nombre": {
            "type": "string",
            "description": "segundo_nombre"
          },
          "cli_primer_apellido": {
            "type": "string",
            "description": "primer_apellido"
          },
          "cli_segundo_apellido": {
            "type": "string",
            "description": "segundo_apellido"
          }
        }
      },
      "Compra": {
        "type": "object",
        "properties": {
          "com_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "com_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "com_numero_compra": {
            "type": "string",
            "description": "numero_compra"
          },
          "com_monto_total": {
            "type": "number",
            "description": "monto_total"
          },
          "com_fecha_compra": {
            "type": "string",
            "description": "fecha_compra"
          },
          "com_pag_id": {
            "type": "integer",
            "description": "pag_id"
          },
          "com_cli_id": {
            "type": "integer",
            "description": "cli_id"
          }
        }
      },
      "DatoCliente": {
        "type": "object",
        "properties": {
          "dat_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "dat_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "dat_correo": {
            "type": "string",
            "description": "correo"
          },
          "dat_telefono": {
            "type": "string",
            "description": "telefono"
          },
          "dat_direccion": {
            "type": "string",
            "description": "direccion"
          },
          "dat_cli_id": {
            "type": "integer",
            "description": "cli_id"
          }
        }
      },
      "DatoProveedor": {
        "type": "object",
        "properties": {
          "ato_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "ato_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "ato_telefono": {
            "type": "string",
            "description": "telefono"
          },
          "ato_correo": {
            "type": "string",
            "description": "correo"
          },
          "ato_pro_id": {
            "type": "integer",
            "description": "pro_id"
          }
        }
      },
      "Descripcion": {
        "type": "object",
        "properties": {
          "des_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "des_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "des_talla": {
            "type": "string",
            "description": "talla"
          },
          "des_color": {
            "type": "string",
            "description": "color"
          },
          "des_pro_id": {
            "type": "integer",
            "description": "pro_id"
          }
        }
      },
      "Devolucion": {
        "type": "object",
        "properties": {
          "dev_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "dev_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "dev_estado_producto": {
            "type": "string",
            "description": "estado_producto"
          },
          "dev_motivos": {
            "type": "string",
            "description": "motivos"
          },
          "dev_tipo_producto": {
            "type": "string",
            "description": "tipo_producto"
          },
          "dev_fecha_devolucion": {
            "type": "string",
            "description": "fecha_devolucion"
          }
        }
      },
      "Pagos": {
        "type": "object",
        "properties": {
          "pag_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "pag_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "pag_monto": {
            "type": "number",
            "description": "monto"
          },
          "pag_metodo_transaccion": {
            "type": "string",
            "description": "metodo_transaccion"
          }
        }
      },
      "Producto": {
        "type": "object",
        "properties": {
          "pro_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "pro_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "pro_cofigo": {
            "type": "string",
            "description": "codigo"
          },
          "pro_nombre": {
            "type": "string",
            "description": "nombre"
          },
          "pro_pricio": {
            "type": "number",
            "description": "precio"
          },
          "pro_stock": {
            "type": "number",
            "description": "stock"
          },
          "pro_edor_id": {
            "type": "integer",
            "description": "edor_id"
          }
        }
      },
      "Proveedor": {
        "type": "object",
        "properties": {
          "edor_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "edor_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "edor_nit": {
            "type": "string",
            "description": "nit"
          },
          "edor_nombre": {
            "type": "string",
            "description": "nombre"
          }
        }
      },
      "Realiza": {
        "type": "object",
        "properties": {
          "rea_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "rea_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "rea_cli_id": {
            "type": "integer",
            "description": "cli_id"
          },
          "rea_dev_id": {
            "type": "integer",
            "description": "dev_id"
          }
        }
      },
      "Registra": {
        "type": "object",
        "properties": {
          "rej_id": {
            "type": "integer",
            "description": "Identificador unico"
          },
          "rej_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID"
          },
          "rej_usu_id": {
            "type": "integer",
            "description": "usu_id"
          },
          "rej_com_id": {
            "type": "integer",
            "description": "com_id"
          }
        }
      }
    }
  }
}

@documentacion_bp.route("/swagger.json")
def swagger_json():
    return jsonify(SWAGGER_SPEC)

@documentacion_bp.route("/")
def swagger_ui():
    return render_template_string("""
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>ADSO-RP</title>
  <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css" />
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-standalone-preset.js"></script>
  <script>
    window.onload = function() {
      SwaggerUIBundle({
        url: "./swagger.json",
        dom_id: "#swagger-ui",
        presets: [SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset],
        layout: "StandaloneLayout"
      });
    };
  </script>
</body>
</html>
""")
