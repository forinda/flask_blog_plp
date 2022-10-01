""" Flask application """
from flask import Flask # pylint: disable=import-error
from flask_fontawesome import FontAwesome # pylint: disable=import-error
from .views import base as baseBlueprint
from .config import config


def create_app():
    """Create the application."""
    app = Flask(__name__)
    FontAwesome(app)
    app.config.from_object(config['dev'])

    app.register_blueprint(baseBlueprint)

    return app
