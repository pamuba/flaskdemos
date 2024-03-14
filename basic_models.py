import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc

# basedir only if ur using SQLLite db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://rootuser:pamuba@24@MLBSRL1-106854/test'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://MLBSRL1-106854/test?driver=SQL Server Native Client 11.0?trusted_connection=yes?UID" \
#                               "=rootuser?PWD=pamuba"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://rootuser:pamuba@MLBSRL1-106854/test?driver=SQL+Server"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# the following code should produce the SQL Lite database
db = SQLAlchemy(app)

###################################################

class Puppy(db.Model):
    #manual way of specifying a table name
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"

    





