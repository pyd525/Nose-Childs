

from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def create(self):
        pass
