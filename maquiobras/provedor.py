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
        if not dato:
            return {"message": "Datos incorrectos para registrar"}, 500
        else:
            todosInsert = ProvedorModel(**dato)
            try:
                db.session.add(todosInsert)
                db.session.commit()
                return {"message": "ok"}, 200
            except Exception as e:
                #print(e)
                traceback.print_exc(file=sys.stdout)
                return {"message": "An error occurred inserting the item."}, 500

    
api.add_resource(ProvedorResource, '/api/provedor')

