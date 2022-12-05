from app import app
from flask import render_template, request, redirect, url_for
from app.forms import Pokesearchform
import requests

from app.models import Team


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/pokemon', methods=['GET', 'POST'])

def pokemon():
    form = Pokesearchform()
    if request.method == 'POST':
       if form.validate():
            search = form.search.data
            url = f'https://pokeapi.co/api/v2/pokemon/{search}'
            response = requests.get(url)
            pokemon_info ={
                        'name' : response.json()['forms'][0]['name'],
                        'ability_name' : response.json()['abilities'][0]['ability']['name'],
                        "base_experience ": response.json()['base_experience'],
                        "sprite" : response.json()['sprites']['front_default'],
                        "attack_base_stat" : response.json()['stats'][1]['base_stat'],
                        "hp_base_stat ": response.json()['stats'][0]['base_stat'],
                        "defense_base_stat" : response.json()['stats'][2]['base_stat']
                }
            print(pokemon_info) 

            
            # response.raise_for_status()
            # if response.status_code != 204:
            #     return response.json()
            # elif response.status_code == 200
            # return redirect(url_for('pokemon2'))
            
    return render_template('pokemon.html', form=form, pokemon_info=pokemon_info)



@app.route('/pokemon2')
def pokemon2():
    # name = response.json()['forms'][0]['name']
    # ability_name = response.json()['abilities'][0]['ability']['name']
    # base_experience = response.json()['base_experience']
    # sprite = response.json()['sprites']['front_default']
    # attack_base_stat = response.json()['stats'][1]['base_stat']
    # hp_base_stat = response.json()['stats'][0]['base_stat']
    # defense_base_stat = response.json()['stats'][2]['base_stat']

    return render_template('pokemon2.html')