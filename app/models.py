from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

# create models based off our ERD
class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), nullable=False, unique=True)
        email = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(250), nullable=False)
        team = db.relationship('Team', backref='Trainer', lazy=True)

        def __init__(self, username, email, password):
                self.username = username
                self.email = email
                self.password = generate_password_hash(password)

        def save_to_db(self):
            db.session.add(self)
            db.session.commit()


class Team(db.Model):
        id = db.Column(db.Integer, primary_key=True)  
        team_name = db.Column(db.String(50), nullable=False, unique=True)
        date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        
        
        def __init__(self, team_name, user_id):
                    self.team_name = team_name
                    self.user_id = user_id
                    

        def save_to_db(self):
                db.session.add(self)
                db.session.commit()

        def update_db(self):
                db.session.commit()

        def delete_from_db(self):
                db.session.delete(self)
                db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable=False)
    base_stat_hp =db.Column(db.Integer, nullable=False)
    base_stat_defense = db.Column(db.Integer, nullable=False)
    base_stat_attack = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.String, nullable=False)
    abilities = db.Column(db.String, nullable=False)
    # team = db.relationship('Team', backref='pokemon', lazy=True)

    def __init__(self, name, base_stat_hp, base_stat_defense, base_stat_attack, sprite, abilities):
        self.name = name
        self.base_stat_hp = base_stat_hp
        self.base_stat_defense = base_stat_defense
        self.base_stat_attack = base_stat_attack
        self.sprite = sprite
        self.abilities = abilities
