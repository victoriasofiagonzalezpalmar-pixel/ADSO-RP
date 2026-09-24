from .usuario import usuario_bp
from .almacena import almacena_bp
from .categoria import categoria_bp
from .clasifica import clasifica_bp
from .cliente import cliente_bp
from .compra import compra_bp
from .datocliente import datocliente_bp
from .datoproveedor import datoproveedor_bp
from .descripcion import descripcion_bp
from .devolucion import devolucion_bp
from .pagos import pagos_bp
from .producto import producto_bp
from .proveedor import proveedor_bp
from .realiza import realiza_bp
from .registra import registra_bp
from .documentacion import documentacion_bp
from .health import health_bp

def loadRoutes(app):
    app.register_blueprint(usuario_bp, url_prefix="/usuario")
    app.register_blueprint(almacena_bp, url_prefix="/almacena")
    app.register_blueprint(categoria_bp, url_prefix="/categoria")
    app.register_blueprint(clasifica_bp, url_prefix="/clasifica")
    app.register_blueprint(cliente_bp, url_prefix="/cliente")
    app.register_blueprint(compra_bp, url_prefix="/compra")
    app.register_blueprint(datocliente_bp, url_prefix="/datocliente")
    app.register_blueprint(datoproveedor_bp, url_prefix="/datoproveedor")
    app.register_blueprint(descripcion_bp, url_prefix="/descripcion")
    app.register_blueprint(devolucion_bp, url_prefix="/devolucion")
    app.register_blueprint(pagos_bp, url_prefix="/pagos")
    app.register_blueprint(producto_bp, url_prefix="/producto")
    app.register_blueprint(proveedor_bp, url_prefix="/proveedor")
    app.register_blueprint(realiza_bp, url_prefix="/realiza")
    app.register_blueprint(registra_bp, url_prefix="/registra")
    app.register_blueprint(documentacion_bp, url_prefix="/documentacion")
    app.register_blueprint(health_bp, url_prefix="/health")
