"""Base views for the application."""
from flask import Blueprint, render_template

base = Blueprint('base', __name__)


@base.route("/")
def index():
    """Render the index page."""
    services = [
        {
            "name": ""
        }
    ]
    return render_template('index.html', context={"services": services})
