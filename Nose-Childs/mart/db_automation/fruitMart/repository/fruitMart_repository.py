from abc import ABC, abstractmethod


class FruitMartRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    #@abstractmethod
    #def findByGameId(self, gameId):
     #   pass

    #@abstractmethod
    #def findByGameAndPlayer(self, game, player):
    #    pass

    @abstractmethod
    def findAll(self):
        pass
