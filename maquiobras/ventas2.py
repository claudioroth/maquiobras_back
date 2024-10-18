from flask import Flask, Blueprint, jsonify, request
from flask_restful.reqparse import RequestParser
from flask_restful import Resource, Api

from maquiobras.exts import db
from maquiobras.helpers import BaseSerializer
from sqlalchemy import or_, and_
from sqlalchemy.ext import mutable
#from sqlalchemy_filters import apply_pagination
import json
from string import capwords
from maquiobras.models import Ventas2Model, ProductsDetailModel
from datetime import datetime
import traceback, sys


api_ventas2 = Blueprint('api_ventas2', __name__)
api = Api(api_ventas2)


class Ventas2Resource(Resource, BaseSerializer):
    ventas2_parser = RequestParser()
    ventas2_parser.add_argument("id_user", type=int, required=False, help="This user field cannot be left blank!")
    ventas2_parser.add_argument("id_sucursal", type=str, required=False, help="This user field cannot be left blank!")
    ventas2_parser.add_argument("ventas", type=str, required=False, help="This password field cannot be left blank!")

    
    def get(self):
        """
        Ventas2 Maquiobras, traemos todo
        """
        data = Ventas2Model.find_all_ventas2()
        lista = []
        data_final = {}

        if not data:
            return {"message": "No hay ventas2 para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200
            # for i in data:
            #     print(i.serialize()["ventas"])
            #     for ii in i.serialize()["ventas"]:
            #         x = json.loads(ii)
            #     break
            #     print(x)
        #return True    
            


    def post(self):
        """
        Post de Ventas2 = Sucursal Galicia
        """

        dato = json.loads(request.form.get('data'))
        #print("dato: ", dato)
        #print("ventas: ", dato["ventas"])
        data_insert = {}

        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            lista_ventas = []
            fecha_update = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            data_insert["id_user"] = dato["id_user"]
            data_insert["id_sucursal"] = dato["id_sucursal"]
            #data_insert["venta"] = dato.venta
            data_insert["fecha"] = fecha_update
            
            for i in dato["ventas"]:
                lista_ventas.append(i)
            
            data_insert["ventas"] = json.dumps(lista_ventas)
        

            todosInsert = Ventas2Model(**data_insert)
            try:
                db.session.add(todosInsert)
                db.session.commit()
                
                try:
                    for o in dato["ventas"]:
                        stock_prod_suc2 = ProductsDetailModel.find_products_by_index(o["id_prod"])
                        cant_nueva = int(stock_prod_suc2.suc2) - int(o["cantidad"])
                        new_stock =  int(stock_prod_suc2.stock) - int(o["cantidad"])
                        db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == o["id_prod"]).update(dict(suc2=cant_nueva, stock=new_stock))
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






api.add_resource(Ventas2Resource, '/api/ventas2')