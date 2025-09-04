from app.models.user import User
from app.dtos.user_dto import User_dto
from app.services.base_service import Base_service


class User_service(Base_service):
    @staticmethod
    def get_all():
        return [User_dto(u) for u in User.query.all()]

    @staticmethod
    def create():
        pass
