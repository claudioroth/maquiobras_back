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
from datetime import datetime

api_product_detail = Blueprint('api_product_detail', __name__)
api = Api(api_product_detail)

class ProductDetailResource(Resource, BaseSerializer):

    prod_parser = RequestParser()
    prod_parser.add_argument("index", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("nro", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("venta_iva", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("descripcion", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("lista_vieja", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("importe", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("iva_21", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("iva_10", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("oferta_sin_iva", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("aumento", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("ultimo_modif", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("prov1", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("prov2", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("prov3", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("oferta", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("costo_bajo", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("costo_bajo1", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("rentab", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("venta", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("un_18", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("venta_oferta", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("cantidad", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("estado", type=str, required=False, help="This user field cannot be left blank!")


    def get(self):
        """
        Productos Maquiobras, get all
        """
        data = ProductsDetailModel.find_all_products_detail()
        lista = []
        if not data:
            return {"message": "No hay productos para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200
    

    def post(self):
        """
        Productos Maquiobras Post, creacion de productos
        """
        dato = self.prod_parser.parse_args()
        #print(dato)
        data_insert = {}
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            data_insert["nro"] = dato["nro"]
            data_insert["descripcion"] = dato["descripcion"]
            data_insert["cantidad"] = dato["cantidad"]
            data_insert["estado"] = dato["estado"]
            data_insert["ultimo_modif"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            
            todosInsert = ProductsDetailModel(**data_insert)
            try:
                db.session.add(todosInsert)
                db.session.commit()
                return {"message": "ok"}, 200

            except Exception as e:
                print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting product_detail item."}, 500


    def put(self):
        """
        Productos Detail Maquiobras, metodo de modificacion
        """
        dato = self.prod_parser.parse_args()
        #print(dato)
        get_product = ProductsDetailModel.find_products_by_index(dato.index)
        #print("get_product: ", get_product.serialize())

        if not get_product.index:
            return {"message": "Invalid product index '{}'".format(dato.index)}, 400
        else:
            try:
                newDatos={}
                newDatos["index"] = dato.index
                newDatos["nro"] = dato.nro
                newDatos["venta_iva"] = dato.venta_iva
                newDatos["descripcion"] = dato.descripcion
                newDatos["lista_vieja"] = dato.lista_vieja
                newDatos["importe"] = dato.importe
                newDatos["iva_21"] = dato.iva_21
                newDatos["iva_10"] = dato.iva_10
                newDatos["oferta_sin_iva"] = dato.oferta_sin_iva
                newDatos["aumento"] = dato.aumento
                newDatos["ultimo_modif"] = dato.ultimo_modif
                newDatos["prov1"] = dato.prov1
                newDatos["prov2"] = dato.prov2
                newDatos["prov3"] = dato.prov3
                newDatos["oferta"] = dato.oferta
                newDatos["costo_bajo"] = dato.costo_bajo
                newDatos["costo_bajo1"] = dato.costo_bajo1
                newDatos["rentab"] = dato.rentab
                newDatos["venta"] = dato.venta
                newDatos["un_18"] = dato.un_18
                newDatos["venta_oferta"] = dato.venta_oferta
                newDatos["cantidad"] = dato.cantidad
                newDatos["estado"] = dato.estado

                #print(newDatos)
                #return True
                db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato.index).update(dict(newDatos))
                db.session.commit()

                return {'message': "The product index '{}' has been updated.".format(dato.index)}, 200

            except Exception as e:
                print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred editing product_detail item."}, 500


    def delete(self):
        """
        Product_detail Maquiobras, metodo de borrado
        """
        dato = self.prod_parser.parse_args()
        get_product = ProductsDetailModel.find_products_by_index(dato.index)

        if not get_product:
            return {"message": "Invalid product_detail index '{}'".format(dato.index)}, 400
        else:
            try:
                db.session.delete(get_product)
                db.session.commit()
                return {'message': "The product_detail has been deleted.".format(dato.index)}, 200
            
            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred deleting the item."}, 500



class ProductDetailResources(Resource, BaseSerializer):
    def get(self, index):
        get_prod = ProductsDetailModel.find_products_by_index(index)
        if not get_prod:
            return {"message": "The product_detail index '{}' doesnt exist.".format(index)}, 404
        else:
            return get_prod.serialize(), 200


api.add_resource(ProductDetailResource,  '/api/product_detail')
api.add_resource(ProductDetailResources, '/api/product_detail/<int:index>')

