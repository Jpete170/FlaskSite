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
    Horror = 2

class Item(db.Model):
    __tablename__="books"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), index=True)
    Year_Published = db.Column(db.Integer, index=True)
    Author = db.Column(db.String(100), index=True)
    Description = db.Column(db.String(250), index=True)
    Genre = db.Column(db.String(100), index=True)
    Sub_Genre = db.Column(db.String(100), index=True)
    bookURL = db.Column(db.String(100), index=True)
    bookIMG = db.Column(db.String(100), index=True)
    def __repr__(self):
        return "<Name: {}, ID: {}".format(self.title, self.id)

#Future db model
class Author(db.Model):
    __tablename__="Author"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Name = db.Column(db.String(100), index=True)
    Birthdate = db.Column(db.String(100), index=True)
    Deathdate = db.Column(db.String(100), index=True)
    Bio = db.Column(db.String(500), index=True)

