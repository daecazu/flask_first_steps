# Flask imports
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# wtforms imports
from wtforms.fields import StringField
from wtforms.fields import PasswordField 
from wtforms.fields import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'Super SECRETO'

todos = ['Comprar cafe', 'cambiar solicitud de compra', 'entregar video a productor']

class LoginForm(FlaskForm):
    username = StringField(
        'Nombre de usuario',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form

    } 
    return render_template('hello.html', **context)
