#from FlaskSite.views import index
from datetime import datetime
from sqlalchemy.sql import expression
import enum

from . import db
#Genres will be used as part of a future functionality
class genres(enum.Enum):
    Science_Fiction = 1
    Romance = 2
    Fiction = 3
    Drama = 4

#not yet implemented in the database
#implemented here for future implementation reference
class sub_genres(enum.Enum):
    Marriage_Drama= 1


class Item(db.Model):
    __tablename__="books"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), index=True)
    Year_Published = db.Column(db.Integer, index=True)
    Author = db.Column(db.String(100), index=True)
    Description = db.Column(db.String(250), index=True)
    Genre = db.Column(db.Enum(genres))
    bookURL = db.column(db.String(100), index=True)
    bookIMG = db.column(db.String(100), index=True)
    def __repr__(self):
        return "<Name: {}, ID: {}".format(self.title, self.id)

#Future db model
#class Author(db.Model):
