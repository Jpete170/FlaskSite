from flask_wtf import FlaskForm
from wtforms.fields import SelectField

from . import db

class Jumbo(FlaskForm):
    Genre = SelectField(choices=[("sci-fi", "Sci-Fi")])
