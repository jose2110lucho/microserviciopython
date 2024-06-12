from flask import Flask

from config import config

#Routes
from routes import Ventacombustible
from routes import Ventaproducto

app=Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__=='__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(Ventacombustible.main,url_prefix='/api/ventacombustibles')
    app.register_blueprint(Ventaproducto.main,url_prefix='/api/ventaproductos')
    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
