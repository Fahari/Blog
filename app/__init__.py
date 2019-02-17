from flask import Flask
# from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(DevConfig)

    # Initializing flask extensions
    bootstrap.init_app(app)

    return app
