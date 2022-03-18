#from crypt import methods
from flask import Blueprint, render_template #, url_for, redirect
from .models import Item, Author

bp = Blueprint('main', __name__)

## General Pages
@bp.route('/', methods=['GET'])
def index():
    #used to get the different categories of books available
    #category = Item.query.all()
    return render_template('index.html')

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

## Book Pages
#overall product page
@bp.route('/products', methods=['GET'])
def prodcuts():
    item = Item.query.all()
    #return "<h1>Placeholder Products Page</h1>"
    return render_template('/products/products.html', item=item)

#specific individual pages for each item / book
@bp.route('/products/<genre>', methods=["GET"])
def sci_fi(genre):
    item = Item.query.filter_by(genre=genre)
    return "<h1>Page for Science Fiction Novels</h1>"
    #return render_template("products/details", item=item)

## Author Pages
@bp.route('/authors', methods=['GET'])
def authors():
    #authors = Author.query.all()
    #return "Test Page Currently"
    return render_template("authors/authors.html")

#Will need to change <name> into something that is more concise for a html link
@bp.route('/authors/<name>', methods=['GET'])
def authPage(name):
    #author = Author.query.filter_by(name=name)
    #return "Test Page currently"
    return render_template('authors/authorBio.html')#, auth=author)