from flask import Flask, jsonify
from maquiobras.exts import db, cors, api
from maquiobras.utils import ApiException
#from maquiobras.productos import api_product
from maquiobras.provedor import api_provedor
from maquiobras.control import api_control
from maquiobras.users import api_users
from maquiobras.product_detail import api_product_detail
from maquiobras.ingresos import api_ingresos
from maquiobras.ventas1 import api_ventas1
from maquiobras.ventas2 import api_ventas2
from maquiobras.ventas3 import api_ventas3


from login import api_login


def register_exts(app):
    db.init_app(app)
    cors.init_app(app, support_credentials=True)
    api.init_app(app)

def register_error_handlers(app):
    app.register_error_handler(ApiException, lambda err: err.to_result())

def register_blueprints(app):
    app.register_blueprint(api_login)
    #app.register_blueprint(api_product)
    app.register_blueprint(api_control)
    app.register_blueprint(api_users)
    app.register_blueprint(api_provedor)
    app.register_blueprint(api_product_detail)
    app.register_blueprint(api_ingresos)
    app.register_blueprint(api_ventas1)
    app.register_blueprint(api_ventas2)
    app.register_blueprint(api_ventas3)



def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    register_exts(app)
    register_error_handlers(app)
    register_blueprints(app)
    return app


app = create_app("maquiobras/config.py")


@app.route("/")
def index():
    message = {'status': 200, 'message': 'Welcome'}
    resp = jsonify(message)
    resp.status_code = 200
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': 'Not Found'}
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.errorhandler(500)
def special_exception_handler(error):
    message = {'status': 500, 'message': 'Database Error'}
    resp = jsonify(message)
    resp.status_code = 500
    return resp





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5115)
