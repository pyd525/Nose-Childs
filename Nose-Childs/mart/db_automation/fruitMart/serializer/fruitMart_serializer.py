from rest_framework import serializers

from fruitMart.entity.fruitMart import FruitMart


class FruitMartSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitMart
        fields = ['id', 'fruitName', 'count']

