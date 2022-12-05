from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import TeamCreationform
from app.models import Team

poketeam = Blueprint('pokemon_team', __name__, template_folder='poketeam_templates')



@poketeam.route('/team/create', methods=['GET', 'POST'])
@login_required
def create_team():
    form = TeamCreationform()
    if request.method == 'POST':
        if form.validate():
            team_name = form.team_name.data
            
            # instantiate Team from models
            team = Team(team_name, current_user.id)
            


            # add team to database
            team.save_to_db()

            return redirect(url_for('pokemon_team.view_team'))

    return render_template('team_create.html', form=form)

@poketeam.route('/view_team')
@login_required
def view_team():
    teams = Team.query.all()
    return render_template('team_home.html', teams=teams)


# Dynamic Routes
@poketeam.route('/view_team/<int:team_id>')
def view_single_team(team_id):
    team = Team.query.get(team_id)
    if team:
        return render_template('single_team.html', team=team)
    else:
        return redirect(url_for('pokemon_team.view_team'))

@poketeam.route('/view_team/update/<int:team_id>', methods=['GET', 'POST'])
@login_required
def update_team(team_id):
    form = TeamCreationform()
    team = Team.query.get(team_id)
    if current_user.id == team.user_id:
        if request.method == 'POST':
            if form.validate():
                team_name = form.team_name.data
            
                #update team attributes on db
                team.team_name = team_name
                
                # commit team changes to db
                team.update_db()

                return redirect(url_for('pokemon_team.view_team'))
    else:
        flash("You are not aloud to be here.", 'danger')
        return redirect(url_for('pokemon_team.view_team'))
    return render_template('update_team.html', form=form, team=team)

@poketeam.route('/view_team/delete/<int:team_id>')
@login_required
def delete_team(team_id):
    team = Team.query.get(team_id)
    if team:
        team.delete_from_db()
    return redirect(url_for('pokemon_team.view_team'))