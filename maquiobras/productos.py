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
from maquiobras.models import ProductsModel
import sys
import traceback

api_product = Blueprint('api_product', __name__)
api = Api(api_product)


class ProductResource(Resource, BaseSerializer):

    product_parser = RequestParser()
    product_parser.add_argument("nombre_prod", type=str, required=False, help="This password field cannot be left blank!")
    product_parser.add_argument("tipo_prod", type=str, required=False, help="This is_admin field cannot be left blank!")
    product_parser.add_argument("cantidad", type=str, required=False, help="This user field cannot be left blank!")
    product_parser.add_argument("descripcion", type=str, required=False, help="This user field cannot be left blank!")

    def get(self):
        data = ProductsModel.find_all_products()
        lista = []
        if not data:
            return {"message": "No hay productos para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200


    def post(self):
        """
        Productos Maquiobras
        """
        dato = self.product_parser.parse_args()
        #print(dato)
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            todosInsert = ProductsModel(**dato)
            try:
                db.session.add(todosInsert)
                db.session.commit()
                return {"message": "ok"}, 200
            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting the item."}, 500

    
api.add_resource(ProductResource, '/api/product')

