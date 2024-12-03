from django.db import models

#dice - 게임에서 나온 dice 숫자 -> 나온 주사위 값 4개: {1, 2, 5, 3}
#앞 두개 : 첫번째 플레이어 dice 값, 뒤 두개: 두번째 플레이어 dice 값


class Dice(models.Model):

    id = models.AutoField(primary_key=True)  # diceId로 하고 싶었다... / accountId도 primary_key
    diceNumber = models.IntegerField()
    # 주사위 굴려서 나온 값 한개 : diceNumber

    def __str__(self):
        return f"주사위 결과: {self.diceNumber}"

    def getDiceId(self):
        return self.id

    def getDiceNumber(self):
         return self.diceNumber

    class Meta:
        db_table = "dice"
