from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')