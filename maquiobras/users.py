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
from maquiobras.models import UserModel
from maquiobras.models import Ventas1Model, Ventas2Model, Ventas3Model
from datetime import datetime
import traceback, sys

api_users = Blueprint('api_users', __name__)
api = Api(api_users)


class UsersResource(Resource, BaseSerializer):
    users_parser = RequestParser()
    users_parser.add_argument("id", type=int, required=False, help="This user field cannot be left blank!")
    users_parser.add_argument("user", type=str, required=False, help="This user field cannot be left blank!")
    users_parser.add_argument("password", type=str, required=False, help="This password field cannot be left blank!")
    users_parser.add_argument("rol", type=str, required=False, help="This is_admin field cannot be left blank!")
    users_parser.add_argument("is_active", type=str, required=False, help="This is_admin field cannot be left blank!")
    users_parser.add_argument("sucursal", type=str, required=False, help="This is_admin field cannot be left blank!")

    def get(self):
        """
        Usuarios Maquiobras, traemos todo
        """
        data = UserModel.find_all_users()
        lista = []
        if not data:
            #return {"message": "No hay usuarios para visualizar."}, 404
            return lista, 200
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200


    def post(self):
        """
        Usuarios Maquiobras, creacion
        """
        dato = self.users_parser.parse_args()
        #print(dato.user)
        busco_user = UserModel.find_users_by_name(dato.user)
        #print(busco_user)
        lista = []

        if busco_user is not None:
            #return {'error': "Este usuario '{}' ya existe.".format(dato.user)}, 400
            return lista, 200
        else:
            try:
                fecha_update = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                data = {}
                data["user"] = dato.user
                data["password"] = dato.password
                data["rol"] = dato.rol
                data["is_active"] = 1
                data["fecha"] = fecha_update
                data["sucursal"] = dato.sucursal
                #print(data)
                user_insert = UserModel(**data)
                db.session.add(user_insert)
                db.session.commit()
                return {"message": "Usuario '{}' creado.".format(dato.user)}, 200
            
            except Exception as e:
                return e.args, 500
    
    def put(self):
        """
        Usuarios Maquiobras, metodo de modificacion
        """
        dato = self.users_parser.parse_args()
        get_user = UserModel.find_users_by_id(dato.id)
        lista = []

        if not get_user.id :
            #return {"message": "Invalid user id '{}'".format(dato.id)}, 400
            return lista, 200
        else:
            try:
                newDatos={}
                fecha_update = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                newDatos["id"] = dato.id
                newDatos["user"] = dato.user
                newDatos["password"] = dato.password
                newDatos["rol"] = dato.rol
                newDatos["is_active"] = dato.is_active
                newDatos["fecha"] = fecha_update
                newDatos["sucursal"] = dato.sucursal

                db.session.query(UserModel).filter(UserModel.id == dato.id).update(dict(newDatos))
                db.session.commit()

                return {'message': "The user id '{}' has been updated.".format(dato.id)}, 200

            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting the item."}, 500
    
    def delete(self):
        """
        Usuarios Maquiobras, metodo de borrado
        """
        dato = self.users_parser.parse_args()
        get_user = UserModel.find_users_by_id(dato.id)
        lista = []

        if not get_user:
            #return {"message": "Invalid user id '{}'".format(dato.id)}, 400
            return lista, 200
        else:
            try:
                db.session.delete(get_user)
                db.session.commit()
                return {'message': "The user has been deleted.".format(dato.id)}, 200
            
            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred deleting the item."}, 500
            



class VentasGetAll(Resource, BaseSerializer):
    
    def get(self):
        """
        Ventas Maquiobras, traemos todas las 3 Tablas de Ventas
        """
        ven1 = Ventas1Model.find_all_ventas1()
        ven2 = Ventas2Model.find_all_ventas2()
        ven3 = Ventas3Model.find_all_ventas3()

        lista = []
        
        for i in ven1:
            lista.append(i.serialize())

        for ii in ven2:
            lista.append(ii.serialize())
        
        for iii in ven3:
            lista.append(iii.serialize())

        return lista, 200




api.add_resource(UsersResource, '/api/users')
api.add_resource(VentasGetAll, '/api/ventas')
