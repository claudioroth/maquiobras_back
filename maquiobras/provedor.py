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
from maquiobras.models import ProvedorModel
import sys
import traceback
from datetime import datetime

api_provedor = Blueprint('api_provedor', __name__)
api = Api(api_provedor)


class ProvedorResource(Resource, BaseSerializer):

    provedor_parser = RequestParser()
    provedor_parser.add_argument("prov_id", type=str, required=False, help="This password field cannot be left blank!")
    provedor_parser.add_argument("nombre", type=str, required=False, help="This is_admin field cannot be left blank!")

    def get(self):
        data = ProvedorModel.find_all_prov()
        lista = []
        if not data:
            return {"message": "No hay provedor para visualizar."}, 404
        else:
            for i in data:
                lista.append(i.serialize())
            return lista, 200


    def post(self):
        """
        Provedor Maquiobras
        """
        dato = self.provedor_parser.parse_args()
        #print(dato)
        #print("dato.prov_id: ", dato.prov_id)
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            
            get_provedor = ProvedorModel.find_prov_by_id(dato.prov_id)
            #print(get_provedor.serialize())
            #print("get_provedor.prov_id: ", get_provedor.prov_id)

            if get_provedor:
                if int(get_provedor.prov_id) == int(dato.prov_id):
                    return {"message": "Este numero de Proveedor ya existe, id: {}".format(dato.prov_id)}, 200
            else:
            

                try:
                    newInsert = {}
                    newInsert["prov_id"] = dato.prov_id
                    newInsert["nombre"] = dato.nombre
                    newInsert["fecha"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    
                    todosInsert = ProvedorModel(**newInsert)

                    db.session.add(todosInsert)
                    db.session.commit()
                    return {"message": "ok"}, 200
                except Exception as e:
                    #print(e)
                    traceback.print_exc(file=sys.stdout)
                    return {"message": "An error occurred inserting the item."}, 500

    
    def put(self):
        """
        Proveedor Maquiobras, metodo de modificacion
        """
        dato = self.provedor_parser.parse_args()
        #print("dato: ", dato)
        get_provedor = ProvedorModel.find_prov_by_id(dato.prov_id)
        lista = []

        if not get_provedor :
            #return {"message": "Invalid Provedor id '{}'".format(dato.prov_id)}, 400
            return lista, 200
        else:
            
            try:
                newDatos={}
                newDatos["prov_id"] = dato.prov_id
                newDatos["nombre"] = dato.nombre
                newDatos["fecha"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                #print(newDatos)
                db.session.query(ProvedorModel).filter(ProvedorModel.prov_id == dato.prov_id).update(dict(newDatos))
                db.session.commit()

                return {'message': "The Proveedor id '{}' has been updated.".format(dato.prov_id)}, 200

            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting the item."}, 500


    
api.add_resource(ProvedorResource, '/api/provedor')

