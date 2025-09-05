from app import db
from sqlalchemy import Identity


class UserMessage(db.Model):
    __tablename__ = "user_messages"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    message_id = db.Column(
        db.Integer, db.ForeignKey("messages.message_id"), nullable=False
    )
    user = db.relationship("User", back_populates="user_messages")
    message = db.relationship("Message", back_populates="user_messages")
