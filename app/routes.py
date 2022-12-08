from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import Pokesearchform
import requests
from flask_login import login_required, current_user

from app.models import Pokemon, Team, User


@app.route("/")
def home():
    users = User.query.all()
    return render_template('home.html', users=users)


@app.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pokemon():
    form = Pokesearchform()
    pokemon_info={}
    if request.method == 'POST':
       if form.validate():
            search = form.search.data
            url = f'https://pokeapi.co/api/v2/pokemon/{search}'
            response = requests.get(url)
            
            pokemon_info ={
                        'name' : response.json()['forms'][0]['name'],
                        'ability_name' : response.json()['abilities'][0]['ability']['name'],
                        "base_experience": response.json()['base_experience'],
                        "sprite" : response.json()['sprites']['front_default'],
                        "attack_base_stat" : response.json()['stats'][1]['base_stat'],
                        "hp_base_stat": response.json()['stats'][0]['base_stat'],
                        "defense_base_stat" : response.json()['stats'][2]['base_stat']
                }
            
            name = pokemon_info['name']
            ability_name = pokemon_info['ability_name']
            base_experience = pokemon_info['base_experience']
            sprite = pokemon_info['sprite']
            base_stat_attack = pokemon_info['attack_base_stat']
            base_stat_hp = pokemon_info['hp_base_stat']
            base_stat_defense = pokemon_info['defense_base_stat']
            
            pokemon = Pokemon(name, base_stat_hp, base_stat_defense, base_stat_attack, sprite, ability_name, base_experience)
            pokemon.save_to_db()
        
            # response.raise_for_status()
            # if response.status_code != 204:
            #     return response.json()
            # elif response.status_code == 200
            # return redirect(url_for('pokemon2'))
            
    return render_template('pokemon.html', form=form, pokemon_info=pokemon_info)


@app.route('/catch/<int:pokemon_id>')
@login_required
def catch(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    if pokemon:
        catch(pokemon)
        flash(f'Successfully caught {pokemon.name.title()}!', 'succuss')
    else:
        flash('Check spelling.', 'warning')
    
    return redirect(url_for('poketeam.view_team'))
    
    