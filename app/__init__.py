from flask import Flask
from config import Config
from flask_migrate import Migrate

from .models import db, User
from flask_login import LoginManager

from .auth.routes import auth
from .pokedeck.routes import poke


app = Flask(__name__)


login_manager=LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config.from_object(Config)


# register blueprints
app.register_blueprint(auth)
app.register_blueprint(poke)



# initialize our database to work with our app
login_manager.init_app(app)



# initialize our database to work with our app
db.init_app(app)
migrate = Migrate(app, db)
login_manager.login_view = 'auth.login'


from . import routes
from . import models






