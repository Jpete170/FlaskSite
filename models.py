from . import db
from datetime import datetime
from sqlalchemy.sql import expression
import enum

class genres(enum.Enum):
    sci_fi = 1


class Item(db.Model):
    __tablename__="item"