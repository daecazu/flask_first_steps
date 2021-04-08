from app.forms import LoginForm
from . import auth
from flask import render_template
from flask import session
from flask import url_for
from flask import redirect
from flask import flash


@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado')
        return redirect(url_for('index'))
    return render_template('login.html', **context)
