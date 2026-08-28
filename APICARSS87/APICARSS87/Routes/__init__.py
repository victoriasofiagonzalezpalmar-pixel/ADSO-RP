from .Car import car_bp


def loadRoutes(app):

    app.register_blueprint(car_bp,url_prefix="/cars")


 