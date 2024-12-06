from django.forms import model_to_dict
from fruitMart.repository.fruitMart_repository import FruitMartRepository
from fruitMart.entity.fruitMart import FruitMart


class FruitMartRepositoryImpl(FruitMartRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self):
        fruitDict = {'Apple': 50, 'Orange': 60, "Strawberry": 70}  # 과일 목록

        stock = []

        for fruitName, count in fruitDict.items():
            fruitMart = FruitMart(fruitName=fruitName, count=count)
            fruitMart.save()

        stock.append(model_to_dict(fruitMart))

        return stock


    def findById(self, id):
        return FruitMart.objects.get(id=id)

    #def findByGameId(self, game):
    #    return Dice.objects.filter(game=game)

    def findAll(self):
        return FruitMart.objects.all()

    #def findByGameAndPlayer(self, game, player):
    #    return Dice.objects.filter(game=game, player=player)
