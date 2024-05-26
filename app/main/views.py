from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def index():
    return render_template('main.html')

@main.route('/boveda')
@login_required
def boveda():
    return render_template('boveda.html')