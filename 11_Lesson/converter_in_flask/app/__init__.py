from flask import Flask
import flask_sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/currency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = flask_sqlalchemy.SQLAlchemy(app)

uri = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

from app import routes
