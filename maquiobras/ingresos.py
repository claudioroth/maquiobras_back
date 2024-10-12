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
from maquiobras.models import IngresosModel
from datetime import datetime
import traceback, sys


api_ingresos = Blueprint('api_ingresos', __name__)
api = Api(api_ingresos)


class IngresosResource(Resource, BaseSerializer):
    ingresos_parser = RequestParser()
    ingresos_parser.add_argument("id_user", type=int, required=False, help="This user field cannot be left blank!")
    ingresos_parser.add_argument("id_sucursal", type=str, required=False, help="This user field cannot be left blank!")
    ingresos_parser.add_argument("cantidad", type=str, required=False, help="This password field cannot be left blank!")
    ingresos_parser.add_argument("producto", type=str, required=False, help="This is_admin field cannot be left blank!")
    ingresos_parser.add_argument("semi_admin", type=str, required=False, help="This is_admin field cannot be left blank!")
    ingresos_parser.add_argument("remito", type=str, required=False, help="This is_admin field cannot be left blank!")




    def get(self):
        """
        Ingresos Maquiobras, traemos todo
        """
        data = IngresosModel.find_all_ingresos()
        lista = []
        if not data:
            return {"message": "No hay ingresos para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200



    def post(self):
        """
        Post de Ingresos
        """
        dato = self.ingresos_parser.parse_args()
        #print(dato)
        data_insert = {}
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            fecha_update = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            data_insert["id_user"] = dato.id_user
            data_insert["id_sucursal"] = dato.id_sucursal
            data_insert["cantidad"] = dato.cantidad
            data_insert["producto"] = dato.producto
            data_insert["semi_admin"] = dato.semi_admin
            data_insert["remito"] = dato.remito
            data_insert["fecha"] = fecha_update
            
            #print(data_insert)
            todosInsert = IngresosModel(**data_insert)
            try:
                db.session.add(todosInsert)
                db.session.commit()
                return {"message": "ok"}, 200

            except Exception as e:
                print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting product_detail item."}, 500
            

class IngresoResource(Resource, BaseSerializer):
    
    def get(self, id):
        """
        Ingreso Maquiobras, traemos todo
        """
        data = IngresosModel.find_all_ingresos_by_suc(id=id)
        lista = []
        if not data:
            return {"message": "No hay ingresos para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200




api.add_resource(IngresosResource, '/api/ingresos')
api.add_resource(IngresoResource,  '/api/ingreso/<int:id>')