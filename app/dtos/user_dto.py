from dataclasses import dataclass
from app.models.user import User
from copy import deepcopy


@dataclass
class User_dto:
    def __init__(self, User: User):
        self.id = User.user_id
        self.username = User.user_username
        self.first_name = User.user_first_name
        self.last_name = User.user_last_name
        # self.image_file = User.user_image_file
        self.email = User.user_email
        self.role = User.user_role

    def serialize(self):
        dto = deepcopy(self)

        return dto.__dict__
