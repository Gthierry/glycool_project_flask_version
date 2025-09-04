from abc import ABC, abstractmethod


class Base_service(ABC):
    @abstractmethod
    def insert(self, form):
        pass
