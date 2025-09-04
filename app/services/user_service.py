from app import db
from app.models.user import User
from app.dtos.user_dto import User_dto


class User_service:
    @staticmethod
    def get_all_users():
        return [User_dto(u) for u in User.query.all()]

    @staticmethod
    def create_user():
        pass
