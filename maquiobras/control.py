from flask import Flask, Blueprint, jsonify
from flask_restful.reqparse import RequestParser
from flask_restful import Resource, Api

from maquiobras.exts import db
from maquiobras.helpers import BaseSerializer
from sqlalchemy import or_, and_
from sqlalchemy.ext import mutable
#from sqlalchemy_filters import apply_pagination
import json
from string import capwords
from maquiobras.models import ControlModel, UserModel, ProductsModel, ProductsDetailModel
import sys
import traceback
from datetime import datetime

api_control = Blueprint('api_control', __name__)
api = Api(api_control)


class ControlResource(Resource, BaseSerializer):

    control_parser = RequestParser()
    control_parser.add_argument("retiro", type=int, required=False, help="This password field cannot be left blank!")
    control_parser.add_argument("id_user", type=int, required=False, help="This is_admin field cannot be left blank!")
    control_parser.add_argument("id_prod", type=int, required=False, help="This user field cannot be left blank!")

    def get(self):
        """
        Control Resource para materiales
        """
        data = ControlModel.find_all_control()
        lista = []

        if not data:
            return {"message": "No hay data para mostrar."}, 404
        else:
            for i in data:
                res = {}
                #lista.append(i.serialize())
                res["id"] = i.id
                res["retiro"] = i.retiro
                res["fecha"] = i.fecha.strftime('%Y-%m-%d %H:%M:%S')

                users_lista = UserModel.find_users_by_id(i.id_user)
                prod_lista = ProductsModel.find_products_by_id(i.id_prod)

                res["nombre"] = users_lista.user
                res["producto"] = prod_lista.nombre_prod
                lista.append(res)
            
            #aca falta hacer la resta de la cantidad total que hay en productos respecto a lo que se saca.
            return lista, 200



    def post(self):
        """
        Control Resource para materiales
        """
        dato = self.control_parser.parse_args()
        #print(dato)
        data_insert = {}
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            data_insert["retiro"] = dato["retiro"]
            data_insert["id_user"] = dato["id_user"]
            data_insert["id_prod"] = dato["id_prod"]
            data_insert["fecha"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            todosInsert = ControlModel(**data_insert)
            try:
                db.session.add(todosInsert)
                db.session.commit()
                return {"message": "ok"}, 200
            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting the item."}, 50


class ControlMixResourse(Resource, BaseSerializer):
    
    controlmix_parser = RequestParser()
    controlmix_parser.add_argument("id", type=int, required=False, help="This password field cannot be left blank!")
    

    def get(self):
        #dato = self.controlmix_parser.parse_args()
        #print(dato)
        get_user = UserModel.find_all_users()
        get_product_detail = ProductsDetailModel.find_all_products_detail()

        data = {}
        lista = []
        lista_users = []

        
        for ii in get_user:
            lista_users.append(ii.serialize()["user"])
        
        data["user"] = lista_users

        for i in get_product_detail:
            #print("i: ", i.serialize()["nro"])
            #print("i: ", i.serialize()["descripcion"])
            lista.append(i.serialize()["descripcion"])

        data["productos"] = lista
        #print(data)

        return data


api.add_resource(ControlResource, '/api/control')
api.add_resource(ControlMixResourse, '/api/controlmix')