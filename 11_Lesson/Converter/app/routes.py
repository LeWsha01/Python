import http
import os

import flask
import flask_sqlalchemy
import flask_marshmallow
import flask_wtf
import wtforms
from wtforms import validators
from app import app

app.config['SECRET_KEY'] = 'random_string_for_safe'

class CreateForm(flask_wtf.FlaskForm):
    pass


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return flask.render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return flask.render_template("login.html")

