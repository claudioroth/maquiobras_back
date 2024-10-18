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
    prod_parser.add_argument("descripcion", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("importe_sin_iva", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("iva_21", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("iva_10", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("oferta_sin_iva", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("aumento", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("ultimo_modif", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("oferta_costo", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("costo_mas_bajo", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("rentabilidad", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("stock", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("suc1", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("suc2", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser.add_argument("depo", type=int, required=False, help="This user field cannot be left blank!")


    def get(self):
        """
        Productos Maquiobras, get all
        """
        data = ProductsDetailModel.find_all_products_detail()
        lista = []
        if not data:
            #return {"message": "No hay productos para visualizar."}, 404
            return lista, 200
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
        lista = []

        if not dato:
            #return {"message": "Datos incorrectos para registrar"}, 500
            return lista, 200
        else:
            data_insert["nro"] = dato["nro"]
            data_insert["descripcion"] = dato["descripcion"]
            data_insert["importe_sin_iva"] = dato.importe_sin_iva
            data_insert["iva_21"] = dato.iva_21
            data_insert["iva_10"] = dato.iva_10
            data_insert["oferta_sin_iva"] = dato.oferta_sin_iva
            data_insert["aumento"] = dato.aumento
            data_insert["ultimo_modif"] = dato.ultimo_modif
            data_insert["oferta_costo"] = dato.oferta_costo
            data_insert["costo_mas_bajo"] = dato.costo_mas_bajo
            data_insert["rentabilidad"] = dato.rentabilidad
            data_insert["stock"] = dato.stock
            data_insert["suc1"] = dato.suc1
            data_insert["suc2"] = dato.suc2
            data_insert["depo"] = dato.depo

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
        lista = []

        if not get_product.index:
            #return {"message": "Invalid product index '{}'".format(dato.index)}, 400
            return lista, 200
        else:
            try:
                newDatos={}
                newDatos["index"] = dato.index
                newDatos["nro"] = dato.nro
                newDatos["descripcion"] = dato.descripcion
                newDatos["importe_sin_iva"] = dato.importe_sin_iva
                newDatos["iva_21"] = dato.iva_21
                newDatos["iva_10"] = dato.iva_10
                newDatos["oferta_sin_iva"] = dato.oferta_sin_iva
                newDatos["aumento"] = dato.aumento
                newDatos["ultimo_modif"] = dato.ultimo_modif
                newDatos["oferta_costo"] = dato.oferta_costo
                newDatos["costo_mas_bajo"] = dato.costo_mas_bajo
                newDatos["rentabilidad"] = dato.rentabilidad
                newDatos["stock"] = dato.stock
                newDatos["suc1"] = dato.suc1
                newDatos["suc2"] = dato.suc2
                newDatos["depo"] = dato.depo

                #print(newDatos)
                #return True
                if newDatos["suc1"] + newDatos["suc2"] + newDatos["depo"] <= newDatos["stock"]:
                    db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato.index).update(dict(newDatos))
                    db.session.commit()

                    return {'message': "The product index '{}' has been updated.".format(dato.index)}, 200
                
                else:
                    return {'message': "No se puede grabar en db por inconsistencia en stock."}, 400

            except Exception as e:
                print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred editing product_detail item."}, 500


    def delete(self):
        """
        Product_detail Maquiobras, metodo de borrado
        """
        # dato = self.prod_parser.parse_args()
        # get_product = ProductsDetailModel.find_products_by_index(dato.index)

        # if not get_product:
        #     return {"message": "Invalid product_detail index '{}'".format(dato.index)}, 400
        # else:
        #     try:
        #         db.session.delete(get_product)
        #         db.session.commit()
        #         return {'message': "The product_detail has been deleted.".format(dato.index)}, 200
            
        #     except Exception as e:
        #         #print(e)
        #         traceback.print_exc(file=sys.stdout)
        #         return {"message": "An error occurred deleting the item."}, 500
        return {"message": "Metodo deshabilitado."}, 200



class ProductDetailResources(Resource, BaseSerializer):

    prod_parser1 = RequestParser()
    prod_parser1.add_argument("index", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("nro", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("descripcion", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("importe_sin_iva", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("iva_21", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("iva_10", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("oferta_sin_iva", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("aumento", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("ultimo_modif", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("oferta_costo", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("costo_mas_bajo", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("rentabilidad", type=str, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("stock", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("suc1", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("suc2", type=int, required=False, help="This user field cannot be left blank!")
    prod_parser1.add_argument("depo", type=int, required=False, help="This user field cannot be left blank!")



    def get(self, index):
        get_prod = ProductsDetailModel.find_products_by_index(index)
        if not get_prod:
            return {"message": "The product_detail index '{}' doesnt exist.".format(index)}, 404
        else:
            return get_prod.serialize(), 200

    def delete(self, index):
        """
        Product_detail Maquiobras, metodo de borrado
        """

        get_product = ProductsDetailModel.find_products_by_index(index)

        if not get_product:
            return {"message": "Invalid product_detail index '{}'".format(index)}, 400
        else:
            try:
                db.session.delete(get_product)
                db.session.commit()
                return {'message': "The product_detail has been deleted.".format(index)}, 200
            
            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred deleting the item."}, 500


    def put(self, index):
        """
        Productos Detail Maquiobras, metodo de modificacion individual x item
        """
        dato = self.prod_parser1.parse_args()
        #print(dato)
        get_product = ProductsDetailModel.find_products_by_index(index)
        #print("get_product: ", get_product.serialize())

        if not get_product.index:
            return {"message": "Invalid product index '{}'".format(index)}, 400
        else:
            try:
                newDatos={}
                newDatos["index"] = dato.index
                newDatos["nro"] = dato.nro
                newDatos["descripcion"] = dato.descripcion
                newDatos["importe_sin_iva"] = dato.importe_sin_iva
                newDatos["iva_21"] = dato.iva_21
                newDatos["iva_10"] = dato.iva_10
                newDatos["oferta_sin_iva"] = dato.oferta_sin_iva
                newDatos["aumento"] = dato.aumento
                newDatos["ultimo_modif"] = dato.ultimo_modif
                newDatos["oferta_costo"] = dato.oferta_costo
                newDatos["costo_mas_bajo"] = dato.costo_mas_bajo
                newDatos["rentabilidad"] = dato.rentabilidad
                newDatos["stock"] = dato.stock
                newDatos["suc1"] = dato.suc1
                newDatos["suc2"] = dato.suc2
                newDatos["depo"] = dato.depo

                #print(newDatos)
                if newDatos["suc1"] + newDatos["suc2"] + newDatos["depo"] <= newDatos["stock"]:
                    db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato.index).update(dict(newDatos))
                    db.session.commit()
                    
                    return {'message': "The product index '{}' has been updated.".format(dato.index)}, 200
                
                else:
                    return {'message': "No se puede grabar en db por inconsistencia en stock."}, 400
                
                

            except Exception as e:
                print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred editing product_detail item."}, 500



api.add_resource(ProductDetailResource,  '/api/product_detail')
api.add_resource(ProductDetailResources, '/api/product_detail/<int:index>')

