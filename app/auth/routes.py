from flask import Blueprint, render_template, request, redirect, url_for

from app.auth.forms import UserCreationForm 
from app.auth.forms import LoginForm
from app.models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)

            user.save_to_db()

            return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    # if request.method == 'POST':
    #     if form.validate():
    #         username = form.username.data
    #         password = form.password.data
    return render_template('login.html')
