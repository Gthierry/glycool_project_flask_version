from app import db
from sqlalchemy import Identity


class Recipes(db.Model):
    __tablename__ = "recipes"
