# models.py
# Import the db instance
from app import db


# Define the User model
class User(db.Model):
    # Define table name
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(50), unique=True, nullable=False)
    user_first_name = db.Column(db.String(50), nullable=True)
    user_last_name = db.Column(db.String(50), nullable=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    # user_image_file = db.Column(db.String(30), nullable=False, default="default.jpg")
    is_active = db.Column(db.Boolean, default=True)
