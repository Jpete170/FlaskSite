from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@bp.route('/products', methods=['GET'])
def prodcuts():
    return "<h1>Placeholder Products Page</h1>"

@bp.route('/products/sci-fi', methods=["GET"])
def scifi():
    return "<h1>Page for Science Fiction Novels</h1>"