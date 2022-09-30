from flask import Blueprint,render_template

base = Blueprint('base',__name__)


@base.route("/")
def index():
	context = [
		{

		}
	]
	return render_template('index.html',context=context)
