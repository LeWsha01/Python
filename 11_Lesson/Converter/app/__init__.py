__version__ = '1.0'
from flask import Flask
import http
import os

import flask
import flask_sqlalchemy
import flask_marshmallow
import flask_wtf
import wtforms
from wtforms import validators

app = Flask(__name__)
app.config.from_object('config')


from app import routes


