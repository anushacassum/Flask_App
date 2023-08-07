#include "Python.h"

from flask import Flask

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/anusha/Documents/Flaskapp/Flask_App/postgresdatabase.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nassa2580@localhost/bookstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False