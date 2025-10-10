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
from maquiobras.models import IngresosModel, UserModel, ProductsDetailModel
from datetime import datetime
import traceback, sys


api_ingresos = Blueprint('api_ingresos', __name__)
api = Api(api_ingresos)


class IngresosResource(Resource, BaseSerializer):
    ingresos_parser = RequestParser()
    ingresos_parser.add_argument("id_user", type=int, required=False, help="This user field cannot be left blank!")
    ingresos_parser.add_argument("id_sucursal", type=str, required=False, help="This user field cannot be left blank!")
    ingresos_parser.add_argument("productos", type=str, required=False, help="This is_admin field cannot be left blank!", action="append")
    ingresos_parser.add_argument("semi_admin", type=str, required=False, help="This is_admin field cannot be left blank!")
    ingresos_parser.add_argument("remito", type=str, required=False, help="This is_admin field cannot be left blank!")




    def get(self):
        """
        Ingresos Maquiobras, traemos todo
        """
        data = IngresosModel.find_all_ingresos()
        lista = []
        if not data:
            #return {"message": "No hay ingresos para visualizar."}, 404
            return lista, 200
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200 
        
       



    def post(self):
        """
        Post de Ingresos
        """
        #dato = self.ingresos_parser.parse_args()

        dato = json.loads(request.form.get('data'))
        #print("dato: ", dato)
        #print("productos: ", dato["productos"])

        data_insert = {}
        lista = []
        if not dato:
            # return {"message": "Datos incorrectos para registrar"}, 500
            return lista, 200
        else:
            lista_productos = []
            fecha_update = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            data_insert["id_user"] = dato["id_user"]
            data_insert["id_sucursal"] = dato["id_sucursal"]
            data_insert["semi_admin"] = dato["semi_admin"]
            data_insert["remito"] = dato["remito"]
            data_insert["fecha"] = fecha_update
            
            for i in dato["productos"]:
                lista_productos.append(i)
            
            data_insert["productos"] = json.dumps(lista_productos)

            todosInsert = IngresosModel(**data_insert)
            
            try:
                db.session.add(todosInsert)
                db.session.commit()

                try:
                    if dato["id_sucursal"] == "suc1":
                        
                        for i in dato["productos"]:                     

                            stock_prod_suc1 = ProductsDetailModel.find_products_by_index(i["id_prod"])
                            cant_nueva = int(stock_prod_suc1.suc1) + int(i["cantidad"])
                            new_stock =  int(stock_prod_suc1.stock) + int(i["cantidad"])
                        
                            #print("cant_nueva: ", cant_nueva)
                        
                            db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == i["id_prod"]).update(dict(suc1=cant_nueva, stock=new_stock))
                            db.session.commit()

                        return {"message": "ok"}, 200                        


                    elif dato["id_sucursal"] == "suc2":
                        
                        for i in dato["productos"]:                     

                            stock_prod_suc2 = ProductsDetailModel.find_products_by_index(i["id_prod"])
                            cant_nueva = int(stock_prod_suc2.suc2) + int(i["cantidad"])
                            new_stock =  int(stock_prod_suc2.stock) + int(i["cantidad"])
                        
                            db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == i["id_prod"]).update(dict(suc2=cant_nueva, stock=new_stock))
                            db.session.commit()

                        return {"message": "ok"}, 200          


                    elif dato["id_sucursal"] == "depo":
                        
                        for i in dato["productos"]:                     

                            stock_prod_depo = ProductsDetailModel.find_products_by_index(i["id_prod"])
                            cant_nueva = int(stock_prod_depo.depo) + int(i["cantidad"])
                            new_stock =  int(stock_prod_depo.stock) + int(i["cantidad"])
                        
                            db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == i["id_prod"]).update(dict(depo=cant_nueva, stock=new_stock))
                            db.session.commit()

                        return {"message": "ok"}, 200          

                    # elif dato.id_sucursal == "suc2":
                    #     stock_prod_suc2 = ProductsDetailModel.find_products_by_index(dato.id_prod)
                    #     cant_nueva = int(stock_prod_suc2.suc2) + int(dato.cantidad)
                    #     new_stock =  int(stock_prod_suc2.stock) + int(dato.cantidad)
                        
                    #     db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato.id_prod).update(dict(suc2=cant_nueva, stock=new_stock))
                    #     db.session.commit()

                    #     return {"message": "ok"}, 200

                    # elif dato.id_sucursal == "depo":
                    #     stock_prod_depo = ProductsDetailModel.find_products_by_index(dato.id_prod)
                    #     cant_nueva = int(stock_prod_depo.suc2) + int(dato.cantidad)
                    #     new_stock =  int(stock_prod_depo.stock) + int(dato.cantidad)
                        
                    #     db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato.id_prod).update(dict(depo=cant_nueva, stock=new_stock))
                    #     db.session.commit()

                    #     return {"message": "ok"}, 200


                    

                except Exception as ee:
                    print(ee)
                    traceback.print_exc(file=sys.stdout)
                    return {"message": "An error occurred inserting Ingresos Resource cant_nueva."}, 500

            
            except Exception as e:
                print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting product_detail item."}, 500
            

class IngresoResource(Resource, BaseSerializer):
    
    def get(self, id):
        """
        Ingreso Maquiobras, traemos todo pasar dato suc1, suc2, depo
        """
        #print("id: ", id)
        data = IngresosModel.find_all_ingresos_by_suc(id=id)
        lista = []
        if not data:
            #return {"message": "No hay ingresos para visualizar."}, 404
            return lista, 200
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200





class SemiAdminResource(Resource, BaseSerializer):

    def get(self):
        dato = UserModel.find_semiadmin_users()
        lista = []
        if not dato:
            #return {"message": "No hay usuarios semi-admin para mostrar"}, 404
            return lista, 200
        else:
            for i in dato:
                lista.append(i.serialize())
            return lista, 200




api.add_resource(IngresosResource,  '/api/ingresos')
api.add_resource(IngresoResource,   '/api/ingreso/<string:id>')
api.add_resource(SemiAdminResource, '/api/semiadmin')



#{
#	"id_user": 22,
#	"id_sucursal": "suc1",
#	"semi_admin": 3,
#	"remito": "0017-00000123",
#	"fecha": "2025-10-10 10:12:27",
#	"productos": [
#		{"id_prod": 1, "producto": "ABRAZADERA PLASTICA 100 x 2,5 ABR1100", "cantidad": 10},
#		{"id_prod": 2, "producto": "ABRAZADERA PLASTICA 150 x 3,6 ABR1160", "cantidad": 10}
#	]
#}