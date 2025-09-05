from abc import ABC, abstractmethod


class Abstract_dto(ABC):
    @abstractmethod
    def serialize(self):
        pass
