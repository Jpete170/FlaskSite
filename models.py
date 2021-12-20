#from FlaskSite.views import index
from datetime import datetime
from sqlalchemy.sql import expression
import enum

from FlaskSite import db

class genres(enum.Enum):
    sci_fi = 1


class Item(db.Model):
    __tablename__="books"
    ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), index=True)
    Year_Published = db.Column(db.Integer, index=True)
    Author = db.Column(db.String(100), index=True)
    Description = db.Column(db.String(250), index=True)
    Genre = db.Column(db.Enum(genres))

    def __repr__(self):
        return "<Name: {}, ID: {}".format(self.Title, self.ID)