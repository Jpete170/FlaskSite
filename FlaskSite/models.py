#from FlaskSite.views import index
from datetime import datetime
from sqlalchemy.sql import expression
import enum

from . import db
#Genres will be used as part of a future functionality
class genres(enum.Enum):
    Science_Fiction = 1


class Item(db.Model):
    __tablename__="books"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), index=True)
    Year_Published = db.Column(db.Integer, index=True)
    Author = db.Column(db.String(100), index=True)
    Description = db.Column(db.String(250), index=True)
    Genre = db.Column(db.Enum(genres))

    def __repr__(self):
        return "<Name: {}, ID: {}".format(self.title, self.id)
