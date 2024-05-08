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
from maquiobras.models import ProductsDetailModel
import sys
import traceback

api_product_detail = Blueprint('api_product_detail', __name__)
api = Api(api_product_detail)

class ProductDetailResource(Resource, BaseSerializer):

    def get(self):
        data = ProductsDetailModel.find_all_products_detail()
        lista = []
        if not data:
            return {"message": "No hay productos para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200


api.add_resource(ProductDetailResource, '/api/product_detail')