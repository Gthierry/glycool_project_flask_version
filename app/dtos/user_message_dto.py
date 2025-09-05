from dataclasses import dataclass
from app.models.user_message import User_message
from copy import deepcopy
from app.dtos.abstract_dto import Abstract_dto


@dataclass
class User_message(Abstract_dto):
    def __init__(self, User_message: User_message):
        self.user_id = User_message.user_id
        self.message_id = User_message.message_id

    def serialize(self):
        dto = deepcopy(self)
        return dto.__dict__
