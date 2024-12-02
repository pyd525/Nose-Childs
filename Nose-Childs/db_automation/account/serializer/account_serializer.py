from rest_framework import serializers

from db_automation.account.entity.account import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['accountId', 'name']