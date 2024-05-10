from maquiobras.exts import db
from maquiobras.helpers import BaseSerializer
from sqlalchemy import or_, and_
from sqlalchemy.ext import mutable
#from sqlalchemy_filters import apply_pagination
import json
from string import capwords
from datetime import datetime

class UserModel(db.Model, BaseSerializer):
    __tablename__ = 'users'
    __bind_key__ = 'maquiobrasdb'

    fields = ['id', 'user', 'password', 'is_admin', 'is_active', 'fecha']

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String)
    password = db.Column(db.String)
    is_admin = db.Column(db.Integer)
    is_active = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)

    @classmethod
    def find_all_users(cls):
        return cls.query.all()

    @classmethod
    def find_users_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_users_by_name(cls, user):
        return cls.query.filter_by(user=user).first()


class ControlModel(db.Model, BaseSerializer):
    __tablename__ = 'control'
    __bind_key__ = 'maquiobrasdb'

    fields = ['id', 'id_user', 'id_prod', 'retiro', 'fecha']

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    id_prod = db.Column(db.Integer)
    retiro = db.Column(db.Integer)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def find_all_control(cls):
        #return cls.query.all()
        return cls.query.order_by(ControlModel.id.desc())
    

class ProductsModel(db.Model, BaseSerializer):
    __tablename__ = 'products'
    __bind_key__ = 'maquiobrasdb'

    fields = ['id', 'nombre_prod', 'tipo_prod', 'cantidad', 'descripcion']

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre_prod = db.Column(db.Integer)
    tipo_prod = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)
    descripcion = db.Column(db.DateTime)

    @classmethod
    def find_all_products(cls):
        return cls.query.all()
    
    @classmethod
    def find_products_by_id(cls, id):
        return cls.query.filter_by(id=id).first()



class ProvedorModel(db.Model, BaseSerializer):
    __tablename__ = 'provedor'
    __bind_key__ = 'maquiobrasdb'

    fields = ['id', 'prov_id', 'nombre']

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    prov_id = db.Column(db.Integer)
    nombre = db.Column(db.String)

    @classmethod
    def find_all_prov(cls):
        return cls.query.all()
    

class ProductsDetailModel(db.Model, BaseSerializer):
    __tablename__ = 'product_detail'
    __bind_key__ = 'maquiobrasdb'

    fields = ['index', 'nro', 'venta_iva', 'descripcion', 'lista_vieja', 'importe', 'iva_21', 'iva_10', 'oferta_sin_iva',
              'aumento', 'ultimo_modif', 'prov1', 'prov2', 'prov3', 'oferta', 'costo_bajo', 'costo_bajo1', 'rentab',
              'venta', 'un_18', 'venta_oferta']


    index = db.Column('index', db.Integer, primary_key=True, autoincrement=True)
    nro = db.Column('N°', db.String)
    venta_iva = db.Column('VENTA + 1/2 IVA',db.String)
    descripcion = db.Column('DESCRIPCION', db.String)
    lista_vieja = db.Column('LISTA VIEJA', db.String)
    importe = db.Column('IMPORTE', db.String)
    iva_21 = db.Column('C/IVA 21%', db.String)
    iva_10 = db.Column('C/IVA 10.5%', db.String)
    oferta_sin_iva = db.Column('OFERTA SIN IVA', db.String)
    aumento = db.Column('AUMENTO', db.String)
    ultimo_modif = db.Column('ULT.MODIF.', db.String)
    prov1 = db.Column('PROV.1', db.String)
    prov2 = db.Column('PROV.2', db.String)
    prov3 = db.Column('PROV.3', db.String)
    oferta = db.Column('OFERTA', db.String)
    costo_bajo = db.Column('COSTO MAS BAJO', db.String)
    costo_bajo1 = db.Column('COSTO MAS BAJO.1', db.String)
    rentab = db.Column('RENTAB.', db.String)
    venta = db.Column('VENTA', db.String)
    un_18 = db.Column('Unnamed: 18', db.String)
    venta_oferta = db.Column('VENTA OFERTA', db.String)




    @classmethod
    def find_all_products_detail(cls):
        return cls.query.all()