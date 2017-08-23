# coding: utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:batman123@127.0.0.1:3306/movie_flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '71fe86deea00463b8523a4eff0d21bc4'

app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")

