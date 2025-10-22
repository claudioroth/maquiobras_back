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
from maquiobras.models import ControlModel, UserModel, ProductsDetailModel
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
    control_parser.add_argument("descripcion", type=str, required=False, help="This user field cannot be left blank!")
    control_parser.add_argument("local", type=str, required=False, help="This user field cannot be left blank!")
    control_parser.add_argument("destino", type=str, required=False, help="This user field cannot be left blank!")

    def get(self):
        """
        Control Resource para materiales
        """
        data = ControlModel.find_all_control()
        lista = []

        if not data:
            # return {"message": "No hay data para mostrar."}, 404
            return lista, 200
        else:
            for i in data:
                #print("i: ", i.serialize())
                res = {}
                res["id"] = i.id
                res["retiro"] = i.retiro
                res["fecha"] = i.fecha.strftime('%Y-%m-%d %H:%M:%S')
                res["local"] = i.local
                res["destino"] = i.destino

                users_lista = UserModel.find_users_by_id(i.id_user)
                #prod_lista = ProductsDetailModel.find_products_by_index(i.id_prod)
                res["nombre"] = users_lista.user
                res["producto"] = i.id_prod
                
                lista.append(res)

            return lista, 200



    def post(self):
        """
        Control Resource para materiales
        """
        dato = self.control_parser.parse_args()
        #print("retiro: ", dato["retiro"])
        #print("dato: ", dato)
        dato_producto = ProductsDetailModel.find_products_by_index(dato.id_prod)
        #print("stock: ", dato_producto.stock)
        #print(dato_producto.serialize())
        data_insert = {}
        
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            if dato_producto.stock >= dato["retiro"]:    #si hay stock de cantidad del prod mas o igual que lo q quiero sacar
                data_insert["retiro"] = dato["retiro"]
                data_insert["id_user"] = dato["id_user"]
                data_insert["id_prod"] = dato["descripcion"]
                data_insert["fecha"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                data_insert["local"] = dato["local"]
                data_insert["destino"] = dato["destino"]
                todosInsert = ControlModel(**data_insert)
                try:
                    db.session.add(todosInsert)
                    db.session.commit()
                    
                    try:
                        cant_nueva = int(dato_producto.stock) - int(dato["retiro"])
                        #print("cant_nueva: ", cant_nueva)

                        if data_insert["local"] == "Local Galicia":
                            cant_nueva_suc = int(dato_producto.suc1) - int(dato["retiro"])
                            if dato["destino"] == "Deposito":
                                cant_nueva_destino = int(dato_producto.depo) + int(dato["retiro"])
                                #db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(stock=cant_nueva, suc1=cant_nueva_suc, depo=cant_nueva_destino))
                                db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(suc1=cant_nueva_suc, depo=cant_nueva_destino))
                            elif dato["destino"] == "Local Juan B Justo":
                                cant_nueva_destino = int(dato_producto.suc2) + int(dato["retiro"])
                                #db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(stock=cant_nueva, suc1=cant_nueva_suc, suc2=cant_nueva_destino))
                                db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(suc1=cant_nueva_suc, suc2=cant_nueva_destino))
                            
                            

                        elif data_insert["local"] == "Local Juan B Justo":
                            cant_nueva_suc = int(dato_producto.suc2) - int(dato["retiro"])
                            if dato["destino"] == "Deposito":
                                cant_nueva_destino = int(dato_producto.depo) + int(dato["retiro"])
                                #db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(stock=cant_nueva, suc2=cant_nueva_suc, depo=cant_nueva_destino))
                                db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(suc2=cant_nueva_suc, depo=cant_nueva_destino))
                            elif dato["destino"] == "Local Galicia":
                                cant_nueva_destino = int(dato_producto.suc1) + int(dato["retiro"])
                                #db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(stock=cant_nueva, suc2=cant_nueva_suc, suc1=cant_nueva_destino))
                                db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(suc2=cant_nueva_suc, suc1=cant_nueva_destino))

                            

                        elif data_insert["local"] == "Deposito":
                            cant_nueva_suc = int(dato_producto.depo) - int(dato["retiro"])
                            if dato["destino"] == "Local Galicia":
                                cant_nueva_destino = int(dato_producto.suc1) + int(dato["retiro"])
                                #db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(stock=cant_nueva, depo=cant_nueva_suc, suc1=cant_nueva_destino))
                                db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(depo=cant_nueva_suc, suc1=cant_nueva_destino))
                            elif dato["destino"] == "Local Juan B Justo":
                                cant_nueva_destino = int(dato_producto.suc2) + int(dato["retiro"])
                                #db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(stock=cant_nueva, depo=cant_nueva_suc, suc2=cant_nueva_destino))
                                db.session.query(ProductsDetailModel).filter(ProductsDetailModel.index == dato["id_prod"]).update(dict(depo=cant_nueva_suc, suc2=cant_nueva_destino))

                            
                
                        db.session.commit()

                        return {"message": "ok"}, 200

                    except Exception as ee:
                        print(ee)
                        traceback.print_exc(file=sys.stdout)
                        return {"message": "An error occurred inserting product_detail cant."}, 500    
                    
                    
                
                except Exception as e:
                    print(e)
                    traceback.print_exc(file=sys.stdout)
                    return {"message": "An error occurred inserting control."}, 500
            else:
                return {"message": "Stock Quantity less than Quantity of control."}, 404


