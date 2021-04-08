# Flask imports

from flask import flash
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

# tests
import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar cafe', 'cambiar solicitud de compra', 'entregar video a productor']



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

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

@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    #login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username
    } 
    return render_template('hello.html', **context)
