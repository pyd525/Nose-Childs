from abc import ABC, abstractmethod

class DiceService(ABC):

    @abstractmethod
    def getDiceResult(self):
        pass

    @abstractmethod
    def findDice(self, requestDiceId):
        pass
