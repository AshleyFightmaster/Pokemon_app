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
        pokes = db.relationship('Pokemon', backref= 'trainer')

        def __init__(self, username, email, password):
                self.username = username
                self.email = email
                self.password = generate_password_hash(password)

        def save_to_db(self):
            db.session.add(self)
            db.session.commit()

        def catch(self, pokes):
            self.pokes.append(pokes)        
            db.session.commit()

        def check_team(self):
            return len(self.pokes) <= 5  

        def release(self, pokes):
            db.session.delete(pokes)
            db.session.commit()  



class Pokemon(db.Model):
    name = db.Column(db.String(50), primary_key = True, unique = True, nullable=False)
    base_stat_hp =db.Column(db.Integer)
    base_stat_defense = db.Column(db.Integer)
    base_stat_attack = db.Column(db.Integer)
    sprite = db.Column(db.String, nullable=False)
    ability_name = db.Column(db.String)
    base_experience = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, base_stat_hp, base_stat_defense, base_stat_attack, sprite, ability_name, base_experience):
                self.name = name
                self.base_stat_hp = base_stat_hp
                self.base_stat_defense = base_stat_defense
                self.base_stat_attack = base_stat_attack
                self.sprite = sprite
                self.ability_name = ability_name
                self.base_experience = base_experience

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
