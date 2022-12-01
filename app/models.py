from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# create models based off our ERD
class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), nullable=False, unique=True)
        email = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(250), nullable=False)
        pokemon = db.relationship('Pokemon', backref='Owner', lazy=True)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable=False)
    base_stat_for_hp =db.Column(db.Integer, nullable=False)
    base_stat_for_defense = db.Column(db.Integer, nullable=False)
    base_stat_for_attack = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.String, nullable=False)
    abilities = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)