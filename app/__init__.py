from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object('config') 
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1224@localhost/flask-db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.model import user_model

from app.controller import user_controller