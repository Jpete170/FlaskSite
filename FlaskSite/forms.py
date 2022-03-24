from flask_wtf import FlaskForm
from wtforms.fields import SelectField

from . import db

class Jumbo(FlaskForm):
    Genre = SelectField(choices=[("fiction", "Fiction"), ("romance", "Romance"), ("comedy", "Comedy"), ("essays", "Essays")])

#Possibly implement different sub-genre selection fields depending on the main genre selected
class FictionSubGenre(FlaskForm):
    Sub_Genre= SelectField(choices=[])