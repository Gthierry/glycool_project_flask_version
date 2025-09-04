from app.models.user import User
from app.dtos.user_dto import User_dto
from app.services.base_service import Base_service
from app.forms.users.user_insert_form import user_insert_form
import bcrypt
from app import db


class User_service(Base_service):
    @staticmethod
    def get_all():
        return [User_dto(u) for u in User.query.all()]

    @staticmethod
    def create(form: user_insert_form):
        salt = bcrypt.gensalt()
        user = User(
            user_first_name=form.first_name.data,
            user_last_name=form.last_name.data,
            user_email=form.email.data,
            user_username=form.username.data,
            user_password=bcrypt.hashpw(
                form.password.data.encode("utf-8"), salt
            ).decode("utf-8"),
            user_role="user",
        )
        db.session.add(user)
        db.session.commit()
        return User_dto(user)
