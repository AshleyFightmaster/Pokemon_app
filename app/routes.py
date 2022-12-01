from app import app
from flask import render_template, request
from app.forms import Pokesearchform


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = Pokesearchform()
    if request.method == 'POST':
       if form.validate():
            search = form.search.data
    return render_template('pokemon.html', form=form)