from flask import Blueprint, render_template, request

from app.auth.forms import UserCreationForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form - UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

    return render_template('signup.html', form=form)

