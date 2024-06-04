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
    def find_all_active_users(cls):
        return cls.query.filter(UserModel.is_active).all()

    @classmethod
    def find_users_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_users_by_name(cls, user):
        return cls.query.filter_by(user=user).first()


class ControlModel(db.Model, BaseSerializer):
    __tablename__ = 'control'
    __bind_key__ = 'maquiobrasdb'

    fields = ['id', 'id_user', 'id_prod', 'retiro', 'fecha', 'local']

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    id_prod = db.Column(db.Integer)
    retiro = db.Column(db.Integer)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    local = db.Column(db.String)

    # Deposito, Local Galicia, Local Juan B Justo

    @classmethod
    def find_all_control(cls):
        #return cls.query.all()
        return cls.query.order_by(ControlModel.id.desc())
    


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

    fields = ['index', 'nro', 'descripcion', 'importe_sin_iva', 'iva_21', 'iva_10', 'oferta_sin_iva',
              'aumento', 'ultimo_modif', 'oferta_costo', 'costo_mas_bajo', 'rentabilidad', 'stock']


    index = db.Column('index', db.Integer, primary_key=True, autoincrement=True)
    nro = db.Column('N° PROV.', db.String)
    descripcion = db.Column('DESCRIPCION', db.String)
    importe_sin_iva = db.Column('IMPORTE S/IVA', db.String)
    iva_21 = db.Column('C/IVA 21%', db.String)
    iva_10 = db.Column('C/IVA 10.5%', db.String)
    oferta_sin_iva = db.Column('OFERTA SIN IVA', db.String)
    aumento = db.Column('AUMENTO', db.String)
    ultimo_modif = db.Column('ULT.MODIF.', db.String)
    oferta_costo = db.Column('OFERTA COSTO', db.String)
    costo_mas_bajo = db.Column('COSTO MAS BAJO', db.String)
    rentabilidad = db.Column('RENTAB.', db.String)
    stock = db.Column('STOCK', db.Integer)




    @classmethod
    def find_all_products_detail(cls):
        return cls.query.all()
    
    @classmethod
    def find_all_productos_with_stock(cls):
        return cls.query.filter(ProductsDetailModel.stock != None, ProductsDetailModel.stock > 0).all()
    
    @classmethod
    def find_products_by_index(cls, index):
        return cls.query.filter_by(index=index).first()
    