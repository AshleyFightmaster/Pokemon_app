from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.pokedeck.forms import Pokesearchform
from flask_login import current_user, login_required
import requests
from app.models import Pokemon

poke = Blueprint('pokemon_team', __name__, template_folder='poketeam_templates')

@poke.route('/view_deck')
@login_required
def view_deck():
    return render_template('pokedeck.html')

@poke.route('/pokemon', methods=['GET', 'POST'])
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
            # name = pokemon_info['name']
            # ability_name = pokemon_info['ability_name']
            # base_experience = pokemon_info['base_experience']
            # sprite = pokemon_info['sprite']
            # base_stat_attack = pokemon_info['attack_base_stat']
            # base_stat_hp = pokemon_info['hp_base_stat']
            # base_stat_defense = pokemon_info['defense_base_stat']
            
            # pokemon = Pokemon(name, base_stat_hp, base_stat_defense, base_stat_attack, sprite, ability_name, base_experience)
            # poke = Pokemon.query.get(name)
            # team = Team.query.all()
            # if poke:
            #     flash("That pokemon has already been caught!")
            # elif current_user.id == team[user_id]:
            #     if team.pokemon_name == 5:
            #         flash("Your pokemon deck is full. Delete another pokemon to catch more.")
            #         return redirect(url_for('pokemon_team.view_team'))
            # elif poke < 1:
            #     flash(f'Successfully caught {poke.title()}!', 'succuss')
            #     pokemon.save_to_db()
            #     return redirect(url_for('app.pokemon'))
            # else:
            #     flash('Check spelling.', 'warning')

            # return render_template('pokemon.html')
            

    return render_template('pokemon.html', form=form, pokemon_info=pokemon_info)

@poke.route('/catch_pokemon/<pokemon_name>')
def catch_pokemon(pokemon_name):
    poke = Pokemon.query.get(pokemon_name)
    if poke:
        flash("Sorry, taken!", 'danger')
        return render_template('pokemon.html')
    elif not current_user.check_team:
        flash('Team is full! Delete a pokemon.')
        # return render_template('single_team')
    else:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
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
        current_user.catch(pokemon)
        flash("Success!", 'info')
        return redirect(url_for('pokemon_team.pokemon'))

    return render_template('pokemon.html')

@poke.route('/view_pokedeck/<pokemon_name>')
def view_pokedeck(pokemon_name):
    poke = Pokemon.query.get(pokemon_name)
    if current_user.id == poke.user_id:
        return render_template('pokedeck.html', poke=poke) 
