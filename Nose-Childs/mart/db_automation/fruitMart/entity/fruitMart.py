from django.db import models


class FruitMart(models.Model):

    id = models.AutoField(primary_key=True)   # FruitMart table 참고하기/ 여기 id는 과일 id가 될 것임
    fruitName = models.CharField(max_length=50)  # 과일 이름
    counter = models.IntegerField()   # 과일 수량


    def __str__(self):
        return f"입고 숫자: {self.id}, 과일 이름: {self.fruitName}, 과일 수량: {self.counter}"

    def getId(self):
        return self.id

    def getFruitName(self):
        return self.fruitName

    def getFruitCounter(self):
        return self.counter

    class Meta:
        db_table = "FruitMart"
