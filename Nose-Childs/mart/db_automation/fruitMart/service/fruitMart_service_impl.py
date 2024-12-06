from abc import ABC

from fruitMart.repository.fruitMart_repository_impl import FruitMartRepositoryImpl
from fruitMart.service.fruitMart_service import FruitMartService
#from game.repository.game_repository_impl import GameRepositoryImpl
from customer.repository.customer_repository_impl import CustomerRepositoryImpl


class FruitMartServiceImpl(FruitMartService, ABC):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__fruitMartRepository = FruitMartRepositoryImpl.getInstance()
            #cls.__instance.__gameRepository = OrderRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = CustomerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def stockFruit(self):
        return self.__fruitMartRepository.create()

    def findFruitId(self, requestFruitMartId):
        return self.__fruitMartRepository.findById(requestFruitMartId)

    def findEveryFruit(self):
        return self.__fruitMartRepository.findAll()
