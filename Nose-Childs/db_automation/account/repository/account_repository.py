from abc import ABC, abstractmethod

class AccountRepository(ABC):
    #인터페이스
    @abstractmethod
    def __processUserInput(self):
        pass

    @abstractmethod
    def createName(self):
        pass

    @abstractmethod
    def findById(self, id):
        pass


