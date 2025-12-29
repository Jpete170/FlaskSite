#from crypt import methods
from flask import Blueprint, render_template #, url_for, redirect
from models import Item, Author

bp = Blueprint('main', __name__)

## General Pages
@bp.route('/', methods=['GET'])
def index():
    #used to get all the books in the database
    items = Item.query.all()
    authors= Author.query.all()
    return render_template('index.html', items=items, auth=authors)

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

## Book Pages
#overall product page
@bp.route('/products', methods=['GET'])
def prodcuts():
    item = Item.query.all()
    return render_template('/products/products.html', item=item)

#specific individual pages for each book category
@bp.route('/products/<genre>', methods=["GET"])
def page_genre(genre):
    item = Item.query.filter_by(Genre=genre)
    title = Item.query.filter_by(Genre=genre).first()
   
    return render_template("products/details.html", item=item, title=title)

#Specific pages for each sub-genre of book, part of the filtering functionality
@bp.route('/products/<genre>/<sub_genre>', methods=['GET'])
def filter(genre, sub_genre):
    item = Item.query.filter_by(Genre=genre, Sub_Genre=sub_genre)
    title = Item.query.filter_by(Sub_Genre=sub_genre).first()
    sub_genre = Item.query.filter_by(Sub_Genre=sub_genre)
    return render_template("products/details.html", subGenre=sub_genre, item=item, title=title)

#individual item page
@bp.route('/products/book/<book_id>', methods=["GET"])
def single_page(book_id):
    item = Item.query.filter_by(id = book_id).first()
    author = Author.query.filter_by(Name=item.Author).first()
    return render_template("products/single.html", item=item, auth=author)

## Author Pages
@bp.route('/authors', methods=['GET'])
def authors():
    authors = Author.query.all()
    #return "Test Page Currently"
    return render_template("authors/authors.html", auth=authors)

#Will need to change <name> into something that is more concise for a html link
@bp.route('/authors/<name>', methods=['GET'])
def authPage(name):
    author = Author.query.filter_by(Name=name).first()
    items = Item.query.filter_by(Author=name)
    
    return render_template('authors/authorBio.html', auth=author, items=items)