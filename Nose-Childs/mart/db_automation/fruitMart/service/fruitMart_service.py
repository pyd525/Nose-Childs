from abc import ABC, abstractmethod


class FruitMartService(ABC):

    @abstractmethod
    def stockFruit(self):
        pass

    @abstractmethod
    def findFruitId(self, requestFruitMartId):
        pass

    @abstractmethod
    def findEveryFruit(self):
        pass
