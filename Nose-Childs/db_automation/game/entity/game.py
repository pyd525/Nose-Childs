from django.db import models

class Game:
    id = models.AutoField(primary_key=True)
    # gamePlayerId로 하고 싶었으나.../ accountId, diceId 도 primary_key
    diceNumber = models.IntegerField()  # 앤 dice에서 옴.
    gameFinalResult = models.CharField(max_length=255)

    #def __str__(self):
    #    return f" 게임의 결과: {self.id}, 눈금: {self.accountName}"
    # id의 diceNumber의 합으로

    def getGameId(self):
        return self.id

    def getGameFinalResult(self):
        return self.gameFinalResult

    class Meta:
        db_table = "game"