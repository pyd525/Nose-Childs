from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.response import Response
from fruitMart.serializer.fruitMart_serializer import FruitMartSerializer
# Serializer 왜있는지 일단 모르겠지만 있으니까 했음.
from fruitMart.service.fruitMart_service_impl import FruitMartServiceImpl

# 우리 DB에
        # [ {"id": 1, "fruitName": "Apple", "count": 50},
        #   {"id": 2, "fruitName": "Orange", "count": 50},
        #   {"id": 3, "fruitName": "Strawberry", "count": 50} ] 이렇게 저장되어 있음.
        # 따라서, fruitMartId는 앞에 id가 되는 것임.

# Create your views here.
class FruitMartController(viewsets.ViewSet):
   fruitMartService = FruitMartServiceImpl.getInstance()

   def requestStockFruit(self, request):
        requestGetData = request.GET
        fruitMartId = requestGetData.get('fruitMartId')

        fruitMart = self.fruitMartService.sellFruit(fruitMartId)

        return Response(fruitMart, status=status.HTTP_200_OK)


   def requestEveryFruit(self, request):
        fruitMartList = self.fruitMartService.findEveryFruit()

        serializer = FruitMartSerializer(fruitMartList, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
