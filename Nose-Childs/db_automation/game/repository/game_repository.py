from abc import ABC, abstractmethod


class GameRepository(ABC):

    @abstractmethod
    def diceGame(self, diceList):  # sum
        pass

    @abstractmethod
    def checkWinner(self):
        pass
