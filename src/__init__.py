from flask import Flask
from .views import base as baseBlueprint
from .config import config
from flask_fontawesome import FontAwesome


def create_app():
    app = Flask(__name__)
    FontAwesome(app)
    app.config.from_object(config['dev'])

    app.register_blueprint(baseBlueprint)

    return app
