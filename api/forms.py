from flask_wtf import FlaskForm
from wtforms.fields import SelectField


class Jumbo(FlaskForm):
    Genre = SelectField(choices=[("fiction", "Fiction"), ("romance", "Romance"), ("comedy", "Comedy"), ("essays", "Essays")])

#Possibly implement different sub-genre selection fields depending on the main genre selected
class FictionSubGenre(FlaskForm):
    Sub_Genre= SelectField(choices=[('science-fiction', 'Science Fiction'), ('psychological_fiction', "Psychological Fiction"), ('mystery', 'Mystery'), ('historical', 'Historical'), ('supernatural', 'Supernatural'), ('horror', 'Horror'), ('english-fiction', 'English Fiction'), ('adventure', 'Adventure')])