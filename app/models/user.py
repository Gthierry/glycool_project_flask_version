# models.py
# Import the db instance
from app import db
from sqlalchemy import Identity


# Define the User model
class User(db.Model):
    # Define table name
    __tablename__ = "users"
    user_id = db.Column(db.Integer, Identity(), primary_key=True)
    user_username = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    user_first_name = db.Column(db.String(50), nullable=True)
    user_last_name = db.Column(db.String(50), nullable=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_birthdate = db.Column(db.DateTime, nullable=True)
    user_city = db.Column(db.String(100), nullable=True)
    user_avatar = db.Column(db.String(30), nullable=False, default="default.jpg")
    user_role = db.Column(db.String(20), nullable=True, default="user")
    user_bio = db.Column(db.Text, nullable=True)
    user_active = db.Column(db.Boolean, default=True)
    user_created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_last_login = db.Column(db.DateTime, nullable=True)
    messages = db.relationship("Message", back_populates="user")
