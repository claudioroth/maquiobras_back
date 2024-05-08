from flask import Flask, Blueprint, jsonify
from flask_restful.reqparse import RequestParser
from flask_restful import Resource, Api

from maquiobras.helpers import BaseSerializer
from maquiobras.exts import db
from maquiobras.models import UserModel
import time
from datetime import datetime
import traceback, sys


api_login = Blueprint('api_login', __name__)
api = Api(api_login)


class Login(Resource, BaseSerializer):
    login_parser = RequestParser()
    login_parser.add_argument("user", type=str, required=False, help="This qlookid field cannot be left blank!")
    login_parser.add_argument("password", type=str, required=False, help="This password field cannot be left blank!")

    def post(self):
        """
        Login de acceso a Base de Datos
        """
        dato = self.login_parser.parse_args()
        res = UserModel.find_users_by_name(dato.user)
        if not res:
            return {"message": "ERR_BAD_RESPONSE"}, 500
        else:
            if res.user == dato.user and res.password == dato.password:
                time.sleep(1)
                try:
                    fecha_update = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    db.session.query(UserModel).filter(UserModel.user == dato.user).update(dict(fecha=fecha_update))
                    db.session.commit()

                except Exception as e:
                    #print(e)
                    traceback.print_exc(file=sys.stdout)
                    return {"message": "An error occurred inserting the item."}, 500
                return res.serialize(), 200
            else:
                return True, 404



api.add_resource(Login,   '/login')