from flask import Flask
from .view import base as baseBlueprint
from .config import config


def create_app():
	app = Flask(__name__)
	app.config.from_object(config['dev'])
	
	app.register_blueprint(baseBlueprint)
	return app
	
	