class ControlMixResourse(Resource, BaseSerializer):
    
    controlmix_parser = RequestParser()
    controlmix_parser.add_argument("id", type=int, required=False, help="This password field cannot be left blank!")
    

    def get(self):
        #dato = self.controlmix_parser.parse_args()
        #print(dato)
        get_user = UserModel.find_all_active_users()
        get_product_detail = ProductsDetailModel.find_all_productos_with_stock()

        data = {}
        lista = []
        lista_users = []

        
        for ii in get_user:
            user_interno = {}
            user_interno["id"] = ii.serialize()["id"]
            user_interno["user"] = ii.serialize()["user"]
            lista_users.append(user_interno)
        
        data["user"] = lista_users

        for i in get_product_detail:
            lista_interno = {}
            #print("i: ", i.serialize())
            lista_interno["index"] = i.serialize()["index"]
            lista_interno["nro"] = i.serialize()["nro"]
            lista_interno["descripcion"] = i.serialize()["descripcion"]
            lista_interno["stock"] = i.serialize()["stock"]
            lista_interno["suc1"] = i.serialize()["suc1"]
            lista_interno["suc2"] = i.serialize()["suc2"]
            lista_interno["depo"] = i.serialize()["depo"]
            lista.append(lista_interno)
            

        data["productos"] = lista

        return data


class ControlMixResourses(Resource, BaseSerializer):
    

    def get(self, suc):
        #print(suc)
        get_tools_by_suc = ProductsDetailModel.find_products_by_sucursal(suc)
        
        #print(get_tools_by_suc)
        lista=[]

        if not get_tools_by_suc:
            return lista, 200
        else:
            for i in get_tools_by_suc:
                #print("i: ", i.serialize())
                lista.append(i.serialize())

            return lista, 200
        


class ControlGetAll(Resource, BaseSerializer):
    
    

    def get(self):
        #dato = self.controlmix_parser.parse_args()
        #print(dato)
        get_user = UserModel.find_all_active_users()
        get_product_detail = ProductsDetailModel.find_all_products_by_alphabetic_order()

        data = {}
        lista = []
        lista_users = []

        
        for ii in get_user:
            user_interno = {}
            user_interno["id"] = ii.serialize()["id"]
            user_interno["user"] = ii.serialize()["user"]
            lista_users.append(user_interno)
        
        data["user"] = lista_users

        for i in get_product_detail:
            lista_interno = {}
            #print("i: ", i.serialize())
            lista_interno["index"] = i.serialize()["index"]
            lista_interno["nro"] = i.serialize()["nro"]
            lista_interno["descripcion"] = i.serialize()["descripcion"]
            lista_interno["stock"] = i.serialize()["stock"]
            lista_interno["suc1"] = i.serialize()["suc1"]
            lista_interno["suc2"] = i.serialize()["suc2"]
            lista_interno["depo"] = i.serialize()["depo"]
            lista.append(lista_interno)
            

        data["productos"] = lista

        return data



api.add_resource(ControlResource,     '/api/control')
api.add_resource(ControlMixResourse,  '/api/controlmix')
api.add_resource(ControlMixResourses, '/api/controlmix/<string:suc>')
api.add_resource(ControlGetAll,       '/api/allproducts')