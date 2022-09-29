from flask import Flask
from .view import base as baseBlueprint


def create_app():
	app = Flask(__name__)
	
	app.register_blueprint(baseBlueprint)
	return app
	
	
