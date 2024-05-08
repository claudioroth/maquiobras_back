from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

cors = CORS()
db = SQLAlchemy()
api = Api()
