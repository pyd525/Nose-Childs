from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fruit_mart.serializer.fruit_mart_serializer import FruitMartSerializer
# Serializer 왜있는지 일단 모르겠지만 있으니까 했음.
from fruit_mart.service.fruit_mart_service_impl import FruitMartServiceImpl


# Create your views here.
class DiceController(viewsets.ViewSet):
   diceService = FruitMartServiceImpl.getInstance()

    def requestRollDice(self, request):
        requestGetData = request.GET
        requestPlayerId = requestGetData.get('playerId')
        gameId = requestGetData.get('gameId')

        dice = self.diceService.rollDice(gameId, requestPlayerId)

        return Response(dice, status=status.HTTP_200_OK)

    def requestFindDice(self, request):
        requestGetData = request.GET
        requestDiceId = requestGetData.get('id')

        foundDice = self.diceService.findDice(requestDiceId)

        return Response(
            model_to_dict(foundDice),
            status=status.HTTP_200_OK)

    def requestEveryDice(self, request):
        diceList = self.diceService.findEveryDice()

        # diceList 중 JSON 변환 할 항목들을 미리 지정하고
        # serializer.data로 변환한 항목을 리턴함
        serializer = DiceSerializer(diceList, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
