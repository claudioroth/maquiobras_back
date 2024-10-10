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
from maquiobras.models import Ventas3Model, ProductsDetailModel
from datetime import datetime
import traceback, sys


api_ventas3 = Blueprint('api_ventas3', __name__)
api = Api(api_ventas3)


class Ventas3Resource(Resource, BaseSerializer):
    ventas3_parser = RequestParser()
    ventas3_parser.add_argument("id_user", type=int, required=False, help="This user field cannot be left blank!")
    ventas3_parser.add_argument("id_sucursal", type=str, required=False, help="This user field cannot be left blank!")
    ventas3_parser.add_argument("venta", type=str, required=False, help="This password field cannot be left blank!")
    ventas3_parser.add_argument("producto", type=str, required=False, help="This is_admin field cannot be left blank!")
    ventas3_parser.add_argument("id_prod", type=str, required=False, help="This is_admin field cannot be left blank!")
    
    def get(self):
        """
        Ventas1 Maquiobras, traemos todo
        """
        data = Ventas3Model.find_all_ventas3()
        lista = []
        if not data:
            return {"message": "No hay ventas3 para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200


    def post(self):
        """
        Post de Ventas3 = Sucursal Deposito
        """
        dato = self.ventas3_parser.parse_args()
        #print(dato)
        data_insert = {}
        stock_prod_depo = ProductsDetailModel.find_products_by_index(dato.id_prod)
        #print(stock_prod_depo.depo)
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            fecha_update = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            data_insert["id_user"] = dato.id_user
            data_insert["id_sucursal"] = dato.id_sucursal
            data_insert["venta"] = dato.venta
            data_insert["producto"] = dato.producto
            data_insert["id_prod"] = dato.id_prod
            data_insert["fecha"] = fecha_update
            
            #print(data_insert)
        
        #return True
            todosInsert = Ventas3Model(**data_insert)
            try:
                db.session.add(todosInsert)
                db.session.commit()
                
                try:
                    cant_nueva = int(stock_prod_depo.depo) - int(dato.venta)
                    new_stock =  int(stock_prod_depo.stock) - int(dato.venta)
                    db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato.id_prod).update(dict(depo=cant_nueva, stock=new_stock))
                    db.session.commit()
                
                except Exception as ee:
                    print(ee)
                    traceback.print_exc(file=sys.stdout)
                    return {"message": "An error occurred inserting product_detail cant_nueva."}, 500

                return {"message": "ok"}, 200

            except Exception as e:
                print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting product_detail item."}, 500






api.add_resource(Ventas3Resource, '/api/ventas3')