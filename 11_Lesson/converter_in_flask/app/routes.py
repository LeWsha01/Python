import flask
from app import app, uri
from flask import render_template, flash, redirect, get_template_attribute
from app.forms import LoginForm, RegisterForm, CurrencyForm
from app.models import User, session
from app.calculate import calculation
from app.req import get_data_from_uri


CURRENCY = get_data_from_uri(uri)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if session.query(User.login).filter(User.login == form.login.data).count():
            password_user = [instance.password for instance in session.query(User.password)
                             .filter_by(login=form.login.data)]
            if form.password.data in password_user:
                id_user = session.query(User.id).filter(User.login == form.login.data).first()
                user = form.login.data
                return redirect(flask.url_for('home', id_user=id_user, user=user))  # home(id_user, user)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if session.query(User.login).filter(User.login == form.login.data).count() == 0:
            session.add(User(form.name.data, form.surname.data, form.login.data, form.password.data))
            session.commit()
            return redirect(flask.url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/home', methods=['GET', 'POST'])
def home(id_user, user):
    form = CurrencyForm()
    if form.validate_on_submit():
        first_cur = str(form.first_cur.data).upper()
        money_cur = int(form.how_much.data)
        second_cur = str(form.second_cur.data).upper()
        return redirect(flask.url_for('result', first=first_cur, money=money_cur, second=second_cur, id_user=id_user))
    return render_template('home.html', title='Home', form=form, user=user, currency=CURRENCY)


@app.route('/result', methods=['GET', 'POST'])
def result(first, money, second, id_user):
    result_of_currency = calculation(first, money, second, CURRENCY, id_user)
    return render_template('result.html', title='Result',
                           first=first,
                           second=second,
                           money=money,
                           result_of_currency=result_of_currency)
