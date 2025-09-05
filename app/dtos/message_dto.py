from dataclasses import dataclass
from copy import deepcopy
from app.models.message import Message
from app.dtos.abstract_dto import Abstract_dto

@dataclass
class Message_dto(Abstract_dto):
    def __init__(self, Message: Message):
        self.id = Message.message_id
        self.subject = Message.message_subject
        self.body = Message.message_body
        self.created_at = Message.message_created_at
        self.user_id = Message.user_id
        self.mesage_id = Message.message_id

    def serialize(self):
        dto = deepcopy(self)
        return dto.__dict__
: