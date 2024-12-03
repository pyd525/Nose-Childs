from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def createName(self):
        pass

    @abstractmethod
    def findAccount(self, requsetAccountId):
        pass