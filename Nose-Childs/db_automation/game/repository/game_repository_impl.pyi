from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    __gameList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def diceGame(self,diceList):
        return

    def checkWinner(self):
        # 필요한거: sum값 playerA= [1,5]  playerB= [2,2]
        # diceList= [[1,5],[2,2]]
        # sum A  =6
        # sum B = 4
        # if sumA > sum B
        #return
        pass


