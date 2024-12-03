import random
from django.forms import model_to_dict

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository
#from dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None

    #__diceList = []

    MIN = 1
    MAX = 6

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
        diceNumber1 = random.randint(self.MIN, self.MAX)
        diceNumber2 = random.randint(self.MIN, self.MAX)
        diceResult = diceNumber1 + diceNumber2
        dice = Dice(number = diceResult) ## 오류 생길 가능성 큼...

        dice.save()
        return model_to_dict(dice)


        #self.__diceList.append(dice)

    def findById(self, number):
        return Dice.objects.get(number=number)


    # E.g. __diceList = [ 3, 5 ]
    # Player1의 game 결과 값  1, 2: __diceList[0]   # 3
    # Player2의 game 결과 값: 3,2  __diceList[1]   # 5


    #def findAll(self):
        # db에 저장된 모든 주사위 데이터를 조회
    #    return Dice.objects.all()  # 전부 찾기