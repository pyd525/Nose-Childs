from django.db import models


class Account(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.IntegerField()

    def __str__(self):
        return f"주사위 id: {self.accountId}, 눈금: {self.accountName}"

    def getAccountId(self):
        return self.accountId

    def getAccountNumber(self):
        return self.accountName

    class Meta:
        db_table = "account"