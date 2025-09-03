# models.py
# Import the db instance
from app import db


# Define the User model
class Message(db.Model):
    # Define table name
    __tablename__ = "messages"
    message_id = db.Column(db.Integer, primary_key=True)
    message_subject = db.Column(db.String(100), unique=True, nullable=False)
    message_body = db.Column(db.String(), nullable=True)
