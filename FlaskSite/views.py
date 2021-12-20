from flask import Blueprint, render_template, url_for, redirect
from models import Item

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

#overall product page
@bp.route('/products', methods=['GET'])
def prodcuts():
    #return "<h1>Placeholder Products Page</h1>"
    return render_template('/products/products.html')

@bp.route('/products/<genre>', methods=["GET"])
def sci_fi(genre):
    item = Item.query.filter_by(genre=genre)
    return "<h1>Page for Science Fiction Novels</h1>"
    #return render_template("products/details", item=item)