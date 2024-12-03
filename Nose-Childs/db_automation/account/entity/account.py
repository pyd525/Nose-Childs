from django.db import models


class Account(models.Model):

    accountId = models.AutoField(primary_key=True)

    accountName = models.CharField(max_length=255)

    def __str__(self):
        return f"주사위 id: {self.accountId}, 눈금: {self.accountName}"

    def getAccountId(self):
        return self.accountId

    def getAccountName(self):
        return self.accountName

    class Meta:
        db_table = "account"