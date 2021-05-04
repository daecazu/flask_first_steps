# Flask imports

from flask import flash
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
# firestore
from app.firestore_service import get_users
from app.firestore_service import get_todos
from app.firestore_service import put_todo
from flask_login import login_required
from flask_login import current_user

# tests
import unittest

from app import create_app
from app.forms import TodoForm

app = create_app()





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

@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form
    } 
    if todo_form.validate_on_submit():
        put_todo(
            user_id=username,
            description=todo_form.description.data 
        )
        flash('tarea creada')
        return redirect(url_for('hello'))
    return render_template('hello.html', **context)
