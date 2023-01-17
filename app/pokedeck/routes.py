from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.pokedeck.forms import Pokesearchform
from flask_login import current_user, login_required
import requests
from app.models import Pokemon, User
import time

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
            if response.ok == True:
                pokemon_info ={
                    'name' : response.json()['forms'][0]['name'],
                    'ability_name' : response.json()['abilities'][0]['ability']['name'],
                    "base_experience": response.json()['base_experience'],
                    "sprite" : response.json()['sprites']['other']['dream_world']['front_default'],
                    "attack_base_stat" : response.json()['stats'][1]['base_stat'],
                    "hp_base_stat": response.json()['stats'][0]['base_stat'],
                    "defense_base_stat" : response.json()['stats'][2]['base_stat']
                } 
            else:
                flash("That Pokemon does not exist. Please check spelling!", 'danger')
    return render_template('pokemon.html', form=form, pokemon_info=pokemon_info)

@poke.route('/catch_pokemon/<pokemon_name>')
def catch_pokemon(pokemon_name):
    form = Pokesearchform()
    poke = Pokemon.query.get(pokemon_name)
    print(poke)
    if poke:
        flash("Sorry, taken!", 'danger')
        return render_template('pokemon.html', form=form)
    elif not current_user.check_team():
        print('checking')
        flash('Team is full! Delete a pokemon.')
        return redirect(url_for('pokemon_team.view_pokedeck'))
    else:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        pokemon_info ={
            'name' : response.json()['forms'][0]['name'],
            'ability_name' : response.json()['abilities'][0]['ability']['name'],
            "base_experience": response.json()['base_experience'],
            "sprite" : response.json()['sprites']['other']['dream_world']['front_default'],
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

@poke.route('/view_pokedeck', methods=['GET', 'POST'])
@login_required
def view_pokedeck():
    user_id = current_user.id
    pokes = Pokemon.query.filter_by(user_id=user_id).all()
    if pokes:
        return render_template('pokedeck.html', pokes=pokes)
    else:
        flash("Let's build your deck!", 'info')
        return redirect(url_for('pokemon_team.pokemon'))

@poke.route('/view_pokedeck/release/<pokemon_name>', methods=['GET', 'POST'])
@login_required
def release_pokemon(pokemon_name):
    poke = Pokemon.query.get(pokemon_name)
    if current_user.id == poke.user_id:
        current_user.release(poke)
        flash('Pokemon has been released!')
        return redirect(url_for('pokemon_team.view_pokedeck'))
    else:
        flash('Error!', 'danger')
        return redirect(url_for('pokemon_team.view_pokedeck'))

@poke.route('/battle/<int:user_id>', methods=['GET', 'POST'])
@login_required
def battle(user_id):
    current = current_user.id
    my_pokes = Pokemon.query.filter_by(user_id=current).all()
    pokes = Pokemon.query.filter_by(user_id=user_id).all()
    attack = 0
    my_attack = 0
    for i in pokes:
        x = i.base_stat_attack
        attack += x
    for i in my_pokes:
        y = i.base_stat_attack
        my_attack += y
    # if my_attack > attack:
    #     flash('Winner', 'success')
    #     return redirect(url_for('pokemon_team.trainers'))
    # else:
    #     flash('You Lost!', 'danger')
    #     return redirect(url_for('pokemon_team.trainers'))

    return render_template('battle.html', my_attack=my_attack, attack=attack)

# url="<https://img.favpng.com/5/3/24/ash-ketchum-pokxe9mon-go-pokxe9mon-ruby-and-sapphire-pikachu-misty-png-favpng-yk4QpKB0R2FnEi4aSayacxA6C_t.jpg>"
# url1="<https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFb7omPV8-aeY9SYCw3bfbCjLNXMHPBlzwjQ&usqp=CAU>"
# url2="<https://e7.pngegg.com/pngimages/528/570/png-clipart-pokemon-sun-and-moon-pokemon-x-and-y-pokemon-trainer-the-pokemon-company-pokemon-trainer-game-human.png>"
# url3="<https://e7.pngegg.com/pngimages/444/617/png-clipart-pokemon-black-2-and-white-2-pokemon-black-white-pokemon-omega-ruby-and-alpha-sapphire-pokemon-crystal-pokemon-trainer-others-game-human-thumbnail.png>"
# urls=[url, url1, url2, url3]


@poke.route('/trainers')
@login_required
def trainers():
    trainers = User.query.all()


    return render_template('trainers.html', trainers=trainers)