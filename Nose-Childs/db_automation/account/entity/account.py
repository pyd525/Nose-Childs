from django.db import models


class Account(models.Model):

    id = models.AutoField(primary_key=True)  # accountId

    accountName = models.CharField(max_length=255)

    def getAccountId(self):
        return self.id

    def getAccountName(self):
        return self.accountName

    class Meta:
        db_table = "account"