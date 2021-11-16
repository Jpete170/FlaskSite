#import flask and other packages
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
from flask_sqlalchemy import *

db = SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.debug=True

    boostrap=Bootstrap(app)
   # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    #view stuff
    from . import views
    app.register_blueprint(views.bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    return app