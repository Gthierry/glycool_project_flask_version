from dataclasses import dataclass
from app.models.user import User
from copy import deepcopy
from app.dtos.abstract_dto import Abstract_dto


@dataclass
class User_dto(Abstract_dto):
    def __init__(self, User: User):
        self.id = User.user_id
        self.username = User.user_username
        self.password = User.user_password
        self.birthdate = User.user_birthdate
        self.city = User.user_city
        self.avatar = User.user_avatar
        self.bio = User.user_bio
        self.active = User.user_active
        self.created_at = User.user_created_at
        self.last_login = User.user_last_login
        self.first_name = User.user_first_name
        self.last_name = User.user_last_name
        # self.image_file = User.user_image_file
        self.email = User.user_email
        self.role = User.user_role

    def serialize(self):
        dto = deepcopy(self)

        return dto.__dict__
