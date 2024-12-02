from django.db import models

class Dice(models.Model):

    #id = models.AutoField(primary_key=True)
    number = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"주사위 결과: {self.number}"

    def getNumber(self):
        return self.number

    class Meta:
        db_table = "dice"
