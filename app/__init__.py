from flask import Flask
from config import Config
app = Flask(__name__)

app.config.from_object(Config)

from . import routes
from .auth.routes import auth

app.register_blueprint(auth)